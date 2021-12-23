from pymongo import MongoClient
import json

IP = "<TARGET_IP>"
port = 27017

client = MongoClient(IP, port, username="", password="")

# Get server info
server_info = client.server_info()
print(json.dumps(server_info, indent=2, sort_keys=True))

# Get available databases
print()
print("Databases:")
databases_names = client.list_database_names()
for db_name in databases_names:
    print("-> {}".format(db_name))
    current_db = client[db_name]
    collection_names = current_db.list_collection_names()
    
    print("Available Collections:")
    for collection in collection_names:
        print("->> {}".format(collection))
        columns = current_db[collection]
        for row in columns.find():
            print(row)
    print()
