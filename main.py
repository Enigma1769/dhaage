import mysql.connector as msc
import mypass
pwd= mypass.pwd()
mydb = msc.connect(
  host="localhost",
  user="root",
  password=pwd,
  database="dhaage"
)

#print(mydb)

# Create a cursor
mycursor = mydb.cursor()

# Execute the query
query = 'SELECT * FROM clothes_info'
mycursor.execute(query)

# Fetch and print the results
result = mycursor.fetchall()
for row in result:
    print(row)

# Close the cursor and database connection
mycursor.close()
mydb.close()
