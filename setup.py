# -*- coding: utf-8 -*-
import os
import sys
from setuptools import setup, find_packages
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def main():
    pkg_setup = {
        'name': 'borica-py',
        'version': '0.0.1',
        'package': ['borica'],
        'name_space_packages': ['borica'],
        'description': 'Python integration for Borica based payments',
        'long_description': open('README.md', 'r').read(),
        'long_description_content_type': 'text/markdown',
        'author': 'CodeBrew',
        'author_email': 'contact@codebrew.io',
        'packages': find_packages(),
        'python_requires': '>=3.8',
        'install_requires': [
            'pyOpenSSL==20.0.*',
            'pytest>=6.2.3',
            'simple_colors>=0.1.5',
        ],
        'extras_require': {},
        'include_package_data': True,
        'license': 'MIT',
    }
    setup(**pkg_setup)


if __name__ == '__main__':
    """this import initiates the settings checker"""
    from borica.settings import check

    main()
