import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    lastName = Column(String(250), nullable=False)
    firstName = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    subscriptionDate = Column(String(250), nullable=False)
    favorites_fk_id = Column(Integer, ForeignKey('favorites.id'))
    


class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_fk_id = Column(Integer, ForeignKey('user.id'))
    people_fk_id = Column(Integer, ForeignKey('people.id'))
    planets_fk_id = Column(Integer, ForeignKey('planets.id'))
    species_fk_id = Column(Integer, ForeignKey('species.id'))
    vehicles_fk_id = Column(Integer, ForeignKey('vehicles.id'))
    


class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    species = Column(String(250), nullable=False)
    

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diamter = Column(String(250), nullable=False)
    rotation_period = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    

class Species(Base):
    __tablename__ = 'species'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    average_height = Column(String(250), nullable=False)
    language = Column(String(250), nullable=False)
    homeworld = Column(String(250), nullable=False)


class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    passengers = Column(Integer)
    max_atmosphering_speed = Column(String(250), nullable=False)


    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
