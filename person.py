

class Person:

    def __init__(self, fName: str, lName: str, month: int, day: int, year: int, \
                add: str, phoNum: int, em: str, pw: str):
        self.__firstName = fName
        self.__lastName = lName
        self.__month = month
        self.__day = day
        self.__year = year
        self.__address = add
        self.__phoneNumber = phoNum
        self.__email = em
        self.__password = pw


    # Getters and Setters
    
    def getFirstName(self):
        return self.__firstName

    def setFirstName(self, new):
        self.__firstName = new
    
    def getLastName(self):
        return self.__lastName

    def setLastName(self, new):
        self.__lastName = new

    def getMonth(self):
        return self.__month

    def setMonth(self, new):
        self.__month = new

    def getDay(self):
        return self.__day

    def setDay(self, new):
        self.__day = new

    def getYear(self):
        return self.__year

    def setYear(self, new):
        self.__year = new

    def getAddress(self):
        return self.__address

    def setAddress(self, new):
        self.__address = new

    def getPhoneNumber(self):
        return self.__phoneNumber

    def setPhoneNumber(self, new):
        self.__phoneNumber = new

    def getEmail(self):
        return self.__email

    def setEmail(self, new):
        self.__email = new

    def getPassword(self):
        return self.__password

    def setPassword(self, new):
        self.__password = new

    