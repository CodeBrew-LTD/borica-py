# -*- coding: utf-8 -*-
import pytest
from json import loads
from requests import request
from borica.config import CONFIG_DICT, configure, config


REQUEST = loads(open('borica/tests/request.json', 'r').read())
RESPONSE = loads(open('borica/tests/response.json', 'r').read())


def configur():
    configure(CONFIG_DICT)
    return config.CONFIG


@pytest.fixture
def configuration():
    return configur()


@pytest.fixture
def request_dict():
    return REQUEST


@pytest.fixture
def response_dict():
    return RESPONSE