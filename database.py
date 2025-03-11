from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# load environment variables
load_dotenv()

# get database url from environment variables
MYSQL_HOST = os.getenv("mysql_host")
MYSQL_PORT = os.getenv("mysql_port")
MYSQL_USER = os.getenv("mysql_user")
MYSQL_PASSWORD = os.getenv("mysql_password")
MYSQL_DATABASE = os.getenv("mysql_database")


DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"

# create database connection
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10,
    pool_timeout=30,
    pool_recycle=3600
)

# create session factory
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# create base class for models
Base = declarative_base()