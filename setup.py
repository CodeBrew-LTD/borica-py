import os
from setuptools import setup, find_packages


with open('README.md', 'r') as fh:
    LONG_DESCRIPTION = fh.read()


def main():
    # Package meta-data preparation
    pkg_setup = {
        'name': 'borica-py',
        'version': '0.0.0',
        'description': 'Python integration for Borica based payments',
        'long_description': LONG_DESCRIPTION,
        'long_description_content_type': 'text/markdown',
        'author': 'CodeBrew',
        'author_email': 'contact@codebrew.io',
        'packages': find_packages(),
        'python_requires': '>=3.7',
        'install_requires': [
            'pyOpenSSL==20.0.*',
        ],
        'extras_require': {},
        'include_package_data': True,
        'license': 'MIT',
    }
    # Do the actual setup
    setup(**pkg_setup)


if __name__ == '__main__':
    main()