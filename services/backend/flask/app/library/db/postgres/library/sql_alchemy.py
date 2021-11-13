class mySQLAlchemy:
    def __init__(self, session, table):
        self.table = table
        self.session = session

    def get(self):
        return self.session.query(self.table)

    def retrieve(self):
        return self.get().all()

    def insert(self, rows=[]):
        self.session.add(rows)
        self.session.commit()
