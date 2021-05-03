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
        pem: str,
        apgw_pem: str,
        url: str,
        timezone: str,
    ):
        self.terminal = terminal
        self.merchant = merchant
        self.pem = pem
        self.apgw_pem = apgw_pem
        self.url = url
        self.timezone = timezone

    @classmethod
    def from_dict(cls, config):
        kwags = {
            k.lower(): v('%({})s'.format(k) % config) for k, v in CONFIG_FIELDS.items()
        }

        return cls(**kwags)
