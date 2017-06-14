import sqlite3

connection = sqlite3.Connection('/home/dirk/Git/fluffy-couscous/sqlite3dbs/userData4.db')
connection2 = sqlite3.Connection('/home/dirk/Git/fluffy-couscous/sqlite3dbs/userData3.db')
cursor=connection.cursor()
cursor2=connection2.cursor()
cursor.execute('SELECT LocationId, Title FROM Location')
cursor2.execute('SELECT LocationId, Title FROM Location')

bigResults =  cursor.fetchall()
littleResults = cursor2.fetchall()

i = 0
while i < len(littleResults):
    if littleResults[i][1] is not None:
        query = littleResults[i][1]

        for rows in bigResults:
            if rows[1] == query:
                print rows
                print littleResults[i]
        #print query
    i = i + 1
