# Class that represents information about Stocks

class Stock:

    def __init__(self, ticker, price, company):
        self.ticker = ticker
        self.price = price
        self.company = company

    
    def get_description(self):
        return f"{self.ticker}: {self.company} -- ${self.price}"


# initialize

msft = Stock("MSFT", 342.0, "Microsoft Corp")
goog = Stock("GOOG", 135.0, "Google Inc")
meta = Stock("META", 275.0, "Meta Platforms Inc")
amzn = Stock("AMZN", 135.0, "Amazon Inc")


print(msft.get_description())
print(goog.get_description())
print(meta.get_description())
print(amzn.get_description())