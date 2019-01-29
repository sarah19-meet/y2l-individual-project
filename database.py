from model import *     
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import googletrans

engine = create_engine('sqlite:///project.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

translator = googletrans.Translator()

def add_user(name,username, password):
    print("Added a user!")
    user = User(name=name,username=username ,password=password)
    session.add(user)
    session.commit()

def get_all_users():
  users = session.query(User).all()
  return users


def query_by_name(name):
  user= session.query(User).filter_by(name=name).first()
  return user 

def query_by_username(username):
  user= session.query(User).filter_by(username=username).first()
  print('user: ' + str(user))
  return user 

def query_by_password(password):
  users= session.query(User).filter_by(password=password).all()
  return users   


def add_programme(name,email, phone_num, address, link):
    print("Added a programme!")
    prog = programme(name=name, email=email, phone_num=phone_num,address=address,link=link, )
    session.add(prog)
    session.commit()

def get_all_programmes():
    progs = session.query(programme).all()
    return progs

def query_by_programme(name):
  p= session.query(programme).filter_by(name=name).first()
  return p



def translate_language(text, language_to="english"):
  return translator.translate(text, dest=googletrans.LANGCODES[language_to]).text, googletrans.LANGCODES[language_to]

# def search_programme(search):
#   results = session.query(programme).filter(programme.name.contains(search)).all()
#   return results

# sarah=add_programme("sarah" ,  "s@gmail.com" , 000, "ha","rf")