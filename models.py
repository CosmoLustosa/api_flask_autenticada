from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(f'sqlite:///mydb.db')
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()

Base.query = db_session.query_property()

class Pessoas(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), index=True, nullable=False)
    idade = Column(Integer)
    

    def __repr__(self):
        return f'{self.nome}'

    def save(self):
        db_session.add(self)
        db_session.commit()



class Atividades(Base):
    __tablename__ = 'atividades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(600))
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship('Pessoas')

def init_db():
    Base.metadata.create_all(engine) # cria o banco

if __name__ == '__main__':
    init_db()