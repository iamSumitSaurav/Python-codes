class book:
    def __init__(self, title, author, publisher, price, Royalty):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.price = price
        self.Royalty = Royalty

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_publisher(self):
        return self.publisher

    def get_price(self):
        return self.price

    def get_Royalty(self):
        return self.Royalty

    def set_title(self, new_title):
        self.title = new_title

    def set_author(self, new_author):
        self.author = new_author

    def set_publisher(self, new_publisher):
        self.publisher = new_publisher

    def set_price(self, new_price):
        self.publisher = new_price

    def set_Royalty(self, new_Royalty):
        self.Royalty = new_Royalty

    def royalty(self):
        no_of_copies = int(input("Enter number of copies"))
        
        if no_of_copies in range(1, 501):
            royalty_amt = 0.1*self.get_price()*no_of_copies

        elif no_of_copies in range(501, 1501):
            remaining = no_of_copies - 500
            royalty_amt = (0.1*500 + 0.125*remaining)*self.get_price()

        elif no_of_copies > 1500:
            remaining = no_of_copies - 1500
            royalty_amt = (0.1*500 + 0.125*1000 + 0.15*remaining)*self.get_price()

        print('Royalty amount applicable =', royalty_amt)


class ebook(book):
    GST = 0.12
    
    def __init__(self, name, author, publisher, price, royalty, ebook_format):
        super().__init__(name, author, publisher, price, royalty)
        self.ebook_format = ebook_format
        
    def get_format(self):
        return self.ebook_format

    def set_format(self, ebk_format):
        self.ebook_format = ebk_format

    def royalty(self):
        no_of_copies = int(input("Enter number of copies"))
        
        if no_of_copies in range(1, 501):
            royalty_amt = 0.1*self.get_price()*no_of_copies

        elif no_of_copies in range(501, 1501):
            remaining = no_of_copies - 500
            royalty_amt = (0.1*500 + 0.125*remaining)*self.get_price()

        elif no_of_copies > 1500:
            remaining = no_of_copies - 1500
            royalty_amt = (0.1*500 + 0.125*1000 + 0.15*remaining)*self.get_price()

        new_royalty = royalty_amt - ebook.GST * self.get_price()
        print('Royalty amount applicable =', new_royalty)
        







        
        
