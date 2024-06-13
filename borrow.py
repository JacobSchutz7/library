import random

class Borrow:
	def __init__(self, staff, member, bookID):
		self.staff = staff
		self.member = member
		self.transaction_ID = random.randint(10000000, 99999999)
