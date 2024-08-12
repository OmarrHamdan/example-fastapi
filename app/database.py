import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from psycopg2.extras import RealDictCursor
import time
from .config import settings
from urllib.parse import quote


password_encoded = quote(settings.database_password)
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{password_encoded}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine=create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

# while True:     
#     try:
#         conn=psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='Skyrim123@@',cursor_factory=RealDictCursor)
#         cursor=conn.cursor()
#         print('Database connection was successfull')
#         break
#     except Exception as error:
#         print(error)
#         time.sleep(2)

#uvicorn app.main:app --reload