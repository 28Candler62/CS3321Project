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
        
        