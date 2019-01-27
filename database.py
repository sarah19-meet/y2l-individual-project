from models import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///cats.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def function(parameter):
    pass


#####################################################3



# Database related imports
# Make sure to import your tables!
from model import Base, Donate

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import literal


# You can change the name of your database, just change project.db to whatever you want (make sure to include .db at the end!)
# Make sure you have the same name for the database in the app.py file!
engine = create_engine('sqlite:///project.db', connect_args={'check_same_thread': False})
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Your database functions are located under here (querying, adding items, etc.)

# Example of adding a student:
def add_donate(name,story,email, needer_type, needs, phone_num, address, link, pic):
    print("Added a donate!")
    don = Donate(name=name,story=story, email=email, needer_type=needer_type, needs=needs,phone_num=phone_num,address=address,link=link, pic=pic)
    session.add(don)
    session.commit()

def get_all_donates():
    donates = session.query(Donate).all()
    return donates

def get_all_donates_by_type(type):
	return session.query(Donate).filter(Donate.needs.contains(type)).all()
def search_donate(search):
	results = session.query(Donate).filter(Donate.name.contains(search)).all()
	return results

gilad=add_donate("gilad" , "i want to buy ice cream" , "g@gmail.com" , "person", "money", 000, "ha","rf", "ddfsdf")