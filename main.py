import pymysql
from pandas import DataFrame
import pandas

cars = {'id': [0,0,0,0],
        'category': ['Honda','Toyota','Ford','Audi'],
        'title': ['title 9','title 10','title 11','title 12'],
        'price': [228800,28800,2880,3880]
        }
df = DataFrame(cars)
engine = sqlalchemy.create_engine('mysql+pymysql://root@localhost/pruebas', encoding='utf-8')
connection = engine.connect()
df.to_sql(name='bd', con=connection, if_exists='append', index=False)
