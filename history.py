import csv

def view_purchase_history():
    with open('purchase_history.csv', 'r') as file:
        reader = csv.reader(file)
        print("History Content Of the File")
        for row in reader:
            return ('Item ID: ', row[0], ', Quantity: ', row[1], ', Date: ', row[2])
view_purchase_history()