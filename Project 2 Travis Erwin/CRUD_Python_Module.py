# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        self.username = username  #added these to remove hardcoded credentials
        self.password = password
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # 
        # Connection Variables 
        # 
        USER = self.username  
        PASS = self.password
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 
        self.database.command("ping")
        
            
    # method to implement the C in CRUD. 
    def create(self, data):
        if data is not None: 
            self.database.animals.insert_one(data)  # data should be dictionary
            return True
        else: 
            return False

    # method to implement the R in CRUD.
    
    def read(self, query):
        if query is not None:
            data = self.database.animals.find(query)
            return list(data)
        else:
            return[]
        
    # method to implement the U in CRUD
    
    def update(self, query, updatedInfo):
        if query is not None and updatedInfo is not None:
            result = self.database.animals.update_many(query, {"$set": updatedInfo})
            return result.modified_count
        else:
            return 0
        
    # method to implement the D
    
    def delete(self, query):
        if query is not None:
            result = self.database.animals.delete_many(query)
            return result.deleted_count
        else:
            return 0
            
            
            