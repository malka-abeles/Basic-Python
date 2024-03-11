from product import Product


class Mouse(Product):
    """Contains the mouse product details"""
    def __init__(self, code, price, company, color, bluetooth,quantity):
        Product.__init__(self,code, price, company,quantity)
        self.color = color
        self.bluetooth = bluetooth

    def print1(self):
        """Prints the product details"""
        print(f"-------------\n computer code:{self.code} price:{self.price} company:{self.company} "
              f"color: {self.color} there is bluetooth:{self.bluetooth}")
        return ""
