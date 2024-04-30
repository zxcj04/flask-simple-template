from pymongo import MongoClient

DB = None


def setup(conf: dict):
    global DB
    DB = MongoClient(
        host=conf.get("host", "localhost"),
        port=conf.get("port", 27017),
        username=conf.get("user", None),
        password=conf.get("pwd", None),
        authSource=conf.get("authSource", "admin"),
    )
    DB = DB[conf.get("db", "test")]
    print("[Init] Database")


def get_db():
    global DB
    return DB
