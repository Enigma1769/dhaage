import mysql.connector as msc
def connect():
    try:
        with open('password.txt', 'r+') as passfile:
            pwd = passfile.read()
            if not pwd:
                pwd = input("Enter the MySQL DB password: ")
                passfile.seek(0)
                passfile.write(pwd)
    except FileNotFoundError:
        pwd = input("Enter the MySQL DB password: ")
        with open('password.txt', 'w') as passfile:
            passfile.write(pwd)
    mydb = msc.connect(
        host="localhost",
        user="root",
        password=pwd,
        database="dhaage"
    )
    return mydb