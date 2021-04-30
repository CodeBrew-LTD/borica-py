# -*- coding: utf-8 -*-
from borica.config.validators import _validate_value, _validate_file

CONFIG_FIELDS = {
    'DEV_PEM': lambda dev_pem: _validate_file('dev_pem', dev_pem),
    'DEV_URL': lambda dev_url: _validate_value('dev_url', dev_url),
    'MERCHANT': lambda merchant: _validate_value('merchant', merchant),
    'TERMINAL': lambda terminal: _validate_value('terminal', terminal),
    'TIMEZONE': lambda timezone: _validate_value('timezone', timezone),
    'DEV_APGW_PEM': lambda dev_apgw_pem: _validate_file('dev_apgw_pem', dev_apgw_pem),
}