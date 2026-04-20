from db import AppDataBase

db = AppDataBase()

res = db.execute(
    '''
    SELECT * 
    FROM shoppingcart sc 
    JOIN shoppinglist sl ON sc.ShoppingListItem = sl.ListItemID
    JOIN inventory i ON i.ItemID = sl.InventoryItem
    JOIN customer c ON c.CustomerID = sl.Customer
    JOIN shopper s ON s.ShopperID = sc.Shopper
    JOIN store st ON i.ItemStore = st.StoreID;
    '''
    )
print(res.fetchall())

# Execute query to get table names
res = db.execute("SELECT name FROM sqlite_master WHERE type='table';")
# Print the list of tables
print(res.fetchall())
