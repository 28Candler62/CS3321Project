class Shopper:
    def __init__(self, db):
        self.db = db
        
    def addinfo(self, fname, lname):
        self.db.executemany("INSERT INTO shopper(ShopperFirstName, ShopperLastName) VALUES(?, ?)", [(fname, lname)])
        
    def shop(self):
        res= self.db.execute('SELECT StoreID, StoreName FROM store')
        print('Store ID \t Store Name')
        [print(f'{x[0]}\t\t{x[1]}') for x in res.fetchall()]
        store = int(input('Select Store ID: '))