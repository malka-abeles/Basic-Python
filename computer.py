from product import Product


class Computer(Product):
    """Contains the details of the computer product"""
    def __init__(self, code, price, company, type, sizeofscreen,quantity):
        Product.__init__(self,code, price, company,quantity)
        self.type = type
        self.sizeofscreen = sizeofscreen

    def print1(self):
        """Prints the product details"""
        print(f"-------------\n computer {self.type} code:{self.code} price:{self.price} company:{self.company} size "
              f"of screen: {self.sizeofscreen} inch")
        return ""

