import unittest
from unittest.mock import patch
from converter import convert_currency


class TestCurrencyConverter(unittest.TestCase):

    @patch("converter.get_exchange_rate")
    def test_convert_currency(self, mock_get_rate):
        mock_get_rate.return_value = 0.9
        result = convert_currency(100, "USD", "EUR")
        self.assertEqual(result, 90.00)


if __name__ == "__main__":
    unittest.main()
