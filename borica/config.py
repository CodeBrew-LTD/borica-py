import os
from borica.exceptions import ImproperlyConfigured

CONFIG = None


def configure(config):
    global CONFIG
    CONFIG = Config.from_dict(config)


class Config:

    def __init__(
            self,
            terminal: str,
            merchant: str,
            dev_pem: str,
            dev_apgw_pem: str,
            dev_url: str,
    ):
        self.terminal = terminal
        self.merchant = merchant
        self.dev_pem = dev_pem
        self.dev_apgw_pem = dev_apgw_pem
        self.dev_url = dev_url
        self.validate()

    @classmethod
    def from_dict(cls, config):
        return cls(
            terminal=config['TERMINAL'],
            merchant=config['MERCHANT'],
            dev_pem=config['DEV_PEM'],
            dev_apgw_pem=config['DEV_APGW_PEM'],
            dev_url=config['DEV_URL']
        )

    def validate(self):
        fields = [
            'terminal',
            'merchant',
            'dev_pem',
            'dev_apgw_pem',
            'dev_url'
        ]
        for field in fields:
            field_value = getattr(self, field, None)
            if not field_value:
                raise ImproperlyConfigured(
                    f'Empty value found for field {field} in Borica config.'
                )
        for field in ('dev_pem', 'dev_apgw_pem'):
            filepath = getattr(self, field)
            if not os.path.exists(filepath):
                raise ImproperlyConfigured(
                    f'File {filepath} does not exist '
                    f'for Borica config option {field}.'
                )
