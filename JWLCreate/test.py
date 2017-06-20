import pyexcel as pe 

records = pe.iget_records(file_name="G:/GitHub/fluffy-couscous/JWLCreate/Test Data/Notes-3-Entries.csv")
for record in records:

    print ("%s %d:%d" %(record['Book'], record['Chapter'], record['Verse']))
    print ("Note title = %s" %(record['Title']))
    print ("Note Content = %s" %(record['Content']))
    print ("---")
