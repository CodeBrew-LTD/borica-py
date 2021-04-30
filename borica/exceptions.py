class ImproperlyConfigured(Exception):
    """Borica is somehow improperly configured"""

    pass


field_exception = lambda field: ImproperlyConfigured(
    f'Empty value found for field {field} in Borica config.'
)
file_exception = lambda filepath, field: ImproperlyConfigured(
    f'File {filepath} does not exist or Borica config option {field}.'
)
