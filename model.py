from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine, delete, func, ForeignKey, Table
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine("sqlite:///NT_skelbimai.db")
Base = declarative_base()


#pridetas komentas
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

class Vartotojas(Base):
    __tablename__ = 'vartotojas'
    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    pavarde = Column(String)
    tel_nr = Column(String)
    username = Column(String)
    slaptazodis = Column(String)
    objektas1 = relationship('Objektas', back_populates='vartotojas1', cascade='all, delete, delete-orphan')


class Objektas(Base):
    __tablename__ = 'objektas'
    id = Column(Integer, primary_key=True)
    adresas = Column(String)
    objekto_tipas = Column(String)
    plotas = Column(Float)
    miestas = Column(String)
    vartotojas_id = Column(Integer, ForeignKey('vartotojas.id'))
    vartotojas1 = relationship('Vartotojas', back_populates='objektas1')
    skelbimas2 = relationship('Skelbimas', back_populates='objektas2', cascade='all, delete, delete-orphan')


Base.metadata.create_all(engine)