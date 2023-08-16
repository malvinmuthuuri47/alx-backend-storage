#!/usr/bin/env python3
"""
    A module that provides stats about Nginx logs stored on MongoDB
"""
import pymongo


def log_stats():
    """
        This function Counts the number of documents stored in the
        database and prints the results based on the criteria provided
    """
    # Get total number of documents in the collection
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


if __name__ == "__main__":
    # MongoDB connection settings
    database_name = "logs"
    collection_name = "nginx"

    # Connect to MongoDB
    client = pymongo.MongoClient()
    db = client[database_name]
    collection = db[collection_name]

    log_stats()

    # Close the connection
    client.close()
