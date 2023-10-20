import csv

def view_purchase_history():
    try: 
        with open('purchase_history.csv', 'r') as file:
            reader = csv.reader(file)
            print("History Content Of the File")
            for row in reader:
                print('Item ID: ', row[0], ', Brand Name: ', row[1], ', Cloth Type: ', row[2], ', Quantity: ', row[3], ', Total Price: ', row[4], ', Date: ', row[5])
    except:
        print("No Items in history")
        
view_purchase_history()