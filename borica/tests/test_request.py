# -*- coding: utf-8 -*-
import unittest
from borica.tests import TestMixin
from borica.request import BoRequest


class TestRequest(TestMixin):
    def test_request(self):
        initial_content = {
            'amount': float(self.request_dict['amount']),
            'order': self.request_dict['order'],
        }
        request = BoRequest(**initial_content)
        self.assertTrue(isinstance(request.jsonify, dict))


if __name__ == '__main__':
    unittest.main()
