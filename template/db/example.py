from . import get_db


def test():
    db = get_db()
    cols = db.list_collection_names()
    doc = db[cols[0]].find_one({})
    print(doc)
    print("DB Test Done")
    return doc
