import pandas as pd
import unittest
from booklover import BookLover

test = BookLover("Olivia", "ocbyram@gmail.com", "romance")
class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        test.add_book(book_name = "Frankenstein", rating =1)
        test1 = "Frankenstein" in test.book_list['book_name'].values
        message = "Book is not in in book list"
        self.assertTrue(test1, message)

    def test_2_add_book(self):
        test.add_book(book_name = "Frankenstein", rating =2)
        testing = test.book_list[test.book_list["book_name"] == "Frankenstein"]
        test1 = len(testing) == 1
        message = "Book is in book_list more than once!"
        self.assertTrue(test1, message)
                
    def test_3_has_read(self): 
        test3 = test.has_read("Frankenstein")
        message = "This book has not been read!"
        self.assertTrue(test3, message)
        
    def test_4_has_read(self): 
        test4 = test.has_read("Pride and Prejudice")
        message = "This book has been read!"
        self.assertFalse(test4, message)
        
    def test_5_num_books_read(self):
        # There is already a book added from the first test method (Frankenstein). So it's
        # these four books plus that one for a total of 5 books expected in the list
        test.add_book(book_name = "Pride and Prejudice", rating =4)
        test.add_book(book_name = "Harry Potter", rating =5)
        test.add_book(book_name = "Percy Jackson", rating =5)
        test.add_book(book_name = "Wuthering Heights", rating =1)
        test5 = test.num_books_read() == 5
        message = "There is a different number of books in this list than you expected!"
        self.assertTrue(test5, message)

    def test_6_fav_books(self):
        test.add_book(book_name = "Emma", rating =2)
        test.add_book(book_name = "Oh the Places You'll Go", rating =5)
        test.add_book(book_name = "War and Peace", rating =1)
        test6 = test.fav_books()
        testing6 = 1 not in test6['book_rating'].values and 2 not in test6['book_rating'].values and 3 not in test6['book_rating'].values
        message = "There is a book with a rating 3 or below!"
        self.assertTrue(testing6, message)
    
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)