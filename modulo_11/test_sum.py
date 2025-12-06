# test_sum.py

import unittest
from calc import somar


class TestSomar(unittest.TestCase):

    def test_soma_basica(self):
        self.assertEqual(somar(2, 3), 5)

    def test_soma_negativos(self):
        self.assertEqual(somar(-1, -4), -5)


if __name__ == "__main__":
    unittest.main()
