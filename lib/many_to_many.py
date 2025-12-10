class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not value.strip():
            raise Exception("title must be a non-empty string")
        self._title = value

    # returns all contracts for this book
    def contracts(self):
        return [c for c in Contract.all if c.book is self]

    # returns all authors for this book via Contract intermediary
    def authors(self):
        return [c.author for c in self.contracts()]


class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise Exception("name must be a non-empty string")
        self._name = value

    # return all related contracts
    def contracts(self):
        return [c for c in Contract.all if c.author is self]

    # return all books via contract
    def books(self):
        return [c.book for c in self.contracts()]

    # create a new contract
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    # total royalties from all contracts
    def total_royalties(self):
        return sum(c.royalties for c in self.contracts())


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("author must be an Author instance")
        self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("book must be a Book instance")
        self._book = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str) or not value.strip():
            raise Exception("date must be a non-empty string")
        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("royalties must be an integer")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date):
        return [c for c in cls.all if c.date == date]
