

class Library:
    def __init__(self):
        self.books=['fault in our stars','looking for alaska']
        self.no_of_books=45

    def add_book(self,new_book):
        self.books.append(new_book)
        
    def remove_book(self,rem_book):
        self.books.remove(rem_book)

a=Library()
print(a.books)
print("no of books are=", a.no_of_books)
a.add_book('harry potter')
print(a.books)
a.remove_book('fault in our stars')
print(a.books)