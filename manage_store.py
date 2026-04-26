class Store:
    def __init__(self, db):
        self.db = db
        
    def get_id(self, name):
        res = self.db.execute(
            """
            SELECT StoreID
            FROM store
            WHERE StoreName == ?
            """,
            (name,)
        )
        return res.fetchone()
        
        

"""
CREATE TABLE IF NOT EXISTS store (
	StoreID				INTEGER PRIMARY KEY AUTOINCREMENT,
	StoreName			Char(35)			NOT NULL,
    CONSTRAINT 			StoreName_UC		UNIQUE (StoreName)
	);

"""