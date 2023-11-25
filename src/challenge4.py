# Class that represents information about Stocks and  bonds
# implement a dataclass


from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Asset(ABC):

    price: float 

    @abstractmethod
    def __lt__(self, other):
        pass


@dataclass
class Stock(Asset):

    ticker: str
    company: str

    def __lt__(self, other):
        return self.price < other.price


@dataclass
class Bond(Asset):

    description: str
    duration: int
    yieldpercentage: float

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
    Bond(98.65, "5 Year US Treasury",5, 7.43),
    Bond(135.0, "2 Year US Treasury",2, 4.98)
]

try:
    ast = Asset(100.00)
except:
    print("Can't instantiate Asset")

# sort uses the less than magic methods
stocks.sort()
bonds.sort()

for stock in stocks:
    print(stock)

print("-------------------------------------------`")

for bond in bonds:
    print(bond)