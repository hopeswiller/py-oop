# Class that represents information about Stocks and  bonds
# add methods for comparison and equality


from abc import ABC, abstractmethod

class Asset(ABC):

    def __init__(self, price):
        self.price = price   

    @abstractmethod
    def __str__(self):
        pass


class Stock(Asset):

    def __init__(self, ticker, price, company):
        super().__init__(price)
        self.ticker = ticker
        self.company = company

    def __str__(self):
        return f"{self.ticker}: {self.company} -- ${self.price}"

    def __lt__(self, other):
        return self.price < other.price


class Bond(Asset):
    
    def __init__(self,price, description, duration, yieldpercentage):
        super().__init__(price)
        self.description = description
        self.duration = duration
        self.yieldpercentage = yieldpercentage

    def __str__(self):
        return f"{self.description}: {self.duration}'yr' : ${self.price} : {self.yieldpercentage}%"

    def __lt__(self, other):
        return self.yieldpercentage < other.yieldpercentage


# TEST CODE

stocks = [
    Stock("MSFT", 342.0, "Microsoft Corp"),
    Stock("GOOG", 135.0, "Google Inc"),
    Stock("META", 275.0, "Meta Platforms Inc"),
    Stock("AMZN", 135.0, "Amazon Inc")
]

bonds = [
    Bond(98.65, "5 Year US Treasury",5, 4.43),
    Bond(135.0, "2 Year US Treasury",2, 4.98)
]

# sort uses the less than magic methods
stocks.sort()
bonds.sort()

for stock in stocks:
    print(stock)

print("-------------------------------------------`")

for bond in bonds:
    print(bond)