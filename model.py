from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine, delete, func, ForeignKey, Table
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine("sqlite:///NT_skelbimai.db")
Base = declarative_base()