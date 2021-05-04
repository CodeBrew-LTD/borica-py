# -*- coding: utf-8 -*-
import os
import sys
from json import loads
from borica.config.config import configure
from borica.exceptions import file_exception
from borica.settings import check

CONFIG_FILE = 'borica/settings/settings.json'

if not os.path.isfile(CONFIG_FILE):
    check()

try:
    CONFIG_DICT = loads(open(CONFIG_FILE, 'r').read())
    configure(CONFIG_DICT)
except FileNotFoundError:
    raise file_exception(CONFIG_FILE, 'all')


__all__ = (
    'configure',
    'CONFIG_DICT'
)