from pymongo import MongoClient, errors


def dbConnection(string: str, dbName: str, dbCol: str):
    try:
        client = MongoClient(string)
        database = client.get_database(dbName)
        collection = database.get_collection(dbCol)

        return collection

    except errors.ConfigurationError:
        print("===== [!] Error Database Connection =====")
