# -*- coding: utf-8 -*-
import unittest
from borica.config import CONFIG_DICT, configure, config
from borica.tests.constants import REQUEST_DATA, RESPONSE_DATA, CURRENT_DIR


class TestMixin(unittest.TestCase):
    config_dict = CONFIG_DICT
    request_dict = REQUEST_DATA
    response_dict = RESPONSE_DATA

    def setUp(self) -> None:
        configure(self.config_dict)
        self.config = config.CONFIG

