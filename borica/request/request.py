# -*- coding: utf-8 -*
import uuid
import pytz
from OpenSSL import crypto
from datetime import datetime
from borica.request import CONFIG
from borica.base import BoricaSignMixin


class BoRequest(BoricaSignMixin):
    """Base verification request.
    Dynamic class attributes set by `__seattr__` method are:
        'trtype', 'amount', 'currency', 'country', 'order', 'desc',
        'dev_pem', 'merchant', 'merch_name', 'timezone', 'timestamp',
        'terminal', 'email', 'nonce', 'sign_data', 'p_sign'
    """

    jsonify = property(lambda self: self.__dict__)
    merch_gmt = property(
        lambda self: datetime.now(pytz.timezone(self.timezone)).strftime('%z')[
            :3
        ]
    )

    def __setattr__(self, key, value):
        self.__dict__[key] = value or getattr(CONFIG, key, value)

    def __init__(
        self,
        amount,
        order,
        currency,
        trtype,
        country,
        email='',
        merch_name="",
        desc='',
        merchant=None,
        pem=None,
        timezone=None,
        timestamp=None,
        terminal=None,
    ) -> None:
        self.trtype = str(trtype)
        self.amount = "{:.2f}".format(float(amount))
        self.currency = str(currency)
        self.country = country
        self.order = order
        self.desc = str(desc)
        self.pem = pem
        self.merchant = merchant
        self.merch_name = merch_name
        self.timezone = timezone
        self.timestamp = (timestamp or datetime.now()).strftime("%Y%m%d%H%M%S")
        self.terminal = terminal
        self.email = email

    @property
    def sign_data(self):
        return self.generate_sign_data()

    @property
    def nonce(self):
        return uuid.uuid4().hex[:32].upper()

    @property
    def p_sign(self):
        with open(self.pem, 'rb') as data:
            cert_data = data.read()
        pkey = crypto.load_privatekey(crypto.FILETYPE_PEM, cert_data)
        sign = crypto.sign(pkey, self.sign_data, "sha256").hex().upper()

        return sign
