# -*- coding: utf-8 -*-
import uuid
import binascii
import decimal
from datetime import datetime
from base64 import b64encode, b64decode
from typing import Any

from OpenSSL import crypto

from borica import config
from borica.base import BoricaSignMixin
from borica.exceptions import ImproperlyConfigured


class BoResponse(BoricaSignMixin):

    def __init__(self, data):
        self.config = config.CONFIG
        self.raw_data = data
        self.sign_fields = [
            'action',
            'rc',
            'approval',
            'terminal',
            'trtype',
            'amount',
            'currency',
            'order',
            'rrn',
            'int_ref',
            'pares_status',
            'eci',
            'timestamp',
            'nonce'
        ]
        self.fields = [
            'auth_step_res',
            'card',
            'card_brand',
            'cardholderinfo',
            'lang',
            'p_sign',
            'statusmsg',
            'tran_date',
            *self.sign_fields
        ]

        self.message = self.generate_sign_data()
        self.is_verified = self.get_is_verified()

    def __getattribute__(self, name: str) -> Any:
        if name in self.fields:
            return self.raw_data.get(name.upper())
        return super().__getattribute__(name)

    def __setattr__(self, name: str, value: Any) -> None:
        if name in self.fields:
            self.raw_data[name.upper()] = value
        else:
            super().__setattr__(name, value)

    def get_is_verified(self):
        with open(self.config.dev_apgw_pem, 'rb') as cf:
            cert_data = cf.read()
            pkey = crypto.load_publickey(crypto.FILETYPE_PEM, cert_data)
        x509 = crypto.X509()
        x509.set_pubkey(pkey)
        binary_string = binascii.unhexlify(self.p_sign)
        try:
            crypto.verify(x509, binary_string, self.message, "sha256")
            return True
        except:
            return False
