import pandas as pd 
from sqlalchemy import create_engine

DATABASE_URL = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

engine = create_engine(DATABASE_URL)