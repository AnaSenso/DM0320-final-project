import os
import dotenv
dotenv.load_dotenv()
import pandas as pd

import sqlalchemy as db
from getpass import getpass

password = os.getenv("SQLPASS")

dbName = "shiva"
connectionData = f"mysql+pymysql://root:{password}@localhost/{dbName}"

engine = db.create_engine(connectionData)
print("Connected to server!")

df = pd.read_sql_query("""
SELECT *
FROM shiva.ipip300 AS 
LIMIT 10
""", engine)

print(df)