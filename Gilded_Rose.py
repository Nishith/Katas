
class Items:
    """
    This is the kata's item class.
    No changes because of the annoying Goblin.
    """
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

####################################################################################################

def qualitySanity(i):
    """
    Make sure the quality is within range
    """
    if i.quality > 50:
        i.quality = 50
    if i.quality < 0:
        i.quality = 0
            
####################################################################################################

"""
Various rules that are applied to the objects in the shop.
"""

def normal(item):
    """
    Quality degrades by one each day.
    Once the sell by date has passed, Quality degrades twice as fast.
    """
    item.quality -= 1
    if item.sellIn < 0:
        item.quality -= 1
    qualitySanity(item)

def ageWell(item):
    """
    Quality increases as the item gets older
    """
    item.quality += 1
    qualitySanity(item)

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
    if item.sellIn <= 5:
        item.quality += 1
    if item.sellIn <= 0:
        item.quality = 0
    qualitySanity(item)

def conjured(item):
    """
    “Conjured” items degrade in Quality twice as fast as normal items
    """
    normal(item)
    normal(item)
    qualitySanity(item)

def legendary(item):
    """
    Legendary items don't care about sellIn dates or quality
    """
    item.sellIn = 0

####################################################################################################

class GildedRose:
"""
This class handles the shop update. There is a function to add new items to the shop
and a function to update item status per cycle of time.
"""
        def __init__(self):
            """
            The list 'items' contains all the items that this shop has available for sale.
            The dictionary 'rules' contains a mapping of the items in the 'items' list
            to the rule that should be applied to it on each update cycle.
            """
            self.items = []
            self.rules = {}

            """Add the default items to the shop's item list."""
            self.addItem("+5 Dexterity Vest", 10, 20, normal)
            self.addItem("Aged Brie", 2, 0, ageWell)
            self.addItem("Elixir of the Mongoose", 5, 7, normal)
            self.addItem("Sulfuras, Hand of Ragnaros", 0, 80, legendary)
            self.addItem("Backstage passes to a TAFKAL80ETC concert", 15, 20, showPasses)
            self.addItem("Conjured Mana Cake", 3, 6, conjured)

        
        def addItem(self, name, sellIn, quality, rule = normal):
            """
            This is used to add a new item to the shop's list and set the
            rule that will govern its status change on each cycle.
            rule is a function and before a new rule is used, the function
            needs to be defined.
            """
            self.items += [Items(name, sellIn, quality)]
            self.rules[hash(self.items[len(self.items) - 1])] = rule
            
        def UpdateQuality(self):
            """
            This will be called on each game loop. It goes through the
            items list and applies the associated rule to that item.
            """
            for i in self.items:
                i.sellIn -= 1
                self.rules[hash(i)](i)

####################################################################################################
