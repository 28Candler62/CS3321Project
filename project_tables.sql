/*
Tables:
	patron
    shopper
    store
    shoppingList
    shoppingCart
    inventory
*/

CREATE TABLE IF NOT EXISTS patron (
	PatronID			INTEGER PRIMARY KEY AUTOINCREMENT,
	PatronFirstName	Char(35)			NOT NULL,
	PatronLastName	Char(35)			NOT NULL,
    CONSTRAINT 			PatronName_UC		UNIQUE (PatronFirstName, PatronLastName)
    );
    
CREATE TABLE IF NOT EXISTS shopper (
	ShopperID			INTEGER PRIMARY KEY AUTOINCREMENT,
	ShopperFirstName	Char(35)			NOT NULL,
	ShopperLastName		Char(35)			NOT NULL,
    CONSTRAINT 			ShopperName_UC		UNIQUE (ShopperFirstName, ShopperLastName)
	);
    
CREATE TABLE IF NOT EXISTS store (
	StoreID				INTEGER PRIMARY KEY AUTOINCREMENT,
	StoreName			Char(35)			NOT NULL,
    CONSTRAINT 			StoreName_UC		UNIQUE (StoreName)
	);
    
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
    
CREATE TABLE IF NOT EXISTS shoppinglist (
	ListItemID			INTEGER PRIMARY KEY AUTOINCREMENT,
	InventoryItem		Integer				NOT NULL,
    Patron			Integer				NOT NULL,
    Quantity  		    Integer 	       	NOT NULL,
    CONSTRAINT 		    InventoryItem_FK 	FOREIGN KEY (InventoryItem)
							REFERENCES  inventory (ItemID)
								ON UPDATE CASCADE,
	CONSTRAINT 		    Patron_FK 		FOREIGN KEY (Patron)
							REFERENCES  Patron (PatronID)
								ON UPDATE CASCADE,
	CONSTRAINT 			ShoppingList_UC		UNIQUE (InventoryItem, Patron)
	);
    
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