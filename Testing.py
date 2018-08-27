import csv, time

with open('parts.txt', 'r') as f:
    fieldnames = ('PartID', 'Partname', 'PartCost')
    parts = list(csv.DictReader(f.readlines(), fieldnames=fieldnames, skipinitialspace=True))

with open('products.txt', 'r') as d:
    fieldnames = ('BikeID', 'BikeName')
    products = list(csv.DictReader(d.readlines(),
                                   fieldnames=fieldnames,
                                   restkey='BikeParts',
                                   skipinitialspace=True))

def get_name(ID):
    try:
        if ID.startswith('bike'):
            for row in products:
                if row['BikeID'] == ID:
                    name = row['BikeName']

        else:
            for row in parts:
                if row['PartID'] == ID:
                    name = row['Partname']
        return name
    except UnboundLocalError:
        return 'Invalid Name'

def get_ID(NAME):
    try:
        if NAME.endswith('Bike'):
            for row in products:
                if row['BikeName'] == NAME:
                    id = row['BikeID']

        else:
            for row in parts:
                if row['Partname'] == NAME:
                    id = row['PartID']
        return id
    except UnboundLocalError:
        return 'Invalid ID'

def get_price(ID):
    try:
        for row in parts:
                if row['PartID'] == ID:
                    cost = row['PartCost']

        else:
            for row in products:
                if row['BikeID'] == ID:
                    cost = 0
                    for item in row['BikeParts']:
                        part_id, qty = item.split(':')
                        for row in parts:
                            if part_id == row['PartID']:
                                cost += int(row['PartCost']) * int(qty)

        return cost
    except UnboundLocalError:
        return 'Invalid ID'

def get_parts(ID):
    try:
        if row ['BikeID'] == ID:
            cost = 0
            for row in products:
                if item in row['BikeParts']:
                    part_id, qty = item.split(':')
                    for row in parts:
                        if part_id == row['PartID']:
                            cost += int(row['PartCost'] * int(qty))

run = True

while run:
    command1 = input("Are you looking for a Part or a Product?\n")
    try:
        if command1 == 'Product':
            response1 = input("Do you know the ID of the product? Yes/No\n")
            if response1 == "Yes":
                command2 = input("What is the ID of the product you're looking for?\n")
                time.sleep(0.3)
                print(" ")
                print(" ")
                print("############################")
                print("## This is a", get_name(command2))
                print("## It costs", get_price(command2), 'cents')
                print("############################")
                print(" ")
                print(" ")
                continue
            else:
                response2 = input("What is the name of the product?\n")
                time.sleep(0.3)
                productID = get_ID(response2)
                print("The item ID you're for is:", productID)
                time.sleep(0.3)
                print("It costs:", get_price(productID))
                print(" ")
                continue



        if command1 == 'Part':
            command2 = input("Do you know the ID of the product you're looking for?\n")
            if command2 == "No":
                command3 = input("What is the name of the part?\n")
                response3 = get_ID(command3)
                print("The ID of the part you're looking for is:", response3)
                print("It costs:", get_price(response3))
                print(" ")
                continue

            command4 = input("What is the ID of the product you're looking for?\n")
            time.sleep(0.3)
            print(" ")
            print(" ")
            print("############################")
            print("## This is a", get_name(command4))
            print("## It costs", get_price(command4), 'cents')
            print(" ")
            print(" To build this", get_name(command4), "you will need: ")
            print("############################")
            print(" ")
            print(" ")
            continue
        else:
            break
    except UnboundLocalError:
        break
