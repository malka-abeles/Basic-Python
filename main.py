from product import Product
from computer import Computer
from keyboard import Keyboard
from mouse import Mouse
from Stock import Stock
from order import Order

"""lambda to cast to int"""
casttoint=lambda x : int(x)

stock = Stock()
print("Hello to our computer store!!!! ")
ans=input("We sell computers - Laptops, desktops, tablets, mice and keyboards Would you like to buy something?")
#The loop will run as long as the manager has not typed an off command.
#In addition, the manager also has the option of 'print stock'.
while ans!= "off":
    if(ans=='print stock'):
        stock.printstock()
    if(ans=="yes"):
        name=input("lets start! What is your name?")
        order=Order(name)
        #As long as the user wants to buy another product
        while (ans == "yes"):
            category = input("Choose a category - laptop, desktop, tablet, mouse or keyboard")
            while(category!="laptop"and category!="desktop"and category!="tablet"and category!="mouse" and category!="keyboard"):
                category=input("Choose a category - laptop, desktop, tablet, mouse or keyboard")
            stock.printstockcategory(category)
            code=input("Enter a product code")
            try:
                code=casttoint(code)
            except:
                print("You entered an invalid code!")
                continue
            if not stock.ifthereis(code):
                print("The product is not in stock")
            else:
                stock.removefromstock(code)
                order.products.append(code)
                order.topay+=casttoint(stock.stock[code].price)
            ans=input("Would you like to buy another product?")
        order.printbasket(stock)
        ans=input("Would you like to remove something from the basket?")
        if(ans=='yes'):
            code=input("Enter a product code")
            code=casttoint(code)
            stock.addtostock(code)
            order.products.remove(code)
            order.topay -= casttoint(stock.stock[code].price)
            order.printbasket(stock)
        print("-----for payment-----")
        input("Enter credit information:")
        print("The order was received successfully! Here is your invoice")
        order.printInvoicing()
    print("Hello to our computer store!!!! ")
    ans = input("We sell computers, tablets, mice and keyboards Would you like to buy something?")