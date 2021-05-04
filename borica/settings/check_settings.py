# -*- coding: utf-8 -*-
import os
import sys
import json
import inspect
from simple_colors import *
from borica.settings.constants import *


def write_settings(settings: dict):
    with open('borica/settings/settings.json', 'w') as data:
        data.write(json.dumps(settings))


def read_settings(settings_path='') -> dict:
    settings_file = os.path.join(settings_path, 'settings.json')

    if os.path.isfile(settings_file):
        with open(settings_file, 'r') as data:
            return json.loads(data.read())

    with open('settings.json', 'r') as data:
        settings = json.loads(data.read())
        if all(list(map(None.__ne__, list(settings.values())))):
            write_settings(settings)
            return settings


def check_execution():
    stack = inspect.stack()
    executed = inspect.getfile(stack[-1][0])

    return executed.endswith('pytest'), executed.endswith('_in_process.py')


def check() -> callable:
    settings = read_settings()
    _testing, _building = check_execution()
    if _building:
        return
    if _testing:
        settings = read_settings(settings_path='borica/settings/')
    try:
        missing = len(settings).__sub__(
            len(list(filter(None.__ne__, list(settings.values()))))
        )
        if missing:
            sys.stdout.write(red(MISSING_SETTINGS(missing)))
            mandatory = settings.items().__iter__()
            while True:
                try:
                    key, value = mandatory.__next__()
                    if not value:
                        input_msg = INPUT_SETTING_VALUE(red(key.upper(), 'bold'))
                        settings[key] = input(input_msg)
                except StopIteration:
                    break

        return write_settings(settings)
    except (TypeError, FileNotFoundError) as e:
        sys.stderr.write(NO_CONFIG_FILE)


if __name__ == '__main__':
    check()
