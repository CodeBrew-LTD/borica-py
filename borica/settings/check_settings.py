# -*- coding: utf-8 -*-
import os
import sys
import json
import inspect
from simple_colors import *


WORDS = {
    True: ('value', 'it'),
    False: ('values', 'them'),
}
MISSING_SETTINGS = (
    lambda missing: 'Your settings are missing mandatory {}'
    '\nyou must provide {} now in order to continue.\n'.format(
        *WORDS[missing == 1]
    )
)
INPUT_SETTING_VALUE = '\ninput {} value: '.format


def write_settings(settings: dict):
    with open('borica/settings/settings.json', 'w') as data:
        data.write(json.dumps(settings))


def read_settings(settings_path='') -> dict:
    with open(os.path.join(settings_path, 'settings.json'), 'r') as data:
        return json.loads(data.read())


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


if __name__ == '__main__':
    check()
