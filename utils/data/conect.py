from tinydb import TinyDB
from utils.data.model import Texto


bd = TinyDB('utils/data/db.json')

def insert(model: Texto):
    return bd.insert({"STRING" : model.texto})

def show():
    return bd.all()


  