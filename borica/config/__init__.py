# -*- coding: utf-8 -*-
from json import loads
from borica.config.config import configure

CONFIG_DICT = loads(open('borica/settings/settings.json', 'r').read())
configure(CONFIG_DICT)

__all__ = (
    'configure',
    'CONFIG_DICT'
)