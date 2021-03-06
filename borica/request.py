# -*- coding: utf-8 -*-
import uuid
import binascii
import decimal
import pytz
from datetime import datetime
from base64 import b64encode, b64decode

from OpenSSL import crypto

from borica.base import BoricaSignMixin
from borica import config
from borica.exceptions import ImproperlyConfigured


class BoRequest(BoricaSignMixin):

    def __init__(
            self,
            amount,
            order,
            currency='BGN',
            trtype=1,
            country="BG",
            email='',
            merchant=None,
            merch_name="",
            desc='',
            timestamp=None,
            terminal=None,
    ) -> None:
        self.config = config.CONFIG
        self.trtype = str(trtype)
        self.amount = "{:.2f}".format(amount)
        self.currency = str(currency)
        self.country = country
        self.order = order
        self.desc = str(desc)
        self.merchant = merchant or self.config.merchant
        self.merch_name = merch_name
        self.merch_gmt = self.get_timezone()
        self.timestamp = (
            timestamp or datetime.now()).strftime("%Y%m%d%H%M%S")
        self.terminal = str(terminal or self.config.terminal)
        self.email = email
        self.nonce = self.generate_nonce()
        self.sign_fields = [
            'terminal',
            'trtype',
            'amount',
            'currency',
            'order',
            'merchant',
            'timestamp',
            'nonce',
        ]
        self.sign_data = self.generate_sign_data()
        self.p_sign = self.generate_p_sign()

    def get_timezone(self):
        tz = self.config.timezone
        return datetime.now(pytz.timezone(tz)).strftime('%z')[:3]

    def generate_nonce(self):
        return uuid.uuid4().hex[:32].upper()

    def generate_p_sign(self):
        with open(self.config.dev_pem, 'rb') as cf:
            cert_data = cf.read()
            pkey = crypto.load_privatekey(crypto.FILETYPE_PEM, cert_data)
        sign = crypto.sign(pkey, self.sign_data, "sha256")
        return sign.hex().upper()

    def get_data(self):
        return {k.upper(): v for k, v in self.__dict__.items()}

    @property
    def __dict__(self):
        _dict = super().__dict__
        if 'config' in _dict.keys():
            _dict.pop('config')
        return _dict
