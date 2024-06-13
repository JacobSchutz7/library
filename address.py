class Address:
	def __init__(self, street_number, street_name, city, post_code):
		self.street_number = street_number
		self.street_name = street_name
		self.city = city
		self.post_code = post_code
	
	def full_address(self):
		return f"{self.street_number} {self.street_name} {self.city} {self.post_code}"
	
	def get_street_number(self):
		return self.street_number
    
	def get_street_name(self):
		return self.street_name
	
	def get_city(self):
		return self.city
	
	def get_post_code(self):
		return self.post_code