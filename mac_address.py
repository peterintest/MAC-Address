"""
Command-line tool to lookup company name associated with MAC address
using macaddress.io API
"""
import argparse
import os
import re
import requests


class MacAddressClient:
    """HTTP Client for macaddress.io API"""
    BASE_URL = 'https://api.macaddress.io/v1'
    API_KEY = os.getenv('API_KEY')

    @staticmethod
    def verify(mac_address):
        """Verify MAC address format"""
        mac_address_regex = r'^([0-9A-Fa-f]{2}[:.]){5}([0-9A-Fa-f]{2})$'
        match = re.match(mac_address_regex, mac_address)
        return bool(match)

    def lookup_company(self, mac_address):
        """Lookup company name associated with MAC address"""
        if not self.verify(mac_address):
            return f'Invalid MAC address: {mac_address}'
        try:
            response = requests.get(
                f'{self.BASE_URL}?apiKey={self.API_KEY}&output=vendor&search={mac_address}')
            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError as e:
                return f'Server error: {e}'
        except requests.exceptions.ConnectionError:
            return f'Connection error'
        return response.text


def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description="Command utility that returns the company name associated with a MAC address")
    parser.add_argument('mac_address',
                        type=str,
                        help='MAC address e.g. 44:38:39:ff:ef:57 or 44.38.39.ff.ef.57')
    parsed = parser.parse_args()
    return parsed


def main():
    args = parse_args()
    client = MacAddressClient()
    print(client.lookup_company(args.mac_address))


if __name__ == '__main__':
    main()

