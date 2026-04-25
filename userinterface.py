from patron import Patron
from shopper import Shopper
from administrator import Administrator
    
class UI():

    # Developer Note: Not sure if this is unnecessary. Please let me know if this is useless!

    pHolder = Patron("", "", 0, 0, 0, "", 0, "", "", 0, "", "")
    sHolder = Shopper("", "", 0, 0, 0, "", 0, "", "", 0, "", 0, "")
    aHolder = Administrator("", "", 0, 0, 0, "", 0, "", "", 0, 0)

    # Developer Test Patron Object. Please remove once database is sorted out.
    testcust = Patron("Greg", "Mercader", 6, 24, 2005, "5100 San Felipe St. 332E, Houston, TX", 713-552-1000, "gregisme18@gmail.com", "nonono", 115, "gregm18", "1110222033304440")

    def logOut():
        print("Are you sure you would like to log out?\n" \
            "1. Yes, log me out.\n" \
            "2. No, return to previous screen\n")
        n = UI.inputIntCheck(1,2)
        if n == 1:
            return True

    def welcomeStatement(a):
        if(isinstance(a, Patron)):
            print("Welcome, patron " + a.getUsername() + ".\n")
        if(isinstance(a, Shopper)):
            print("Welcome, shopper " + a.getFirstName() + " " + a.getLastName() + ".\n")
        if(isinstance(a, Administrator)):
            print("Welcome, administrator " + a.getFirstName() + " " + a.getLastName() + ".\n")
    

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
                if(UI.checkValues(value, lowRange, upRange)):
                    break

            except ValueError:
                print("The value you entered is invalid. Please only type one of the numbers of the options expressed above.\n\n")
                input("Press Enter to try again.\n")

        return value
    

    def introScreen():
        while(True):
            val = 0
            print(
                "\n" \
                "1. Log in\n" \
                "2. Create Account\n" \
                "3. Exit Program"
                "\n")
        
            val = UI.inputIntCheck(1, 3)
            if val == 1:
                UI.logInScreen()
            if val == 2:
                UI.createAccountScreen()
            if val == 3:
                break


    def logInScreen():
        while (True):
            print("\nPlease enter credentials\n")
            em = input("Email: ")
            pw = input("Password: ")

            # This function uses the developer patron object, testcust.
            # Please fix this once the database is sorted out.

            # If Username and Password are in the Database,
            # continue to their designated patron, shopper, or admin screens
            # else, prompt to try again or exit the program
            if(UI.testcust.getPassword() == pw and UI.testcust.getEmail() == em):
                if (isinstance(UI.testcust, Patron)):
                    UI.pHolder = UI.testcust
                    UI.patronMainScreen()
                if (isinstance(UI.testcust, Shopper)):
                    UI.sHolder = UI.testcust
                    UI.shopperMainScreen()
                if (isinstance(UI.testcust, Administrator)):
                    UI.aHolder = UI.testcust
                    UI.adminMainScreen()
                break

            else:
                print(
                    "Credentials not found. Would you like to try again or return to the Main Menu?\n"  \
                    "1. Try again\n" \
                    "2. Main Menu\n" \
                    "\n")
                val = UI.inputIntCheck(1,2)
                if val == 2:
                    break
                                

    def createAccountScreen():
        print("\nWelcome to the Create Account Screen\n")


    def patronMainScreen():
        while(True):
            
            UI.welcomeStatement(UI.pHolder)
            
            print(
                "1. Start Shopping\n" \
                "2. View Shopping Cart\n" \
                "3. Settings\n" \
                "4. Log Out\n\n")
            
            val = UI.inputIntCheck(1,4)
            if val == 1:
                UI.listOfStoresScreen()
            if val == 2:
                UI.shoppingCartScreen()
            if val == 3:
                UI.patronSettingsScreen()
            if val == 4:
                if UI.logOut():
                    break
                

    
    def listOfStoresScreen():
        print("LOS Screen\n")
        input("Press enter to continue")

    def shoppingCartScreen():
        print("shop cart screen\n")
        input("Press enter to continue")
    


    def patronSettingsScreen():
        print("patron settings screen\n")
        input("Press enter to continue.")
        

    def shopperMainScreen():

        UI.welcomeStatement(UI.sHolder)
        input("Press Enter to Continue")


    def adminMainScreen():

        UI. welcomeStatement(UI.aHolder)
        input("Press enter to continue")

