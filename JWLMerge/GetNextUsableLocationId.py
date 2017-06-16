import sqlite3

def getNextUsableLocationId(sqlite3Connection):
    results = []
    cursor = sqlite3Connection.cursor()
    for value in cursor.execute('SELECT LocationId FROM Location'):
        results += value
    nextUsableLocationId = max(results) + 1
    return nextUsableLocationId

fullPathFirstDb = '/home/dirk/git/fluffy-couscous/JWLMerge/userDataSmall.db'
conn = sqlite3.connect(str(fullPathFirstDb))

print getNextUsableLocationId(conn)

conn.close()
