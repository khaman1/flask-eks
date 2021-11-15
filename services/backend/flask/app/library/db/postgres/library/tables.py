from .shared import *
from math import ceil


class AccountsModel(declarative_base()):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)

    account_id = Column(String)


class Tables:
    def init(self):
        self.engine = new_engine()
        self.session = sessionmaker(bind=self.engine)()

        self.DB['accounts'] = mySQLAlchemy(
            session=self.session,
            table=AccountsModel,
        )

    def destroy(self):
        self.session.close()
        self.engine.dispose()

    def get_account(self, account_id=''):
        record = self.DB.accounts.get().filter(
            AccountsModel.account_id == str(account_id)).all()[0].__dict__

        return {
            'id': str(record['id']),
            'account_id': record['account_id'],
        }
