from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine, Text, Boolean

engine = create_engine('mysql+pymysql://gen_user:jp7bbzbxd@188.225.73.190:3306/default_db', echo=True)

meta = MetaData()

students = Table(
   'Kvartira_Data', meta,
   Column('id', Integer, primary_key = True),
   Column('hold', String(200), index=True),
   Column('place', String(200), index=True),
   Column('region', String(200), index=True),
   Column('target', String(200), index=True),
   Column('price',String(200), index=True),
   Column('count_rooms', String(200), index=True),
   Column('photos_id', Text),
   Column('is_active', Boolean),
)

meta.create_all(engine)