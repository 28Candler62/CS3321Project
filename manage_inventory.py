class Inventory:
    def __init__(self, db):
        self.db = db
        
    def get_stores(self):
        res = self.db.execute(
        """
        SELECT s.StoreID, s.StoreName
        FROM store s
        WHERE s.StoreID IN (
            SELECT ItemStore
            FROM inventory
            )
        """
        )
        return res.fetchall()
        
    def get_store_inventory(self, store_id:int):
        res = self.db.execute(
        """
        SELECT ItemID, ItemName, ItemDescription, Quantity, Price
        FROM inventory
        WHERE ItemStore == ?
        """,
        (store_id,)
        )
        return res.fetchall()
        
    def add_item(self, name:str, desc:str, store:int, qty:int, price:float):
        self.db.execute("INSERT INTO inventory(ItemName, ItemDescription, ItemStore, Quantity, Price) VALUES(?, ?, ?, ?, ?)", (name, desc, store, qty, price))
    
    

"""
CREATE TABLE IF NOT EXISTS inventory (
	ItemID				INTEGER PRIMARY KEY AUTOINCREMENT,
	ItemName			Char(35)			NOT NULL,
    ItemDescription		Char(70)			NOT NULL,
    ItemStore			Integer				NOT NULL,
    Quantity  		    Integer 	       	NOT NULL,
	Price  			    Decimal(9,2)     	NOT NULL,
    CONSTRAINT 		    ItemStore_FK 		FOREIGN KEY (ItemStore)
							REFERENCES  store (StoreID)
								ON UPDATE CASCADE,
	CONSTRAINT 			Inventory_UC		UNIQUE (ItemName, ItemDescription, ItemStore)
	);
"""