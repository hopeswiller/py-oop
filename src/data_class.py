# Data classes exist in python from v3.7
# aim is to automate the creation of classes and managing class that exist just to hold data


from dataclasses import dataclass, field

# frozen parameter makes the class immutable
@dataclass(frozen=True)
class ImmutableClass:
    title: str =  field(default="Immutable Title")

    def update(self, val):
        self.title = val


@dataclass
class Book:

    # looks more like class attributes instead of instance attributes but 
    # @dataclass will implicitly rewrite this with the init function 
    title: str
    author: str
    price: float

    # gets called after builtin __init__ method. any logic needed after initialization can be added here
    def __post_init__(self):
        self.info = f"{self.title} by {self.author}"
        return self.info

    # dataclass automatically implements __repr__ and __eq__ methods

    def bookinfo(self):
        return self.info 

bk1 = Book("Old Man and the sea", "David Adams", 200.00)
bk2 = Book("Peacer Trivers", "Joe Marino", 250.00) 
bk3 = Book("Peacer Trivers", "Joe Marino", 250.00) 
im1 = ImmutableClass("Immutable Title At Creation") 

print(bk1)


print(bk3 == bk2)

print(bk1.bookinfo())

print(im1)
try:
    im1.update("Change Test")
except:
    print(f"Error occured. Cannot change frozen param ")