"""Hi and welcome to team Gilded Rose. As you know, we are a small inn with a prime location in a prominent city ran by a friendly innkeeper named Allison. We also buy and sell only the finest goods. Unfortunately, our goods are constantly degrading in quality as they approach their sell by date. We have a system in place that updates our inventory for us. It was developed by a no-nonsense type named Leeroy, who has moved on to new adventures. Your task is to add the new feature to our system so that we can begin selling a new category of items. First an introduction to our system:

All items have a SellIn value which denotes the number of days we have to sell the item
All items have a Quality value which denotes how valuable the item is
At the end of each day our system lowers both values for every item
Pretty simple, right? Well this is where it gets interesting:

Once the sell by date has passed, Quality degrades twice as fast
The Quality of an item is never negative
“Aged Brie” actually increases in Quality the older it gets
The Quality of an item is never more than 50
“Sulfuras”, being a legendary item, never has to be sold or decreases in Quality
“Backstage passes”, like aged brie, increases in Quality as it’s SellIn value approaches; Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but Quality drops to 0 after the concert
We have recently signed a supplier of conjured items. This requires an update to our system:

“Conjured” items degrade in Quality twice as fast as normal items
Feel free to make any changes to the UpdateQuality method and add any new code as long as everything still works correctly. However, do not alter the Item class or Items property as those belong to the goblin in the corner who will insta-rage and one-shot you as he doesn’t believe in shared code ownership (you can make the UpdateQuality method and Items property static if you like, we’ll cover for you)."""

import re

class Items:
    name = ""
    sellIn = 0
    quality = 0

    def __init__(self, name, sellIn, quality):
        self.name = name
        self.sellIn = sellIn
        self. quality = quality

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name
    
    def getSellIn(self):
        return self.sellIn
    
    def setSellIn(self, sellIn):
        self.sellIn = sellIn

    def getQuality(self):
        return self.quality

    def setQuality(self, quality):
        self.quality = quality

class GildedRose:

    def __init__(self):
        """Initialize the item list"""
        self.items = []
        self.items += [Items("+5 Dexterity Vest", 10, 20)]
        self.items += [Items("Aged Brie", 2, 0)]
        self.items += [Items("Elixir of the Mongoose", 5, 7)]
        self.items += [Items("Sulfuras, Hand of Ragnaros", 0, 80)]
        self.items += [Items("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        self.items += [Items("Conjured Mana Cake", 3, 6)]

    def UpdateQuality(self):
        for i in self.items:
            """Sulfuras, has no sell by date and does not decrease in quality"""
            if i.name == "Sulfuras, Hand of Ragnaros":
                break

            """Aged Brie increases in quality as it ages so we increase it by double the amount,
               So that it can then take the normal path.
            """
            if i.name == "Aged Brie":
                i.quality = i.quality + 2
                if i.sellIn <= 0:
                    i.quality = i.quality + 2

            """A concert pass increases in value as the sell by date approaches
               Quality increases by 2 when there are 10 days or less and by 3
               when there are 5 days or less but Quality drops to 0 after the concert
            """
            if i.name == "Backstage passes to a TAFKAL80ETC concert":
                print("Concert")
                if i.sellIn < 1:
                    i.quality = 0
                    break

                i.quality = i.quality + 2
                if i.sellIn < 11:
                    i.quality = i.quality + 1
                if i.sellIn <= 5 and i.sellIn >= 0:
                    i.quality = i.quality + 1
                
                
                    
            if i.sellIn >= 0:
                i.sellIn = i.sellIn - 1
            if i.quality > 0:
                i.quality = i.quality - 1
            if i.sellIn < 0 and i.quality > 0:
                i.quality = i.quality - 1

            if re.search("Conjured", i.name):
                i.quality = i.quality - 1
                if i.sellIn < 0:
                    i.quality = i.quality - 1
            """The quality can never be more than 50
               So, if it more than 50 we set it back to 50.
            """
            if i.quality > 50:
                i.quality = 50

            
if __name__ == '__main__':
    g = GildedRose()
    for i in range(0, 5):
        g.UpdateQuality()
    for i in g.items:
        print(i.quality)
