import unittest
import coin_change

class TestCoinChange(unittest.TestCase):

    def test_one(self):
        change = coin_change.get_change([1], 1)
        self.assertEqual(change, [1])

    def test_o(self):
        change = coin_change.get_change([1], 1)
        self.assertEqual(change, [1])

    def test_one(self):
        change = coin_change.get_change([1], 1)
        self.assertEqual(change, [1])


if __name__ == '__main__':
    unittest.main()
