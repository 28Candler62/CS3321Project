class Patron:
    def __init__(self, db):
        self.db = db
        
    def addinfo(self, fname, lname):
        self.db.executemany("INSERT INTO patron(PatronFirstName, PatronLastName) VALUES(?, ?)", ((fname, lname),))
        
    def get_id(self, lname):
        res = self.db.execute(
        """
        SELECT PatronID
        FROM patron
        WHERE PatronLastName == ?
        """,
        (lname,)
        )
        return res.fetchone()
        
    def shop(self):
        res= self.db.execute('SELECT StoreID, StoreName FROM store')
        print('Store ID \t Store Name')
        [print(f'{x[0]}\t\t{x[1]}') for x in res.fetchall()]
        store = int(input('Select Store ID: '))
        