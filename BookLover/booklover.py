import pandas as pd

class BookLover():
    
    def __init__(self, name, email, fav_genre, num_books=0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books=0
        self.book_list=pd.DataFrame({'book_name':[], 'book_rating':[]})
        
    def add_book(self, book_name, rating):

        if not isinstance(book_name, str):
           print("Book name needs to be a string")
           return
        if not isinstance(rating, int):
            print("Rating needs to be a integer")
            return
        else:
            if book_name in self.book_list['book_name'].values:
                print("This book has already been put into the book list!")
            else:
                new_book = pd.DataFrame({
                    'book_name': [book_name], 
                    'book_rating': [rating]
                })
            try:
                self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            except UnboundLocalError:
                pass
    def has_read(self, book_name):
        if book_name in self.book_list['book_name'].values:
            return True
        else:
            return False
    def num_books_read(self):
        return len(self.book_list)
    def fav_books(self):
        filtered = self.book_list[self.book_list['book_rating'] > 3]
        return filtered
    
    

