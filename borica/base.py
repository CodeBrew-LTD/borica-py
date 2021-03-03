

class BoricaSignMixin:

    def __init__(self):
        self.sign_fields = []

    def generate_sign_data(self):
        message = ''
        for field in self.sign_fields:
            field_text = getattr(self, field, '')
            length = len(field_text) or ''
            field_text = field_text or '-'
            message += str(length) + field_text
        return message