import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
import warnings

USER = "root"
PASSWORD = "password"
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "trig_db"
TABLENAME = "trig_table"

# create the dataframe
x = np.arange(0, 1000)
df = pd.DataFrame({"x": x, "sin": np.sin(x), "cos": np.cos(x), "tan": np.tan(x)})

engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}")

try:
    engine.execute(f"CREATE DATABASE {DATABASE}")
except ProgrammingError:
    warnings.warn(
        f"Could not create database {DATABASE}. Database {DATABASE} may already exist."
    )
    pass

engine.execute(f"USE {DATABASE}")
engine.execute(f"DROP TABLE IF EXISTS {TABLENAME}")
df.to_sql(name=TABLENAME, con=engine)
