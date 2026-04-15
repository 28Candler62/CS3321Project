/*
Tables:
	client
    shopper
    store
    shoppingList
    shoppingCart
    inventory
*/

USE project;

CREATE TABLE client (
	ClientID				Integer				NOT NULL AUTO_INCREMENT,
	ClientFirstName			Char(35)			NOT NULL,
	ClientLastName			Char(35)			NOT NULL,
	CONSTRAINT			Client_PK			PRIMARY KEY(ClientID)
	);
    
CREATE TABLE shopper (
	ShopperID				Integer				NOT NULL AUTO_INCREMENT,
	ShopperFirstName		Char(35)			NOT NULL,
	ShopperLastName			Char(35)			NOT NULL,
	CONSTRAINT			Shopper_PK			PRIMARY KEY(ShopperID)
	);
    
CREATE TABLE store (
	StoreID				Integer				NOT NULL AUTO_INCREMENT,
	StoreName			Char(35)			NOT NULL,
	CONSTRAINT			Store_PK			PRIMARY KEY(StoreID)
	);
    
CREATE TABLE inventory (
	ItemID				Integer				NOT NULL AUTO_INCREMENT,
	ItemName			Char(35)			NOT NULL,
    ItemDescription		Char(70)			NOT NULL,
    ItemStore			Integer				NOT NULL,
    Quantity  		    Integer 	       	NOT NULL,
	Price  			    Decimal(9,2)     	NOT NULL,
    CONSTRAINT 		    ItemStore_FK 	FOREIGN KEY (ItemStore)
							REFERENCES  store (StoreID)
								ON UPDATE CASCADE,
	CONSTRAINT			Item_PK			PRIMARY KEY(ItemID)
	);