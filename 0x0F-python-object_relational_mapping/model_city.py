#!/usr/bin/python3
"""
This module defines the City class using SQLAlchemy
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State

class City(Base):
    """City class
    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The id of the class
        name (str): The name of the class
        state_id (int): The state the city belongs to
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

