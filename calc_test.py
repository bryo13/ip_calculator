import unittest
import calc

class TestCalculator(unittest.TestCase):
    def test_private_or_public_ip(self):
        self.assertEqual(calc.private_or_public_ip("123"),"error")