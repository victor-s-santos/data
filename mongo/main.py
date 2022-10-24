import pymongo

if __name__ == "__main__":
    mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
    mongo_client["Mongo"]["API"].insert_one({"name": "First Document"})


