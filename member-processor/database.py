import os
from pymongo import MongoClient


class Database:
    def __init__(self):
        # Initialize client
        self.client=MongoClient(os.getenv("MONGO_CONNECTION_STRING"))
        self.db=self.client["clanPointsDB"]
        
        # Set up collections
        self.members_collection=self.db["clanmembers"]
        self.applicants_collection=self.db["applicants"]
        self.rankuprequests_collection=self.db["rankuprequests"]
