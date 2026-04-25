

class Grocery():
    def __init__(self, name, price, desc, num):
        self.__itemName = name
        self.__itemPrice = price
        self.__description = desc
        self.__stock = num

    def getItemName(self):
        return self.__itemName

    def setItemName(self, new):
        self.__itemName = new

    def getItemPrice(self):
        return self.__itemPrice

    def setItemPrice(self, new):
        self.__itemPrice = new

    def getItemDescription(self):
        return self.__description

    def setItemDescription(self, new):
        self.__description = new

    def getItemStock(self):
        return self.__stock

    def setItemStock(self, new):
        self.__stock = new

    def updateItemName(self):
        print("This is the current item name: " + self.getItemName() + "\n" )
        new = input("Please type its new name: ")
        self.setItemName(new)
        
    def updateItemPrice(self):
        print("This is the current item price: " + self.getItemPrice() + "\n" )
        new = input("Please type its new price: ")
        self.setItemPrice(new)

    def updateItemDescription(self):
        print("This is the current item description: " + self.getItemDescription() + "\n" )
        print("Please enter its new descripton: ")
        print("Enter text (type END on a new line to finish):")

        lines = []
        while True:
            line = input()
            if line == "END":
                break
            lines.append(line)

        text = "\n".join(lines)

        print("You entered: \n" )
        print(text + "\n")
        print("Are you satisfied with your description? \
              Or would you like to try again?\n")
        
        #Incomplete, trying to make inputIntCheck and checkValues 
        #accessible to other classes so this class can use it.

        self.setItemDescription(text)
        
    def updateItemStock(self):
        print("This is the current item stock: " + self.getItemStock() + "\n" )
        new = input("Please type its new amount of stock: ")
        self.setItemStock(new)