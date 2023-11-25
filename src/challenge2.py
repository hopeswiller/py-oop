# Class that represents information about Stocks and  bonds
# use inheritance and abstract classes


from abc import ABC, abstractmethod

class Asset(ABC):

    def __init__(self, price):
        self.price = price   
    
    @abstractmethod
    def get_description(self):
        pass


class Stock(Asset):

    def __init__(self, ticker, price, company):
        super().__init__(price)
        self.ticker = ticker
        self.company = company

    
    def get_description(self):
        return f"{self.ticker}: {self.company} -- ${self.price}"


class Bond(Asset):
    
    def __init__(self,price, description, duration, yieldpercentage):
        super().__init__(price)
        self.description = description
        self.duration = duration
        self.yieldpercentage = yieldpercentage

    def get_description(self):
        return f"{self.description}: {self.duration}'yr' : ${self.price} : {self.yieldpercentage}%"


# TEST CODE

try:
    ast = Asset(100.00)
except:
    print("Can't instantiate Asset")

msft = Stock("MSFT", 342.0, "Microsoft Corp")
goog = Stock("GOOG", 135.0, "Google Inc")
meta = Stock("META", 275.0, "Meta Platforms Inc")
amzn = Stock("AMZN", 135.0, "Amazon Inc")


b5yr = Bond(98.65, "5 Year US Treasury",5, 4.43)
b2yr = Bond(135.0, "2 Year US Treasury",2, 4.98)


print(msft.get_description())
print(goog.get_description())
print(meta.get_description())
print(amzn.get_description())

print(b5yr.get_description())
print(b2yr.get_description())