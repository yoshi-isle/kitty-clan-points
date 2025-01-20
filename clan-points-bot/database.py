import os
from pymongo import MongoClient


class Database:
    def __init__(self):
        # Initialize client
        self.client=MongoClient(os.getenv("MONGO_CONNECTION_STRING"))
        self.db=self.client[os.getenv("MONGO_DATABASE_NAME")]
        
        # Set up collections
        self.members_collection=self.db[os.getenv("MONGO_MEMBERS_COLLECTION_NAME")]
        self.applicants_collection=self.db[os.getenv("MONGO_APPLICANTS_COLLECTION_NAME")]
        self.rankuprequests_collection=self.db[os.getenv("MONGO_RANKUPREQUESTS_COLLECTION_NAME")]
