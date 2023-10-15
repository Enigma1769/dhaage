import mysql.connector as msc
import mypass
pwd= mypass.pwd()



try:
  with open("pass.txt", "r") as file:
    file_contents = file.read()
    l = [item.strip() for item in file_contents.strip("[]").split(",")]
    host=l[1]
    user=l[2]
    password=l[3]
    database='dhaage' 
except:
    passfile=open('pass.txt','w+')
    host=input("Enter the host(localhost): ")
    user=input("Enter the user(root): ")
    password=input("Enter the database password: ")
    database='dhaage'
    l=[host,user,password,database]
    passfile.write(str(l))



mydb = msc.connect(
  host="localhost",
  user="root",
  password=pwd,
  database="dhaage"
)

#print(mydb)
# Create a cursor
mycursor = mydb.cursor()

# # Executing the query to test
# query = 'SELECT * FROM clothes_info'
# mycursor.execute(query)
# # Fetch and print the results
# result = mycursor.fetchall()
# for row in result:
#     print(row)

# Close the cursor and database connection
# mycursor.close()
# mydb.close()



def view_last_id():
    mycursor.execute("SELECT MAX(id) FROM clothes_info")
    last_id = mycursor.fetchone()[0]
    
    if last_id is not None:
        print(f"The last inserted ID is: {last_id}")
    else:
        print("No items have been inserted yet.")

def user_panel():
    while True:
        print("\nUser Panel:")
        print("1. View Inventory")
        print("2. Exit User Panel")
        
        user_choice = int(input("Enter your choice: "))
        
        if user_choice == 1:
            view_inventory()
        elif user_choice == 2:
            print("Exiting User Panel.")
            break
        else:
            print("Invalid choice. Please choose again.")

def admin_panel():
    while True:
        print("\nAdmin Panel:")
        print("1. Add Item to Inventory")
        print("2. View Inventory")
        print("3. View Last Inserted ID")
        print("4. Remove Item by Index")
        print("5. Exit Admin Panel")
        
        admin_choice = int(input("Enter your choice: "))
        
        if admin_choice == 1:
            add_item()
        elif admin_choice == 2:
            view_inventory()
        elif admin_choice == 3:
            view_last_id()
        elif admin_choice == 4:
            remove_item()
        elif admin_choice == 5:
            print("Exiting Admin Panel.")
            break
        else:
            print("Invalid choice. Please choose again.")


def add_item():
    print("Adding a new item to the inventory:")
    
    mycursor.execute("SELECT MAX(id) FROM clothes_info")
    last_id = mycursor.fetchone()[0]
    if last_id is not None:
        new_id = last_id + 1
    else:
        new_id = 1

    
    print(f"Curent ID: {last_id+1}")
    brand_name = input("Enter brand name: ")
    cloth_type = input("Enter cloth type: ")
    MRP = float(input("Enter MRP: "))
    discount = int(input("Enter discount: "))
    material = input("Enter material: ")
    color = input("Enter color: ")
    size = input("Enter size: ")
    season = input("Enter season: ")
    stock_quantity = int(input("Enter stock quantity: "))
    
    sql = "INSERT INTO clothes_info (id, brand_name, cloth_type, MRP, Discount, Material, Color, Size, Season, StockQuantity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (new_id, brand_name, cloth_type, MRP, discount, material, color, size, season, stock_quantity)
    
    mycursor.execute(sql, val)
    mydb.commit()
    
    print("Item added successfully!")

def view_inventory():
    print("Viewing inventory:")
    mycursor.execute("SELECT * FROM clothes_info")
    result = mycursor.fetchall() #[(1,),(2,)...]
    
    for row in result:
        print(row)
        
def exit_program():
    print("Exiting the program.")
    mydb.close()
    exit()


def admin_panel():
    while True:
        print("\nAdmin Panel:")
        print("1. Add Item to Inventory")
        print("2. View Inventory")
        print("3. View Last Inserted ID")
        print("4. Remove Item by Index #Currently not working")
        print("5. Exit Admin Panel")
        
        admin_choice = int(input("Enter your choice: "))
        
        if admin_choice == 1:
            add_item()
        elif admin_choice == 2:
            view_inventory()
        elif admin_choice == 3:
            view_last_id()
        elif admin_choice == 4:
            remove_item()
        elif admin_choice == 5:
            print("Exiting Admin Panel.")
            break
        else:
            print("Invalid choice. Please choose again.")

while True:
    print('''
$$$$$$$\  $$\                                               
$$  __$$\ $$ |                                              
$$ |  $$ |$$$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  
$$ |  $$ |$$  __$$\  \____$$\  \____$$\ $$  __$$\ $$  __$$\ 
$$ |  $$ |$$ |  $$ | $$$$$$$ | $$$$$$$ |$$ /  $$ |$$$$$$$$ |
$$ |  $$ |$$ |  $$ |$$  __$$ |$$  __$$ |$$ |  $$ |$$   ____|
$$$$$$$  |$$ |  $$ |\$$$$$$$ |\$$$$$$$ |\$$$$$$$ |\$$$$$$$\ 
\_______/ \__|  \__| \_______| \_______| \____$$ | \_______|
                                        $$\   $$ |          
        Where Fashion Meets Comfort     \$$$$$$  |          
                                         \______/         
          ''')
    
    print("\nMain Menu:")
    print("1. Admin Access")
    print("2. User Access")
    print("3. Exit")
    
    main_choice = int(input("Enter your choice: "))
    
    if main_choice == 1:
        admin_panel()
    elif main_choice == 2:
        user_panel()
    elif main_choice == 3:
        exit_program()
    else:
        print("Invalid choice. Please choose again.")