#%%
import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv, find_dotenv

#%%
load_dotenv(find_dotenv())

engine = create_engine(os.environ["cockroack_db_connect_string"])
conn = engine.connect()

#%%
res = conn.execute('SELECT * FROM todos').fetchall()
print(res)
# %%
