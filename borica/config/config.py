from borica.config.fields import CONFIG_FIELDS

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
        timezone: str,
    ):
        self.terminal = terminal
        self.merchant = merchant
        self.dev_pem = dev_pem
        self.dev_apgw_pem = dev_apgw_pem
        self.dev_url = dev_url
        self.timezone = timezone

    @classmethod
    def from_dict(cls, config):
        kwags = {
            k.lower(): v('%({})s'.format(k) % config) for k, v in CONFIG_FIELDS.items()
        }

        return cls(**kwags)
