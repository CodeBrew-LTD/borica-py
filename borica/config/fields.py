# -*- coding: utf-8 -*-
from borica.config.validators import _validate_value, _validate_file

CONFIG_FIELDS = {
    'PEM': lambda pem: _validate_file('pem', pem),
    'URL': lambda url: _validate_value('url', url),
    'MERCHANT': lambda merchant: _validate_value('merchant', merchant),
    'TERMINAL': lambda terminal: _validate_value('terminal', terminal),
    'TIMEZONE': lambda timezone: _validate_value('timezone', timezone),
    'APGW_PEM': lambda apgw_pem: _validate_file('apgw_pem', apgw_pem),
}