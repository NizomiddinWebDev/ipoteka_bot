from calendar import monthrange
from datetime import datetime, timedelta

from sqlalchemy import Column, Integer, String, Boolean, Text, MetaData, distinct, DateTime, Table, Identity
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

connect1 = 'postgresql+psycopg2://postgres:1234@localhost/bot_db'
connect2 = 'mysql+pymysql://gen_user:jp7bbzbxd@188.225.73.190:3306/default_db'
engine = create_engine(connect1, echo=True)

Base = declarative_base()

metadata = MetaData()

data = Table(
    "TelegramUser",
    metadata,
    Column(
        'id', Integer, Identity(start=1, cycle=True), primary_key=True
    ),
    Column('tg_user_id', Integer, unique=True),
    Column('chat_id', Integer),
    Column('phone_number', String),
    Column('full_name', String),
    Column('lang', String),
    Column('is_verified', Boolean),
    Column('code', String),
    Column('send_message_type', String),
    Column('ban', Boolean),
    Column('date_ban', String),
    Column('created_date', DateTime),
    Column('updated_at', DateTime),
)
metadata.create_all(engine)


class TelegramUser(Base):
    __tablename__ = 'TelegramUser'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tg_user_id = Column(Integer, unique=True)
    chat_id = Column(String)
    phone_number = Column(String)
    full_name = Column(String)
    lang = Column(String)
    is_verified = Column(Boolean, default=False)
    code = Column(String)
    send_message_type = Column(String)
    ban = Column(Boolean, default=False)
    date_ban = Column(String, nullable=True)
    created_date = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


"""This is User database """


async def new_user_add(chat_id, tg_user_id, full_name):
    Session = sessionmaker(bind=engine)
    session = Session()
    customer = TelegramUser(
        tg_user_id=tg_user_id,
        chat_id=chat_id,
        full_name=full_name,
    )
    session.add(customer)
    session.commit()


async def getUser(user_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(TelegramUser).filter(TelegramUser.tg_user_id == user_id).one()
    return result


async def get_user_name(full_name):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(TelegramUser).filter(TelegramUser.full_name == full_name).one()
    return result


async def set_user_lang(tg_user_id, lang):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(TelegramUser).filter(TelegramUser.tg_user_id == tg_user_id).update({TelegramUser.lang: lang})
    session.commit()


async def set_phone_number(tg_user_id, phone_number):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(TelegramUser).filter(TelegramUser.tg_user_id == tg_user_id).update(
        {TelegramUser.phone_number: phone_number})
    session.commit()


async def set_phone_code(tg_user_id, code):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(TelegramUser).filter(TelegramUser.tg_user_id == tg_user_id).update(
        {TelegramUser.code: code})
    session.commit()


async def set_user_verified(tg_user_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(TelegramUser).filter(TelegramUser.tg_user_id == tg_user_id).update(
        {TelegramUser.is_verified: True})
    session.commit()


#
async def getUserList():
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(TelegramUser).all()
    return result


#
async def getUsersCount():
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(TelegramUser).count()
    return result


async def ban_user(tg_user_id):
    today_date = datetime.now().date()  # 2021-10-29
    year = today_date.year
    month = today_date.month

    days_in_month = monthrange(year, month)[1]
    next_month = today_date + timedelta(days=days_in_month)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(TelegramUser).filter(TelegramUser.tg_user_id == tg_user_id).update(
        {TelegramUser.ban: True})
    session.query(TelegramUser).filter(TelegramUser.tg_user_id == tg_user_id).update(
        {TelegramUser.date_ban: str(next_month)})
    session.commit()


async def unban_user(tg_user_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(TelegramUser).filter(TelegramUser.tg_user_id == tg_user_id).update(
        {TelegramUser.ban: False})
    session.commit()
