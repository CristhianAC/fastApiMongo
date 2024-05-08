from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os
conn = MongoClient("mongodb+srv://cristhianholad:3uFfi9wAlgAx2nJr@tallercrud.i7af9tc.mongodb.net/?retryWrites=true&w=majority&appName=TallerCrud",server_api=ServerApi('1'))
