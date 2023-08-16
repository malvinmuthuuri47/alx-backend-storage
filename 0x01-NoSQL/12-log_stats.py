#!/usr/bin/env python3
"""A module that displays Nginx logs stored in MongoDB"""

import pymongo

# start MongoDb
sudo service mongod start

# MongoDB connection settings
db_name = "logs"
collection_name = "nginx"

# connecting to MongoDB
client = pymongo.MongoClient()
db = client[db_name]
collection = db[collection_name]

# Getting the number of documents in the collection
total_logs = collection.count_documents({})
print(f"{total_logs} logs")

# Get the number of documents with each HTTP method
http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_stats = [collection.count_documents({"method": method})
                for method in http_methods]

print("Methods:")
for method, count in zip(http_methods, method_stats):
    print(f"\tmethod {method}: {count} logs")

# Get the no. of documents with method=GET and path=/status
status_path_logs = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
print(f"{status_path_logs} status check")

# Close the MongoDB connection
client.close()
