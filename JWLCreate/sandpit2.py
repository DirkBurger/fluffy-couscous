search_for = "difMulti,difValues,difHere,'Revelation 21'"

dict = {'1':"multi,values,here,'Genesis 1'", '2':"difMulti,difValues,difHere,'Revelation 21'"}
for key in dict.iterkeys():
    print dict[key]

invd = { v:k for k,v in dict.items() }

print invd
print "---"
for key in invd.iterkeys():
    print invd[search_for]
print "---"