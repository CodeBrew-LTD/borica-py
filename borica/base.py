# -*- coding: utf-8 -*-
import re


def generate_sign_data(self):
    message = ''
    for field in self.sign_fields:
        field_text = getattr(self, field) or '-'
        length = '' if field_text == '-' else len(field_text)
        message += str(length) + field_text

    # convert str: message ot bytes: message because of DeprecationWarning: str for data is no longer accepted, use bytes
    message = bytes(message, encoding="raw_unicode_escape")

    return message


def sign_fields(self):
    return __import__(
        re.sub(r'(.\w+)$', '', self.__module__), globals(), locals(), ['sign_fields']
    ).sign_fields


BoricaSignMixin = type(
    'BoricaSignMixin',
    (),
    {
        'sign_fields': property(sign_fields),
        'generate_sign_data': generate_sign_data,
    },
)
