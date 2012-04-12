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

def normal(item):
    """
    Quality degrades by one each day.
    Once the sell by date has passed, Quality degrades twice as fast.
    """
    item.quality -= 1
    if item.sellIn < 0:
        item.quality -= 1

def ageWell(item):
    """
    Quality increases as the item gets older
    """
    item.quality += 1

def showPasses(item):
    """
    Increases in Quality as it’s SellIn value approaches;
    Quality increases by 2 when there are 10 days or less
    and by 3 when there are 5 days or less but
    Quality drops to 0 after the concert
    """
    item.quality += 1
    if item.sellIn <= 10:
        item.quality += 1
    if item.quality <= 5:
        item.quality += 1

def conjured(item):
    """
    “Conjured” items degrade in Quality twice as fast as normal items
    """
    normal(item)
    normal(item)

def legendary(item):
    """
    Legendary items don't care about sellIn dates or quality
    """
    pass

class GildedRose:
    
        def __init__(self):
            self.items = []
            self.rules = {}
            
            self.addItem("+5 Dexterity Vest", 10, 20, normal)
            self.additem("Aged Brie", 2, 0, ageWell)
            self.addItem("Elixir of the Mongoose", 5, 7, normal)
            self.addItem("Sulfuras, Hand of Ragnaros", 0, 80, legendary)
            self.addItem("Backstage passes to a TAFKAL80ETC concert", 15, 20, showPasses)
            self.addItem("Conjured Mana Cake", 3, 6, conjured)

        
        def addItem(self, name, sellIn, quality, rule = normal):
            self.items += [Items(name, sellIn, quality)]
            self.rules[hash(Items(name, sellIn, quality))] = rule
            
        def UpdateQuality(self):
            for i in self.items:
                i.sellIn -= 1
                self.rules[hash(i)](i)
                if i.quality > 50:
                    i.quality = 50
                if i.sellIn < 0:
                    i.sellIn = 0
