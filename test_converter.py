import unittest
from unittest.mock import patch
from converter import convert_currency

class TestCurrencyConverter(unittest.TestCase):
    @patch("converter.get_exchange_rate")
    def test_convert_currency(self, mock_rate):
        mock_rate.return_value = 0.85  # Mock 1 USD = 0.85 EUR
        result = convert_currency(100, "USD", "EUR")
        self.assertEqual(result, 85.00)

if __name__ == "__main__":
    unittest.main()
