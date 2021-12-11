import pymongo
from pymongo import MongoClient
import os
import certifi


def get_database():
    connection_string = os.environ.get("CONNECTION_STRING")
    if not connection_string:
        raise RuntimeError("Bad connection string")
    client = MongoClient(connection_string, tlsCAFile=certifi.where())
    database = client["TablesClaims"]
    return database
