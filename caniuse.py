import sys
import json
import argparse

import requests


class CanIUse():
    def __init__(self, feature=None, browsers=None):
        self.feature = feature
        self.browsers = browsers if browsers else []
        self.support_data = None
        self.data_url = 'https://raw.githubusercontent.com/Fyrd/caniuse/master/data.json'

    def parse_args(self):
        parser = argparse.ArgumentParser(description='Check if you can use ' \
                                                     'some feature in certain browser')
        parser.add_argument('feature', metavar="F", help="feature to check for support")
        parser.add_argument('--in', dest='browsers', nargs='*', help="browsers to check for")
        parser.parse_args(namespace=self)

    def _get_data(self, exit_on_fail=True):
        r = requests.get(self.data_url)
        if r.status_code != 200:
            if exit_on_fail:
                sys.exit('Cannot get data from provided url [%s]' % self.data_url)
            else:
                return
        try:
            self.support_data = json.loads(r.text)
        except ValueError:
            if exit_on_fail:
                sys.exit('Invalid data provided from url [%s]' % self.data_url)
            else:
                return

    def _store_data(self):
        """
        Store data localy for not making requests and parsing json latter
        """
        pass

    def _find_feature(self):
        """
        Finds feautre provided as cli argsnd returns its support status
        """
        pass

    def _update_data(self):
        """
        Checks for data updates and store new data for latter use
        """
        pass


if __name__ == '__main__':
    ciu = CanIUse()
    ciu.parse_args()
    print(ciu.feature, ciu.browsers)
