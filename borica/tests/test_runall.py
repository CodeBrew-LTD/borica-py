# -*- coding: utf-8 -*-
import unittest
from borica.config import config
from borica.request import BoRequest
from borica.response import BoResponse
from borica.tests.fixtures import configur, REQUEST, RESPONSE


class TestAll(unittest.TestCase):

    def setUp(self) -> None:
        self.request_dict = REQUEST
        self.response_dict = RESPONSE
        self.configuration = configur()
        self.request = None

    def test_2_serialization(self):
        request = BoRequest(**self.request_dict)
        self.response_dict.update({
            'nonce': request.nonce,
            'p_sign': request.p_sign
        })
        self.assertTrue(isinstance(request.jsonify, dict))


    def test_3_response(self):
        response = BoResponse(data=self.response_dict)

        self.assertFalse(response.get_is_verified())


    def test_1_config(self):
        self.assertTrue(isinstance(self.configuration, config.Config))


if __name__ == '__main__':
    loader = unittest.TestLoader()
    unittest.main(testLoader=loader, verbosity=2)