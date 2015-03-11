import json
import unittest
from unittest.mock import Mock, patch

import requests

from caniuse import CanIUse


class TestCanIUse(unittest.TestCase):
    def setUp(self):
        self.can_i_use = CanIUse()

    def test_defaults(self):
        self.assertEqual(self.can_i_use.browsers, [])
        self.assertIsNone(self.can_i_use.feature)
        self.assertIsNone(self.can_i_use.support_data)

    def test_get_data(self):
        valid_json = json.dumps({'test': 'gigla'})
        invalid_json = 'gigla-migla'
        fake_response = Mock()
        attrs = {'status_code': 200, 'text': valid_json}
        fake_response.configure_mock(**attrs)

        with patch.object(requests, 'get', return_value=fake_response) as mock_get:
            self.can_i_use._get_data()
        self.assertTrue(mock_get.assert_called())
        self.assertIsNotNone(self.can_i_use.support_data)

        attrs = {'status_code': 200, 'text': invalid_json}
        fake_response.configure_mock(**attrs)
        with patch.object(requests, 'get', return_value=fake_response) as mock_get:
            self.assertRaises(ValueError, self.can_i_use._get_data(exit_on_fail=False),
                              'Invalid data provided from url [%s]' % self.can_i_use.data_url)
        self.assertTrue(mock_get.assert_called())

    def test_find_feature(self):
        self.assertTrue(False)

    def test_store_data(self):
        self.assertTrue(False)

    def test_update_data(self):
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
