class ExtractFromMongo:

    def __init__(self, db, coll):

        self._collection = db[coll]
        self._n_call = -1

    def pagination(self, bach):
        self._n_call += 1
        return self._collection.find({},{"_id": 0}).sort("type", 1). \
            skip(self._n_call*bach).limit(bach)
