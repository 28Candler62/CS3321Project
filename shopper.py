from person import Person

class Shopper(Person):
    def __init__(self, fName: str, lName: str, month: int, day: int, year: int, \
                add: str, phoNum: int, em: str, pw: str, id, rat, payR, shopRep):
        super().__init__(fName, lName, month, day, year, add, phoNum, em, pw)
        self.__shopperID = id
        self.__ratings = rat
        self.__payRate = payR
        self.__shopperReport = shopRep

    def getShopperID(self):
        return self.__shopperID

    def setShopperID(self, id):
        self.__shopperID = id
    
    def getRatings(self):
        return self.__ratings

    def setRatings(self, rat):
        self.__ratings = rat

    def getShopperPayRate(self):
        return self.__payRate

    def setShopperPayRate(self, payR):
        self.__creditCardNum = payR
  
    def getShopperReport(self):
        return self.__shopperReport

    def setShopperReport(self, shopRep):
        self.__shopperReport = shopRep

    def updateShopperID(self):
        print("This is the current shopper ID" + self.getShopperID() + "\n" )
        new = input("Please type their new shopper ID: ")
        self.setShopperID(new)

    def updateRatings(self):
        print("This is the current ratings" + self.getShopperID() + "\n" )
        new = input("Please type shopper + " + self.getShopperID() + "'s new ratings")
        self.setRatings(new)
    
    def updateShopperPayRate(self):
        print("This is the pay rate of shopper " + self.getShopperID() + ": " + self.getShopperPayRate() + "\n" )
        new = input("Please type the new payrate: ")
        self.setShopperPayRate(new)
        
    def updateShopperReport(self):
        print("This is the shopper report of shopper " + self.getShopperID() + ": " + self.getShopperReport() + "\n" )
        new = input("Please type the new shopper report: ")
        self.setShopperReport(new)