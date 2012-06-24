import unittest
import coinchange

class TestCoinChange(unittest.TestCase):

    def testZero(self):
        self.assertEqual([0,0,0,0,0], coinchange.change(0, [1,5,10,25,100]))

    def testOne(self):
        self.assertEqual([1,0,0,0,0], coinchange.change(1, [1,5,10,25,100]))

    def testFifteen(self):
        self.assertEqual([0,1,1,0,0], coinchange.change(15, [1,5,10,25,100]))

    def testForty(self):
        self.assertEqual([0,1,1,1,0], coinchange.change(40, [1,5,10,25,100]))
        
    def testOneFortyOne(self):
        self.assertEqual([1,1,1,1,1], coinchange.change(141, [1,5,10,25,100]))

    def testFour(self):
        self.assertEqual([4,0,0,0,0], coinchange.change(4, [1,5,10,25,100]))

    def testEmptyDenomination(self):
        self.assertEqual([0], coinchange.change(40, [0]))

    def test100Dollars(self):
        self.assertEqual([0,0,0,0,10000], coinchange.change(1000000, [1, 5, 10, 25, 100]))

    def testGreedy(self):
        self.assertEqual([0,0,0,2,0], coinchange.change(40, [1, 5, 10, 20, 25]))


if __name__ == '__main__':
    unittest.main()
