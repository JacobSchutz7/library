import random

class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.bookID = random.randint(100000, 999999)

    def get_title(self):
        return self.title
    
    def set_title(self, title):
        self.title = title

    def get_author(self):
        return self.author
    
    def set_author(self, author):
        self.author = author
    
    def get_ISBN(self):
        return self.ISBN
    
    def get_bookID(self):
        return self.bookID