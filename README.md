# borica-py

Python package for integrating borica-based online payments.

![borica-py](/docs/img/logo.jpg)

## Usage

```python

import borica

borica.configure(
    {
        'TERMINAL': 'TERMINAL VALUE',
        'MERCHANT': 'MERCHANT VALUE',
        'DEV_PEM': '/path/to/certificate/dev.pem',
        'DEV_APGW_PEM': '/path/to/certificate/apgw_dev.pem',
        'DEV_URL': 'https://gateway.borica.bg/example-url'
    }
)
```