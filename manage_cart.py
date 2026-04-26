class Cart:
    def __init__(self, db):
        self.db = db
        
        
"""
CREATE TABLE IF NOT EXISTS shoppingcart (
	CartItemID			INTEGER PRIMARY KEY AUTOINCREMENT,
	ShoppingListItem	Integer				NOT NULL,
    Shopper				Integer				NOT NULL,
    CONSTRAINT 		    ShoppingListItem_FK 	FOREIGN KEY (ShoppingListItem)
							REFERENCES  shoppinglist (ListItemID)
								ON UPDATE CASCADE,
	CONSTRAINT 		    Shopper_FK 			FOREIGN KEY (Shopper)
							REFERENCES  shopper (ShopperID)
								ON UPDATE CASCADE,
	CONSTRAINT 			ShoppingCart_UC		UNIQUE (ShoppingListItem, Shopper)
	);


"""