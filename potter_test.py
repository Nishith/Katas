import unittest
import potter

class TestPotter(unittest.TestCase):

    def setUp(self):
        self.d = potter.discount()
        
    def testBasics(self):
        self.assertEqual(0, self.d.cost([]))
        self.assertEqual(8, self.d.cost(["0"]))
        self.assertEqual(8, self.d.cost(["1"]))
        self.assertEqual(8, self.d.cost(["2"]))
        self.assertEqual(8, self.d.cost(["3"]))
        self.assertEqual(8, self.d.cost(["4"]))
        self.assertEqual(8 * 2, self.d.cost(["0", "0"]))
        self.assertEqual(8 * 3, self.d.cost(["1", "1", "1"]))

    def testSimpleDiscounts(self):
        self.assertEqual(8 * 2 * 0.95, self.d.cost(["0", "1"]))
        self.assertEqual(8 * 3 * 0.9, self.d.cost(["0", "2", "4"]))
        self.assertEqual(8 * 4 * 0.8, self.d.cost(["0", "1", "2", "4"]))
        self.assertEqual(8 * 5 * 0.75, self.d.cost(["0", "1", "2", "3", "4"]))

    def testSeveralDiscounts(self):
        self.assertEqual(8 + (8 * 2 * 0.95), self.d.cost(["0", "0", "1"]))
        self.assertEqual(2 * (8 * 2 * 0.95), self.d.cost(["0", "0", "1", "1"]))
        self.assertEqual((8 * 4 * 0.8) + (8 * 2 * 0.95), self.d.cost(["0", "0", "1", "2", "2", "3"]))
        self.assertEqual(8 + (8 * 5 * 0.75), self.d.cost(["0", "1", "1", "2", "3", "4"]))

    def testEdgeCases(self):
        self.assertEqual(2 * (8 * 4 * 0.8), self.d.cost(["0", "0", "1", "1", "2", "2", "3", "4"]))
        self.assertEqual(4 * (8 * 5 * 0.75) + 1 * (8 * 4 * 0.8), self.d.cost(["0", "0", "0", "0", "0", "1", "1", "1", "1", "1", "2", "2", "2", "2", "3", "3", "3", "3", "3", "4", "4", "4", "4"]))

        
if __name__ == "__main__":
    unittest.main()
