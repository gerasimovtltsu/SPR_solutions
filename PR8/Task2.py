class Book:
    def __init__(self, title, author, published_year):
        self.title = title
        self.author = author
        self.published_year = published_year
    
    def display_book(self):
        return f"{self.title} {self.author} {self.published_year}"

my_book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
print(my_book.display_book())