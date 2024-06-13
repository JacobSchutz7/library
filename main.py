from staff import Staff
from member import Member
from address import Address
from book import Book
from borrow import Borrow

s1 = Staff("Jim", 1234)
a1 = Address(1, "Street Name", "St Agnes", 5097)
m1 = Member("James", 0000, a1)
b1 = Book("Republic", "Plato", 14850239)

bor1 = Borrow(s1, m1, b1.get_bookID())