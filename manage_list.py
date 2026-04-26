class Shoppinglist:
    def __init__(self, db):
        self.db = db

    def add_item(self, inventory_id, patron_id, qty):
        """
        Add an inventory item to a patron's shopping list.
        If the item is already on the patron's list, increase the quantity.
        """
        inventory_id = int(inventory_id)
        patron_id = int(patron_id)
        qty = int(qty)

        if qty <= 0:
            print("Quantity must be greater than 0.")
            return False

        res = self.db.execute(
            """
            SELECT ListItemID, Quantity
            FROM shoppinglist
            WHERE InventoryItem == ?
              AND Patron == ?
            """,
            (inventory_id, patron_id)
        )

        existing_item = res.fetchone()

        if existing_item:
            list_item_id = existing_item[0]
            current_qty = existing_item[1]
            new_qty = current_qty + qty

            self.db.execute(
                """
                UPDATE shoppinglist
                SET Quantity = ?
                WHERE ListItemID == ?
                """,
                (new_qty, list_item_id)
            )
        else:
            self.db.execute(
                """
                INSERT INTO shoppinglist(InventoryItem, Patron, Quantity)
                VALUES(?, ?, ?)
                """,
                (inventory_id, patron_id, qty)
            )

        return True

    def view_list(self, patron_id:int, store_id:int=None):
        """
        View a patron's shopping list with item, store, quantity, price, and total information.
        """
        patron_id = int(patron_id)
        
        if store_id:
            res = self.db.execute(
            """
            SELECT 
                sl.ListItemID,
                i.ItemID,
                i.ItemName,
                i.ItemDescription,
                st.StoreName,
                sl.Quantity,
                i.Price,
                ROUND(sl.Quantity * i.Price, 2) AS LineTotal
            FROM shoppinglist sl
            JOIN inventory i ON i.ItemID = sl.InventoryItem
            JOIN store st ON st.StoreID = i.ItemStore
            WHERE sl.Patron == ?
            AND st.StoreID == ?
            ORDER BY st.StoreName, i.ItemName
            """,
            (patron_id, store_id)
            )
        
        else:
            res = self.db.execute(
                """
                SELECT 
                    sl.ListItemID,
                    i.ItemID,
                    i.ItemName,
                    i.ItemDescription,
                    st.StoreName,
                    sl.Quantity,
                    i.Price,
                    ROUND(sl.Quantity * i.Price, 2) AS LineTotal
                FROM shoppinglist sl
                JOIN inventory i ON i.ItemID = sl.InventoryItem
                JOIN store st ON st.StoreID = i.ItemStore
                WHERE sl.Patron == ?
                ORDER BY st.StoreName, i.ItemName
                """,
                (patron_id,)
            )

        return res.fetchall()

    def remove_item(self, list_item_id):
        """
        Remove one item from the shopping list using its ListItemID.
        """
        list_item_id = int(list_item_id)

        res = self.db.execute(
            """
            DELETE FROM shoppinglist
            WHERE ListItemID == ?
            """,
            (list_item_id,)
        )

        return res.rowcount

    def update_quantity(self, list_item_id, qty):
        """
        Update quantity for a shopping list item.
        If qty is 0 or less, remove the item.
        """
        list_item_id = int(list_item_id)
        qty = int(qty)

        if qty <= 0:
            return self.remove_item(list_item_id)

        res = self.db.execute(
            """
            UPDATE shoppinglist
            SET Quantity = ?
            WHERE ListItemID == ?
            """,
            (qty, list_item_id)
        )

        return res.rowcount

    def calculate_total(self, patron_id):
        """
        Calculate total cost of a patron's shopping list.
        """
        patron_id = int(patron_id)

        res = self.db.execute(
            """
            SELECT ROUND(COALESCE(SUM(sl.Quantity * i.Price), 0), 2)
            FROM shoppinglist sl
            JOIN inventory i ON i.ItemID = sl.InventoryItem
            WHERE sl.Patron == ?
            """,
            (patron_id,)
        )

        total = res.fetchone()[0]
        return total

    def clear_list(self, patron_id):
        """
        Delete all items from a patron's shopping list.
        """
        patron_id = int(patron_id)

        res = self.db.execute(
            """
            DELETE FROM shoppinglist
            WHERE Patron == ?
            """,
            (patron_id,)
        )
        
        return res.rowcount
        
    def view_list_stores(self):
        """
        View stores on the shopping list.
        """

        res = self.db.execute(
            """
            SELECT 
                i.ItemStore,
                st.StoreName
            FROM shoppinglist sl
            JOIN inventory i ON i.ItemID = sl.InventoryItem
            JOIN store st ON st.StoreID = i.ItemStore
            """
        )

        return res.fetchall()
        
    def view_list_patrons(self, store_id:int):
        """
        View patrons on the shopping list with items from selected store.
        """
    
        res = self.db.execute(
            """
            SELECT 
                sl.Patron,
                p.PatronFirstName,
                p.PatronLastName
            FROM shoppinglist sl
            JOIN inventory i ON i.ItemID = sl.InventoryItem
            JOIN patron p ON p.PatronID = sl.Patron
            WHERE i.ItemStore == ?
            """,
            (store_id,)
        )
    
        return res.fetchall()
