from product import Product
from computer import Computer
from keyboard import Keyboard
from mouse import Mouse



class Stock:
    """contains a list of the products in the store"""
    def __init__(self):
        self.stock = {111:Computer(111, 2222, "dell", "laptop", 16.1, 5),
                      222:Computer(222, 3000, "dell", "laptop", 14.1, 5),
                      333:Computer(333, 4500, "hp", "laptop", 14.3, 10),
                      444:Computer(444, 7000, "dell", "desktop", 16.1, 8),
                      555:Computer(555, 8500, "lenovo", "desktop", 16.2, 8),
                      666:Computer(666, 1000, "apple", "tablet", 10.7, 8),
                      777:Computer(777, 2500, "apple", "tablet", 12.1, 8),
                      123:Mouse(123,50,'lenovo','gray','yes',15),
                      456:Mouse(456,100,'dell','gray','yes',8),
                      789:Mouse(789,70,'hp','white','no',5),
                      321:Keyboard(321,50,'lenovo','black','Hebrew',15),
                      654:Keyboard(654,80,'dell','gray','Hebrew and English',7),
                      987:Keyboard(987,120,'apple','pink','English',10)}

    def addproducttostock(self,product):
        """Adding a new product to stock"""
        self.stock.update([(product.code,product)])

    def removefromstock(self,code):
        """Deducting an item from inventory"""
        self.stock[code].quantity-=1

    def addtostock(self,code):
        """Adding an item to inventory"""
        self.stock[code].quantity+=1

    def ifthereis(self,code):
        """Checking whether the product is available in stock"""
        try:
            return self.stock.get(int(code)).quantity>0
        except:
            print("This product does not exist")

    def printstock(self):
        """Printing the products in stock"""
        [print(f"{p.print1()} quantity: {p.quantity}") for p in self.stock.values()]

    def printstockcategory(self,category):
        """Printing products by category"""
        if category== 'laptop' or category== 'desktop' or category== 'tablet':
            [p.print1() for p in self.stock.values() if (isinstance(p,Computer) and p.type==category)]
        if category == 'mouse':
            [p.print1() for p in self.stock.values() if (isinstance(p, Mouse))]
        if category == 'keyboard':
            [p.print1() for p in self.stock.values() if (isinstance(p, Keyboard))]
