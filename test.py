from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine

engine = create_engine('mysql+pymysql://gen_user:jp7bbzbxd@188.225.73.190:3306/default_db', echo=True)

meta = MetaData()

students = Table(
   'Kvartira_bot', meta,
   Column('chat_id', Integer, primary_key = True),
   Column('type', String(16), index=True),
   Column('state', String(16), index=True),
)

meta.create_all(engine)