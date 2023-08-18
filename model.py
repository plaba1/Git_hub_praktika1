from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine, delete, func, ForeignKey, Table
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine("sqlite:///NT_skelbimai.db")
Base = declarative_base()

class Agentura(Base):
    __tablename__ = 'agentura'
    id = Column(Integer, primary_key=True)
    pavadinimas = Column(String)
    imones_kodas = Column(String)
    skelbimas1 = relationship('Skelbimas', back_populates='agentura1', cascade='all, delete, delete-orphan')


class Skelbimas(Base):
    __tablename__ = 'skelbimas'
    id = Column(Integer, primary_key=True)
    kaina = Column(Integer)
    nuoma_pardavimas = Column(String)
    tekstas = Column(String)
    agentura_id = Column(Integer, ForeignKey('agentura.id'))
    agentura1 = relationship('Agentura', back_populates='skelbimas1')
    objektas_id = Column(Integer, ForeignKey('objektas.id'))
    objektas2 = relationship('Objektas', back_populates='skelbimas2')