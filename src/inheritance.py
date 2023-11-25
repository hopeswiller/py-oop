class Publication:

    def __init__(self, title, price):
        self.title = title
        self.price = price


class Periodical(Publication):

    def __init__(self, title, price, period, publisher):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher



class Book(Publication):
    
    def __init__(self, title, price, author, pages):
        super().__init__(title, price)  # initializes the super class
        self.author = author
        self.pages = pages


class Magazine(Periodical):

    def __init__(self, title, price, period, publisher):
        super().__init__(title, price,period,publisher)


class Newspaper(Publication):

    def __init__(self, title, price, period, publisher):
        super().__init__(title, price,period,publisher)


bk1 = Book("Old Man and the sea", 200.00, "David Adams", 500)
mg1 = Magazine("Peacer Trivers", 55.00, "2023", "PAPERBACK") 


print(mg1.publisher)