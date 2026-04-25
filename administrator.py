from person import Person

class Administrator(Person):
    def __init__(self, fName: str, lName: str, month: int, day: int, year: int, \
                add: str, phoNum: int, em: str, pw: str, id, pr):
        super().__init__(fName, lName, month, day, year, add, phoNum, em, pw)
        self.__employeeID = id
        self.__adminPayRate = id

    def getEmployeeID(self):
        return self.__employeeID
    
    def setEmployeeID(self, id):
        self.__employeeID = id

    def getAdminPayRate(self):
        return self.__adminPayRate
    
    def setAdminPayRate(self, pr):
        self.__adminPayRate = pr

    def updateEmployeeID(self):
        print("This is the current employee ID" + self.getEmployeeID() + "\n" )
        new = input("Please type their new employee ID: ")
        self.setEmployeeID(new)
        
    def updateAdminPayRate(self):
        print("This is the current administrator pay rate" + self.getAdminPayRate() + "\n" )
        new = input("Please type their new employee ID: ")
        self.setAdminPayRate(new)
        