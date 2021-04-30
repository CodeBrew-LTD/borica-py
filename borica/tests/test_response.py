# -*- coding: utf-8 -*-
import unittest
from borica.tests import TestMixin
from borica.response import BoResponse


class TestResponse(TestMixin):
    def test_response(self):
        response = BoResponse(data=self.response_dict)

        self.assertTrue(response.get_is_verified())


if __name__ == '__main__':
    unittest.main()
