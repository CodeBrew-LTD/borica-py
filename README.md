# borica-py

Python package for integrating borica-based online payments.

![borica-py](/docs/img/logo.jpg)

## Usage
   - in order of using this packages you must fill your endpoint details 
     in to [settings.json](settings.json) file or input them manually during the installation.
     
     ###### ***Mandatory parameters are:***
     ```json
     {
       "TERMINAL": "TERMINAL identification number.",
       "MERCHANT": "MERCHANT identification number.",
       "PEM": "MERCHANT private key.",
       "APGW_PEM": "Borica APGW public key.",
       "URL": "Borica APGW url.",
       "TIMEZONE": "Current timezone."
     }
     ```