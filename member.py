from user import User

class Member(User):
	def __init__(self, name, id, address):
		self.name = name
		self.id = id
		self.address = address