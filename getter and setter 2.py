class books:
    def __init__(self, b1 = 'history', b1_c = 500, b2 = 'maths', b2_c = 645):
        self.book1 = b1
        self.price_book1 = b1_c
        self.book2 = b2
        self.price_book2 = b2_c

    def get_book(self):
        return {'book1': self.book1, 'price1': self.price_book1, 'book2': self.book2, 'price2': self.price_book2}

    def set_book(self, a, b, c, d):
        self.book1 = a
        self.price_book1 = b
        self.book2 = c
        self.price_book2 = d

    bookvar = property(get_book, set_book)
    

    
