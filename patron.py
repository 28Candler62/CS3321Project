from person import Person

class Patron(Person):
    def __init__(self, fName: str, lName: str, month: int, day: int, year: int, \
                 add: str, phoNum: int, em: str, pw: str, id: int, uname: str, cardNum):
        super().__init__(fName, lName, month, day, year, add, phoNum, em, pw)
        self.__patronID = id
        self.__username = uname
        self.__creditCardNum = cardNum

    # Getters and Setters

    def getPatronID(self):
        return self.__patronID

    def setPatronID(self, id):
        self.__patronID = id
    
    def getUsername(self):
        return self.__username

    def setUsername(self, uname):
        self.__username = uname

    def getCreditCardNum(self):
        return self.__creditCardNum

    def setCreditCardNum(self, cardNum):
        self.__creditCardNum = cardNum

    # Update functions

    def updatePatronID(self):
        print("This is your current patron ID" + self.__patronID + "\n" )
        new = input("Please type your new patron ID: ")
        self.setPatronID(new)

    def updateUsername(self):
        print("This is your current username" + self.__username + "\n" )
        new = input("Please type your new username: ")
        self.setUsername(new)
    
    def updateCreditCardNum(self):
        print("This is your current credit card number" + self.__creditCardNum + "\n" )
        new = input("Please type your new credit card number: ")
        self.setCreditCardNum(new)