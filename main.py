from connection import connect
#print(mydb)
# Create a cursor
mydb = connect()
mycursor = mydb.cursor()
connection = mycursor

import csv
from datetime import datetime


def get_item_name(item_id):
    mycursor.execute("SELECT brand_name FROM clothes_info WHERE id = %s", (item_id,))
    row = mycursor.fetchone()
    if row:
        return row[0]
    else:
        return None



def write_purchase_history(brand_name, quantity):
    item_name = get_item_name(brand_name)
    if item_name is not None:
        with open('purchase_history.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([item_name, quantity, str(datetime.now())[:-7]])


def view_last_id():
    mycursor.execute("SELECT MAX(id) FROM clothes_info")
    last_id = mycursor.fetchone()[0]  
    return last_id

def update_stock_quantity(item_id, quantity):
    mycursor.execute("UPDATE clothes_info SET StockQuantity = StockQuantity - %s WHERE id = %s", (quantity, item_id))
    mydb.commit()

def buy_items():
    selected_items = []

    while True:
        item_id = input("Enter the ID of the item to buy (or 'q' to quit): ")
        
        if item_id == 'q':
            break
        
        quantity = int(input("Enter the quantity: "))
        selected_items.append((int(item_id), quantity))
        update_stock_quantity(int(item_id), quantity)
    
    return selected_items


def admin_panel():
    while True:
        print("\nAdmin Panel:")
        print("1. Add Item to Inventory")
        print("2. View Inventory")
        print("3. View Last Inserted ID")
        print("4. Remove Item by Index")
        print("5. View Purchase History")
        print("6. Exit Admin Panel")
        
        admin_choice = int(input("Enter your choice: "))
        
        if admin_choice == 1:
            add_item()
        elif admin_choice == 2:
            view_inventory()
        elif admin_choice == 3:
            view_last_id()
            if last_id is not None:
                print(f"The last inserted ID is: {last_id}")
            else:
                print("No items have been inserted yet.")
        elif admin_choice == 4:
            remove_item()
        elif admin_choice == 5:
            view_purchase_history()
        elif admin_choice == 6:
            print("Exiting Admin Panel.")
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
            if last_id is not None:
                print(f"The last inserted ID is: {last_id}")
            else:
                print("No items have been inserted yet.")
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
        item_id, brand_name, cloth_type, MRP, Discount, Material, Color, Size, Season, StockQuantity = row
        print(f"ID: {item_id}, Brand: {brand_name}, Type: {cloth_type}, Price: {MRP}, Discount(%): {Discount}, Material: {Material}, Colour: {Color}, Size: {Size}, Season: {Season} Stocks Remaining: {StockQuantity}")
        print()
        
        
        
        
def exit_program():
    print("Exiting the program.")
    mydb.close()
    exit()

def remove_item():
    print("Removing an item from the inventory:")
    
    last_id = view_last_id()
    id_to_remove = input(f"Enter the ID of the item to remove (default~last ID ={last_id}): ")
    
    if id_to_remove == '':
        id_to_remove = last_id
    else:
        id_to_remove = int(id_to_remove)
    
    if id_to_remove is not None:
        sql = "DELETE FROM clothes_info WHERE id = %s"
        val = (id_to_remove, )
        
        mycursor.execute(sql, val)
        mydb.commit()
        
        print("Item removed successfully!")
    else:
        print("No items to remove.")



def admin_panel():
    while True:
        print("\nAdmin Panel: ")
        print("1. Add Item to Inventory: ")
        print("2. View Inventory: ")
        print("3. View Last Inserted ID: ")
        print("4. Remove Item by Index: ")
        print("5. Exit Admin Panel: ")
        
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

def display_items():
    # Execute a query to retrieve all items
    query = "SELECT id, brand_name, cloth_type, MRP FROM clothes_info"
    mycursor.execute(query)

    # Print the items
    print("Available items:")
    for row in mycursor.fetchall():
        item_id, brand_name, cloth_type, mrp = row
        print(f"ID: {item_id}, Brand: {brand_name}, Type: {cloth_type}, Price: {mrp}")
    print()
    

def buy_items():
    global selected_items

    while True:
        item_id = input("Enter the ID of the item to buy (or 'q' to quit): ")
        
        if item_id == 'q':
            break
        
        quantity = int(input("Enter the quantity: "))
        selected_items.append((int(item_id), quantity))
        update_stock_quantity(int(item_id), quantity)
        write_purchase_history(int(item_id), quantity)
        preview_bought_items([(int(item_id), quantity)])  # Preview the added item
    
    return selected_items

def preview_bought_items(items):
    for item in items:
        item_id, quantity = item
        mycursor.execute("SELECT id, brand_name, cloth_type, MRP FROM clothes_info WHERE id = %s", (item_id,))
        row = mycursor.fetchone()
        if row:
            item_id, brand_name, cloth_type, mrp = row
            print(f"ID: {item_id}, Brand: {brand_name}, Type: {cloth_type}, Price: {mrp}, Quantity: {quantity}")
        else:
            print("No items bought")



def calculate_bill(items):
    # Create a dictionary to store the item details
    item_details = {}

    # Calculate the total bill amount and money saved
    total_amount = 0
    total_saved = 0
    total_items = 0

    for item in items:
        item_id, quantity = item
        mycursor.execute("SELECT id, brand_name, cloth_type, MRP, Discount FROM clothes_info WHERE id = %s", (item_id,))
        row = mycursor.fetchone()
        if row:
            item_id, brand_name, cloth_type, mrp, discount = row
            discounted_price = mrp - (mrp * discount / 100)
            total_amount += discounted_price * quantity
            total_saved += (mrp - discounted_price) * quantity
            total_items += quantity

            # Group the same items together
            if item_id in item_details:
                item_details[item_id]['quantity'] += quantity
            else:
                item_details[item_id] = {'brand_name': brand_name, 'cloth_type': cloth_type, 'price': discounted_price, 'quantity': quantity}

    # Print the bought items
    print("Bought items:")
    for item_id, details in item_details.items():
        print(f"ID: {item_id}, Brand: {details['brand_name']}, Type: {details['cloth_type']}, Price: {details['price']}, Quantity: {details['quantity']}")

    # Print the total money saved
    print(f"Total money saved: {total_saved}")

    # Print the total number of items bought
    print(f"Total number of items bought: {total_items}")

    return total_amount

selected_items=[]
def bill_calc():
    global selected_items 

    while True:
        print()
        print("1. Display available items")
        print("2. Buy items")
        print("3. Preview bought items")
        print("4. Calculate bill")
        print("5. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_items()
        elif choice == '2':
            selected_items = buy_items()
        elif choice == '3':
            if selected_items:
                preview_bought_items(selected_items)
            else:
                print("No items have been bought yet.")
        elif choice == '4':
            if selected_items:
                total_bill = calculate_bill(selected_items)
                print(f"The total bill amount is: {total_bill}")
            else:
                print("No items have been bought yet.")
        elif choice == '5':
            selected_items = []
            break
        else:
            print("Invalid choice. Please try again.")

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