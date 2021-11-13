from .levels.level1 import Level1
from .levels.level2 import Level2
from .levels.level3 import Level3
from .levels.level4 import Level4
from .levels.level5 import Level5
from .library.db_basic import DB_Basic


class Postgres(DB_Basic, Level5, Level4, Level3, Level2, Level1):
    pass
