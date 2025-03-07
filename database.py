from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# load environment variables
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# create database connection
engine = create_engine(DATABASE_URL)

# create session factory
Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# create base class for models
Base = declarative_base()