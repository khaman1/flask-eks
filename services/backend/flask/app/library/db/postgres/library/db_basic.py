from .shared import *
from .tables import Tables


class DB_Basic(Tables, mySQLAlchemy):
    def __init__(self):
        self.DB = {}
        self.init()

        self.DB = obj(self.DB)

    def __del__(self):
        self.destroy()
