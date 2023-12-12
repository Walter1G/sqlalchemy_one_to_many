from sqlalchemy import create_engine, Column, Integer, String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import os 
from sqlalchemy.orm import relationship

Current_Dir= os.path.dirname(os.path.realpath(__file__))
conn= 'sqlite:///'+os.path.join(Current_Dir,'blog.db')

engine=create_engine(conn, echo=True)

#tables are created from a base class, --> the declarative_base function
Base=declarative_base()

"""
class User:
    id:int pk
    username:str
    email:str
    
class Post:
    id:int pk
    title:str
    content:str
    user_id:int fk

"""

class User(Base):
    __tablename__='users'
    
    id=Column(Integer(), Primary_Key=True)
    username=Column(String(40), nullable=False)
    email=Column(String(40), nullable=True)
    
    posts=relationship('Post', backref='author' )
    
    def __repr__(self):
        return f"< User: {self.username}>"
    

class Post(Base):
    
    __tablename__='posts'
    
    id=Column(Integer(), Primary_Key=True)
    title=Column(String(45), nullable=False)
    content=Column(String(255), nullable=False)
    user_id=Column(Integer(), ForeignKey('users.id'))
    
    def __repr__(self):
        return f"< Post: {self.title}>"
    
    


