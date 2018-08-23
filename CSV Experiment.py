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
                if row['PartCost'] == ID:
                    name = row['PartCost']
        return name
    except UnboundLocalError:
        return 'Invalid ID'

def get_id(NAME):
    try:
        if NAME.startswith('bike'):
            for row in products:
                if row['BikeName'] == NAME:
                    name = row['BikeID']
        else:
            for row in parts:
                if row['Partname'] == ID:
                    name = row['PartID']
                    
        return name
    except UnboundLocalError:
        return 'Invalid ID'
    
def get_parts_price(ID):
    try: 
        if ID.startswith('bike'):
            for row in products:
                if row['BikeID'] == ID:
                    name = row['BikePrice']
        else:
            return 'Invalid ID'
                   
        return name
    except UnboundLocalError:
        return 'Invalid ID'

def parts_cost(bike_id):
    try:
        for row in products:
            if row['BikeID'] == bike_id:
                cost = 0
                for item in row['BikeParts']:
                    part_id, qty = item.split(':')
                    for row in parts:
                        if part_id == row['PartID']:
                            cost += int(row['PartCost']) * int(qty)
        return cost
    except UnboundLocalError:
        return 'Invalid ID'
   


run = True

while run:
    command1 = input("Are you looking for a Part or a Product?\n")
    
    if command1 == 'Product':
        command2 = input("What is the ID of the product you're looking for?\n")
        time.sleep(0.3)
        print(" ")
        print(" ")
        print("############################")
        print("## This is a", get_name(command2))
        print("## It costs", parts_cost(command2), 'cents')
        print("############################")
        print(" ")
        print(" ")
        response = input("Are you looking for another part? Yes/No.\n")
        if response == ("No"):
            run = False
        else:
            continue
            
        
    if command1 == 'Part':
        command2 = input("What is the ID of the product you're looking for?\n")
        time.sleep(0.3)
        print(" ")
        print(" ")
        print("############################")
        print("## This is a", get_name(command2))
        print("## It costs", get_parts_price(command2), 'cents')
        print("############################")
        print(" ")
        print(" ")
        response = input("Are you looking for another part? Yes/No\n")
        if response == ("No"):
            run = False
        else:
            continue
