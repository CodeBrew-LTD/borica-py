# -*- coding: utf-8 -*-
from json import loads
from borica.config.config import configure

CONFIG_DICT = loads(open('configuration.json', 'r').read())
configure(CONFIG_DICT)

__all__ = (
    'configure',
    'CONFIG_DICT'
)