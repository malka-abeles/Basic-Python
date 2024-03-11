from product import Product
from computer import Computer
from keyboard import Keyboard
from mouse import Mouse
from Stock import Stock

class Order:
    """Contains the order details"""
    def __init__(self, customername):
        self.customername = customername
        self.products = []
        self.topay = 0

    def printbasket(self,stock):
        """Prints all the products in the basket"""
        [stock.stock[p].print1() for p in self.products]

    def printInvoicing(self):
        """Writes an invoice to an external file"""
        f=open("bill.txt", 'w')
        f.write(f"customer name: {self.customername} \n order details:{self.products}\n for payment:{self.topay}\nThank you for shopping with us!")
        f.close()
        f=open("bill.txt", 'r')
        for line in f:
            print(line)
