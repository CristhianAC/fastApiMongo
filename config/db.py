from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os
conn = MongoClient(os.getenv("DB"),server_api=ServerApi('1'))
