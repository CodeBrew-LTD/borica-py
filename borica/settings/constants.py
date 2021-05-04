# -*- coding: utf-8 -*-

SETTINGS_TEMPLATE = {
    "TERMINAL": None,
    "MERCHANT": None,
    "PEM": None,
    "APGW_PEM": None,
    "URL": None,
    "TIMEZONE": None
}

NO_CONFIG_FILE = 'You can not run tests without configuration file,\n' \
                 'to create configuration execute pytest -s\n' \
                 'or fill in your details into settings.json file.'

WORDS = {
    True: ('value', 'it'),
    False: ('values', 'them'),
}
MISSING_SETTINGS = (
    lambda missing: 'Your settings are missing mandatory {}'
    '\nyou must provide {} now in order to continue.\n'.format(
        *WORDS[missing == 1]
    )
)
INPUT_SETTING_VALUE = '\ninput {} value: '.format