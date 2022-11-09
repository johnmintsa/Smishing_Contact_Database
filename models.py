from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from database import Base

class Contact(Base):
    __tablename__ = "Contact_info"

    id = Column(Integer, primary_key=True, nullable= False)
    Contact = Column(Integer, nullable = False)
    Username = Column(String, nullable= False)
