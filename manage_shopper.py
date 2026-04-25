class Shopper:
    def __init__(self, db):
        self.db = db
        
    def addinfo(self, fname, lname):
        self.db.executemany("INSERT INTO shopper(ShopperFirstName, ShopperLastName) VALUES(?, ?)", [(fname, lname)])