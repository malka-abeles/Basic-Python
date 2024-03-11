from product import Product


class Keyboard(Product):
    """Contains the keyboard product information"""
    def __init__(self, code, price, company, color, language,quantity):
        Product.__init__(self,code, price, company,quantity)
        self.color = color
        self.language = language

    def print1(self):
        """Prints the product details"""
        print(f"-------------\n computer code:{self.code} price:{self.price} company:{self.company} "
              f"color: {self.color} language:{self.language}")
        return ""
