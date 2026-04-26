class Cart:
    def __init__(self, db):
        self.db = db
    
    def add_item(self, sl_item_id:int, shopper_id:int):
        
        res = self.db.execute(
            """
            SELECT *
            FROM shoppingcart
            WHERE ShoppingListItem == ?
            AND Shopper == ?
            """,
            (sl_item_id, shopper_id)
        )
        
        existing_item = res.fetchone()
        
        if existing_item:
            return
        else:        
            self.db.execute(
                """
                INSERT INTO shoppingcart(ShoppingListItem, Shopper)
                VALUES(?, ?)
                """,
                (sl_item_id, shopper_id)
            )
        
        return True
        
    def view_cart(self, shopper_id:int):
        """
        View a shopper's cart: .
        """
        
        res = self.db.execute(
            """
            SELECT 
                sc.CartItemID,
                sl.ListItemID,
                p.PatronFirstName,
                p.PatronLastName
            FROM shoppingcart sc
            JOIN shoppinglist sl ON sc.ShoppingListItem = sl.ListItemID
            JOIN patron p ON sl.Patron = p.PatronID
            WHERE sc.Shopper == ?
            ORDER BY p.PatronLastName
            """,
            (shopper_id,)
        )

        return res.fetchall()
        
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