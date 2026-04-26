class Shopper:
    def __init__(self, db):
        self.db = db
        
    def addinfo(self, fname, lname):
        self.db.execute("INSERT INTO shopper(ShopperFirstName, ShopperLastName) VALUES(?, ?)", ((fname, lname),))
        
    def get_id(self, lname):
        res = self.db.execute(
        """
        SELECT ShopperID
        FROM shopper
        WHERE ShopperLastName == ?
        """,
        (lname,)
        )
        return res.fetchone()
        
    def shop(self):
        res= self.db.execute('SELECT StoreID, StoreName FROM store')
        print('Store ID \t Store Name')
        [print(f'{x[0]}\t\t{x[1]}') for x in res.fetchall()]
        store = int(input('Select Store ID: '))
        
        
        
"""
CREATE TABLE IF NOT EXISTS shopper (
	ShopperID			INTEGER PRIMARY KEY AUTOINCREMENT,
	ShopperFirstName	Char(35)			NOT NULL,
	ShopperLastName		Char(35)			NOT NULL,
    CONSTRAINT 			ShopperName_UC		UNIQUE (ShopperFirstName, ShopperLastName)
	);
	
"""