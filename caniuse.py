import argparse


class CanIUse():
    def __init__(self, feature=None, browsers=None):
        self.feature = feature
        self.browsers = browsers if browsers else []

    def parse_args(self):
        parser = argparse.ArgumentParser(description='Check if you can use ' \
                                                     'some feature in certain browser')
        parser.add_argument('feature', metavar="F", help="feature to check for support")
        parser.add_argument('--in', dest='browsers', nargs='*', help="browsers to check for")
        parser.parse_args(namespace=self)

    def _get_data(self):
        # here get data of support for features
        # look at https://github.com/Fyrd/caniuse/blob/master/data.json
        pass


if __name__ == '__main__':
    ciu = CanIUse()
    ciu.parse_args()
    print(ciu.feature, ciu.browsers)
