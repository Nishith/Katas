class discount():

    def __init__(self):
        self.price = 8.0
        self.discounts = {
            1:1.0,
            2:0.95,
            3:0.90,
            4:0.80,
            5:0.75
        }
        self.prices = [0] * (len(self.discounts) + 1)


    def cost(self, basket):
        books = len(basket)
        if books == 0:
            return 0
        self.prices = [0] * (len(self.discounts) + 1)
        """
        Generate all possible sets possible with the give basket and calculate
        the cost for each. Then return the minimum cost.
        """
        for c in range(2, 6):
            """
            sets is a list of lists of the combination of books in basket
            for which the discount will be calculated
            """
            sets = [[]]
            for book in basket:
                added = False
                for i in range(0, len(sets)):
                    if book not in sets[i] and len(sets[i]) < c:
                        sets[i].append(book)
                        added = True
                        break
                if added == False:
                    sets.append([book])
                    added = True
            for i in range(0, len(sets)):
                self.prices[c] += len(sets[i]) * self.price * self.discounts[len(sets[i])]
#            print (sets)
#            print (self.prices)
        return min(self.prices[2:])

