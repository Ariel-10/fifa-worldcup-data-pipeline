import pandas as pd
from sqlalchemy import create_engine
import os

# connection — env variables (docker-compose)
def get_engine():
    return create_engine(
        f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )

# load all data
def load_matches():
    engine = get_engine()
    return pd.read_sql("SELECT * FROM public.fct_matches", engine)