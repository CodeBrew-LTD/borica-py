# -*- coding: utf-8 -*-

import os
import sys
sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
import unittest
from borica.config import config
from borica.tests import TestMixin


class TestConfig(TestMixin):

    def test_config(self):
        self.assertTrue(isinstance(self.config, config.Config))


if __name__ == '__main__':
    unittest.main()