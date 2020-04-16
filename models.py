from sqlalchemy import Table, create_engine, Column, Integer, Float, String, ForeignKey, Boolean 
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///banco.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Usuario(Base):
    __tablename__='usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    email = Column(String(300))

    def __repr__(self):
        return '"{}"'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()
        

class Tarefa(Base):
    __tablename__='tarefas'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(80))
    descricao = Column(String(300))
    tempo = Column(Float())
    usuario = Column(Integer())

    def __repr__(self):
        return '"{}"'.format(self.titulo)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':

    init_db()
