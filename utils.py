from patron import Patron
from shopper import Shopper
from administrator import Administrator
from store import Store


class Utils():
    def welcomeStatement(a):
        if(isinstance(a, Patron)):
            print("Welcome, patron " + a.getUsername() + ".\n")
        if(isinstance(a, Shopper)):
            print("Welcome, shopper " + a.getFirstName() + " " + a.getLastName() + ".\n")
        if(isinstance(a, Administrator)):
            print("Welcome, administrator " + a.getFirstName() + " " + a.getLastName() + ".\n")
        if(isinstance(a, Store)):
            print("Welcome to " + a.getStoreName() + "on " + a.getStoreAddress() + ".\n")
    

    def checkValues(val, lowRange, upRange):
        
        if (val < lowRange or val > upRange):
            print("\nThe number typed is not listed in the menu. Please only type numbers listed in the menu and try again.")
            input("\n Press Enter to continue.")
            return False
        
        return True
    

    def inputIntCheck(lowRange, upRange):
        value = 0

        while True:
            try:
                value = int(input("Please Enter your desired option number: "))
                if(Utils.checkValues(value, lowRange, upRange)):
                    break

            except ValueError:
                print("The value you entered is invalid. Please only type one of the numbers of the options expressed above.\n\n")
                input("Press Enter to try again.\n")

        return value