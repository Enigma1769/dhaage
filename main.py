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

def admin_panel():
    while True:
        print("\nAdmin Panel:")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Exit Admin Panel")
        
        admin_choice = int(input("Enter your choice: "))
        
        if admin_choice == 1:
            add_item()
        elif admin_choice == 2:
            view_inventory()
        elif admin_choice == 3:
            print("Exiting Admin Panel.")
            break
        else:
            print("Invalid choice. Please choose again.")

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


def add_item():
    print("Adding a new item to the inventory:")
    brand_name = input("Enter brand name: ")
    cloth_type = input("Enter cloth type: ")
    MRP = float(input("Enter MRP: "))
    discount = int(input("Enter discount: "))
    material = input("Enter material: ")
    color = input("Enter color: ")
    size = input("Enter size: ")
    season = input("Enter season: ")
    stock_quantity = int(input("Enter stock quantity: "))
    
    sql = "INSERT INTO clothes_info (brand_name, cloth_type, MRP, Discount, Material, Color, Size, Season, StockQuantity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (brand_name, cloth_type, MRP, discount, material, color, size, season, stock_quantity)
    
    mycursor.execute(sql, val)
    mydb.commit()
    
    print("Item added successfully!")

def view_inventory():
    print("Viewing inventory:")
    mycursor.execute("SELECT * FROM clothes_info")
    result = mycursor.fetchall()
    
    for row in result:
        print(row)
        
def exit_program():
    print("Exiting the program.")
    mydb.close()
    exit()

menu = {
    1: add_item,
    2: view_inventory,
    3: exit_program
}


while True:
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