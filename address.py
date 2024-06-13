class Address:
	def __init__(self, street_number, street_name, city, post_code):
		self.street_number = street_number
		self.street_name = street_name
		self.city = city
		self.post_code = post_code
	
	def full_address(self):
	    return f"{self.street_number} + {self.street_name} + {self.city} + {self.post_code}"