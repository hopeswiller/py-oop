class Book:

    __book_list = None

    # Class Attributes are shared by all instances (use CAPS)
    BOOK_TYPES = ("HARDCOVER", "EBOOK", "PAPERBACK")

    def __init__(self, title, author, price, book_type):
        self.title = title
        self.author = author
        self.price = price

        if not book_type in Book.BOOK_TYPES:
            raise ValueError(f"Book type is not a valid book type")
        else:
            self.book_type = book_type

        # use can use double underscores to hide attributes outside of the class, private
        self.__secret = "secret to the book"

    
    def __str__(self):
        return f"{self.title} by {self.author}. Cost: ${self.get_price()}"


    # instance methods
    def get_price(self):
        # since _discount isnt known when the object is initialized, we check if it exists before using it
        if hasattr(self, '_discount'):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def set_discount(self, amount):
        # underscore infront of discount only means the variable's access is private to the class
        self._discount = amount

    # static methods mostly used for singleton objects for the class
    def get_book_list():
        pass

    # class methods
    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES


    # equality and comparison methods
    def __eq__(self, other):
        """ Python doesn't compare attributes in the objects but rather compares
            different instances of the objects and realises that both have different memory locations.
            hence bk1 == bk1 : False
        """
        if not isinstance(other, Book):
            raise ValueError("Is not type of Book")
        return (self.title == other.title and self.author == other.author and self.price == other.price)


    def __ge__(self):
        pass


    # treats objects as functions -- able to update the values of the objects
    def __call__(self,title, author, price, book_type):
        self.title = title
        self.author = author
        self.price = price

        if not book_type in Book.BOOK_TYPES:
            raise ValueError(f"Book type is not a valid book type")
        else:
            self.book_type = book_type


bk1 = Book("Old Man and the sea", "David Adams", 200.00, "EBOOK")
bk2 = Book("Peacer Trivers", "Joe Marino", 250.00,"PAPERBACK") 
bk3 = Book("Old Man and the sea", "David Adams", 200.00, "EBOOK")

print(bk1)

bk1.set_discount(0.25)

print("AFTER DISCOUNT: " + str(bk1))

# print(bk1.__secret)
# print(bk1._Book__secret)

print(f"Book Types : {Book.get_book_types()}")


print(bk1 == bk3)
print(bk1 == bk2)


# callable objects
bk3("Rock City","Frank Castle", 45.00, "PAPERBACK")
print(bk3)