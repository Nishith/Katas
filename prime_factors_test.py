import unittest
import prime_factors

class TestPrimeFactors(unittest.TestCase):
    """
    Test the function which generates a list of prime factors for
    its argument.
    """
    
    def test_generate_one(self):
        self.assertEqual(prime_factors.generate(1), [])

    def test_generate_fifteen(self):
        self.assertEqual(prime_factors.generate(15), [3,5])

    def test_generate_sixteen(self):
        self.assertEqual(prime_factors.generate(16), [2,2,2,2])

    def test_generate_seventyeight(self):
        self.assertEqual(prime_factors.generate(78), [2,3,13])

if __name__ == '__main__':
    unittest.main()
