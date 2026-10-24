import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

def get_engine():
    return create_engine(os.environ['DATABASE_URL'], pool_pre_ping=True)

def run_sql_file(path, engine):
    with open(path) as f, engine.begin() as conn:
        conn.execute(text(f.read()))
