

class Store():
    def __init__(self, name, add, groc):
        self.__storeName = name
        self.__storeAddress = add
        self.__groceries = groc

    # Getters and Setters 
    def getStoreName(self):
        return self.__storeName
    
    def setStoreName(self, new):
        self.__storeName = new

    def getStoreAddress(self):
        return self.__storeAddress

    def setStoreAddress(self, new):
        self.__storeAddress = new

    def getStoreGroceries(self):
        return self.__groceries

    def setStoreGroceries(self, new):
        self.__groceries = new

    # Update Functions

    def updateStoreName(self):
        print("not ready")
    
    def updateStoreAddress(self):
        print("not ready")

    def updateStoreGroceries(self):
        print("not ready")