# Two 'userData.db' sqlite3 databases needed
# 'userDataLarge.db' = Main database
# 'userDataSmall.db' = secondary database to be merged in

import sqlite3

largeResults = []
smallResults = []

connLarge = sqlite3.connect('/home/dirk/Git/fluffy-couscous/JWLMerge/userDataLarge.db')
connSmall = sqlite3.connect('/home/dirk/Git/fluffy-couscous/JWLMerge/userDataSmall.db')

cursorLarge = connLarge.cursor()
cursorSmall = connSmall.cursor()

for rowLarge in cursorLarge.execute('SELECT BookNumber, ChapterNumber, Title FROM Location WHERE BookNumber IS NOT NULL'):
    largeResults += [rowLarge]
for rowSmall in cursorSmall.execute('SELECT BookNumber, ChapterNumber, Title FROM Location WHERE BookNumber IS NOT NULL'):
    smallResults += [rowSmall]

# similarity between
similarResults =  set(smallResults).intersection(largeResults)

# get Location record of similar results in userDataLarge.db
for similarItem in similarResults:
    title = (similarItem[2],)
    cursorLarge.execute('SELECT * FROM Location WHERE Title=?', title)
    print cursorLarge.fetchall()

# if Title (large) is NOT NULL, change Locationid in Notes table (small) to LocationId (large)
# if Title (large) is NULL, set correct, change Locationid in Notes table (small) to LocationId (large)
# get the largest value of LocationId from Location table (large)
#


connLarge.close()
connSmall.close()
