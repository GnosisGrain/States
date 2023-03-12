import pandas
from sqlalchemy import create_engine

hostname="127.0.0.1"
uname="root"
pwd="1cadwaer2"
dbname="states"

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
            .format(host=hostname, db=dbname, user=uname, pw=pwd))

tables = pandas.read_csv(r"C:\Users\Doc\Documents\CNE 350 FINAL STATES PROJECT\populationstate.csv")



connection=engine.connect()
tables.to_sql('population',con = engine, if_exists = 'replace')
connection.close()
print(tables)
