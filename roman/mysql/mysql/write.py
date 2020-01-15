import pandas as pd
from sqlalchemy import create_engine

def write_mysql(filename,name):
    data = pd.read_csv(filename,encoding = 'gbk',header = None)
    engine = create_engine('mysql+mysqldb://root:roman@120.26.240.13:3306/roman?charset=utf8')
    pd.io.sql.to_sql(frame=data,name=name,con=engine,schema='roman',index=False,if_exists='append')