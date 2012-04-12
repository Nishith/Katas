import unittest
import Gilded_Rose

class TestGildedRose(unittest.TestCase):

    g = Gilded_Rose.GildedRose()

    names = ['+5 Dexterity Vest', 'Aged Brie', 'Elixir of the Mongoose', 'Sulfuras, Hand of Ragnaros', 'Backstage passes to a TAFKAL80ETC concert', 'Conjured Mana Cake']

    def setUp(self):
        self.r = Gilded_Rose.GildedRose()

    def test_names(self):
        l = [i.name for i in self.g.items]
        self.assertEqual(l, self.names)
        
    def test_vest_sellIn(self):
        self.r.UpdateQuality()
        self.assertEqual(self.r.items[0].sellIn, 9)

    def test_Vest_quality(self):
        self.r.UpdateQuality()
        self.assertEqual(self.r.items[0].quality, 19)

    def test_Vest_quality_expired(self):
        for i in range(0, self.r.items[0].sellIn+1):
            self.r.UpdateQuality()
        self.assertEqual(self.r.items[0].quality, 8)

    def test_Elixer_past_sellIn(self):
        for i in range(0, self.r.items[2].sellIn+1):
            self.r.UpdateQuality()
        self.assertEqual(self.r.items[2].quality, 0)

    def test_Elixer_past_sellIn_negative_quality(self):
        for i in range(0, self.r.items[2].sellIn+5):
            self.r.UpdateQuality()
        self.assertGreaterEqual(self.r.items[2].quality, 0)

    def test_Aged_Brie(self):
        for i in range(0, 5):
            self.r.UpdateQuality()
        self.assertEqual(self.r.items[1].quality, 5)

    def test_Aged_Brie_ten_days_after_sellIn(self):
        for i in range(0, self.r.items[1].sellIn+10):
            self.r.UpdateQuality()
        self.assertEqual(self.r.items[1].quality, 12)

    def test_Sulfuras(self):
        for i in range(0, 5):
            self.r.UpdateQuality()
        self.assertEqual(self.r.items[3].quality, 80)
        self.assertEqual(self.r.items[3].sellIn, 0)

    def test_Backstage_Pass_eleven_days(self):
        for i in range(0, 3):
            self.r.UpdateQuality()
        self.assertEqual(self.r.items[4].quality, 23)

    def test_Backstage_Pass_seven_days(self):
        for i in range(0, 8):
            self.r.UpdateQuality()
        self.assertEqual(self.r.items[4].quality, 32)

    def test_Backstage_Pass_last_day(self):
        for i in range(0, 14):
            self.r.UpdateQuality()
        self.assertEqual(self.r.items[4].quality, 49)

    def test_Backstage_Pass_Expired(self):
        for i in range(0, 16):
            self.r.UpdateQuality()
        self.assertEqual(self.r.items[4].quality, 0)

    def test_conjured(self):
        for i in range(0, self.r.items[5].sellIn):
            self.r.UpdateQuality()
        self.assertEqual(self.r.items[5].quality, 0)

    
if __name__ == '__main__':
    unittest.main()
