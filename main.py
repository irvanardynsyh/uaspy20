from core.baseapp import BaseApp
from core.search_helper import SearchHelper
from data_model.author import Author
from data_model.book import Book
from data_model.publication import Publication

class MainApp(BaseApp):
    def _init_(self):
        self.books = []
        self.InputBook = []
        self.ViewBook = []
        BaseApp._init_(self)


class ViewBook(Book):
    def _init_(self):
        vBook = ViewBook (self, books)
        vBook.list_book()

    def list(self):
        while True:
            self.clear()
            print("=================================================================================")
            print("| ID |              TITLE               |     AUTHOR      |   PRICE    | COPIES |")
            print("=================================================================================")
            if len(self.books) == 0:
                print("|                                  Data Empty                                   |")

            idx = 0
            for book in self.books:
                idx+=1
                print("| {}  {}".format(idx, book.toRow()))
            print("=================================================================================")

            key = input("Detail [ID], [B]ack to menu: ")
            if key.lower() == "b":
                break
            elif key.isnumeric():
                self.detail(int(key.lower()) - 1)
                
    @property
    def list_book(self):
        return self.list_book
    def add_book(self):
        return self.add_book()
    def search_book(self):
        return self.search_book()