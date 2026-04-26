INSERT INTO patron (PatronFirstName, PatronLastName)
	VALUES 
    ('Mary', 'Smith'),
	('Pete', 'Hansen')/*,
	('Nancy', 'Meyers'),
	('Cindy', 'Lo'),
	('Jerry', 'Martin')*/;

INSERT INTO shopper (ShopperFirstName, ShopperLastName)
	VALUES 
    /*('Mary', 'Smith'),
	('Pete', 'Hansen'),
	('Nancy', 'Meyers'),*/
	('Cindy', 'Lo'),
	('Jerry', 'Martin');
    
INSERT INTO store (StoreName)
	VALUES 
    ('HEB'),
	('Home Depot');

INSERT INTO inventory (ItemName, ItemDescription, ItemStore, Quantity, Price)
	VALUES 
    ('carrot', 'Delicious carrot', 1, 10, 3.99),
	('screwdriver', 'Philips screwdriver', 2, 1, 7.50);
    
INSERT INTO shoppinglist (InventoryItem, Patron, Quantity)
	VALUES 
    (1, 1, 1),
	(2, 1, 1);
    
INSERT INTO shoppingcart (ShoppingListItem, Shopper)
	VALUES 
    (1, 1),
	(2, 2);

/*
SELECT * 
FROM shoppingcart sc 
JOIN shoppinglist sl ON sc.ShoppingListItem = sl.ListItemID
JOIN inventory i ON i.ItemID = sl.InventoryItem
JOIN patron p ON p.PatronID = sl.Patron
JOIN shopper s ON s.ShopperID = sc.Shopper
JOIN store st ON i.ItemStore = st.StoreID
WHERE st.StoreName = 'HEB';

SELECT * FROM shopper;

SELECT * 
FROM shoppinglist s 
JOIN inventory i ON i.ItemID = s.InventoryItem
JOIN patron p ON p.PatronID = s.Patron;

SELECT i.ItemID, i.ItemName, i.ItemDescription, s.StoreName, Quantity, Price 
FROM inventory i JOIN store s ON i.ItemStore = s.StoreID;
*/