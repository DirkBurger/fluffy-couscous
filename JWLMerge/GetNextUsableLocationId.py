import sqlite3

def get_next_usable_location_id(sqlite3_connection):
    cursor = sqlite3_connection.cursor()
    for value_q1 in cursor.execute('SELECT COUNT(*) from Location'):
        if value_q1[0] != 0:
            location_ids = []
            for value_q2 in cursor.execute('SELECT LocationId FROM Location'):
                location_ids += value_q2
            next_usable_location_id = max(location_ids) + 1
            return next_usable_location_id
        else:
            return int(1)
    cursor.close()

fullPathFirstDb = '/home/dirk/GitHub/fluffy-couscous/JWLMerge/userDataEmpty.db'
conn = sqlite3.connect(str(fullPathFirstDb))

print get_next_usable_location_id(conn)

conn.close()
