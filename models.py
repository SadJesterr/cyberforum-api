import os

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from dotenv import load_dotenv


load_dotenv()
engine = create_engine(f'sqlite:///{os.getenv("DATABASE_NAME")}', echo=False, connect_args={'check_same_thread': False})
sessionLocal = sessionmaker(engine)
Base = declarative_base()

class Theme(Base):
    __tablename__ = "theme"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    text = Column(String)

    def __repr__(self):
        return f"name={self.name}, text={self.text}"

class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True)
    author_name = Column(String)
    theme_id = Column(Integer, ForeignKey('theme.id'))
    quote_id = Column(Integer, ForeignKey('comment.id'))
    text = Column(String)

    theme = relationship(Theme)

    def __repr__(self):
        return f"theme_id={self.theme_id}, quote_id={self.quote_id}, text={self.text}"


def create_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)