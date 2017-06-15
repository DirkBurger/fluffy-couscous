import sqlite3

conn = sqlite3.Connection('example.db')
c=conn.cursor()

# Create table
#c.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
#c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
#conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
#conn.close()

# Use the DB-API’s parameter substitution. 
# Put ? as a placeholder wherever you want to use a value, 
# and then provide a tuple of values as the second argument 
# to the cursor’s execute() method. 

# Never do this -- insecure!
# symbol = 'RHAT'
# c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)

# Do this instead
t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
#print c.fetchone()
print c.fetchall()
