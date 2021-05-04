# -*- coding: utf-8 -*-
import os
from borica.exceptions import field_exception, file_exception


def _set_var(field, value):
    os.environ[field] = value

    return value


def _raise(exception):

    raise exception


_validate_value = (
    lambda field, value: _set_var(field, value)
    if value
    else _raise(field_exception(field))
)

_validate_file = (
    lambda field, value: _set_var(field, value)
    if os.path.exists(value)
    else _raise(file_exception(value, field))
)
