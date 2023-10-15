import mysql.connector as msc
import mypass
pwd= mypass.pwd()
def connect():
    mydb = msc.connect(
        host="localhost",
        user="root",
        password=pwd,
        database="dhaage"
    )
    return mydb