class Shoppinglist:
    def __init__(self, db):
        self.db = db
        
    def add_item(self, inventory_id, patron_id, qty):
        self.db.execute("INSERT INTO shoppinglist(InventoryItem, Patron, Quantity) VALUES(?, ?, ?)", ((inventory_id, patron_id, qty),))
        
    def view_list(self, patron_id):
        res = self.db.execute(
        """
        SELECT *
        FROM shoppinglist
        WHERE Patron == ?
        """,
        (patron_id,)
        )
        return res.fetchall()
        
    