def load_parts(textfile):   ##Establishes where the parts file is
    parts_file = open(textfile, 'r')
    parts = parts_file.readlines()
    parts_file.close()
    return parts
 
def load_products(textfile):    ##Establishes where the product file is
    products_file = open(textfile, 'r')
    products = products_file.readlines()
    products_file.close()
    return products
 
parts_data = load_parts('parts.txt') #Don't know what this does but it works
products_data = load_products('products.txt')
 
partNames = {} ##Establishes the dictionaries of the part & product names
 
partPrices = {}
 
productNames = {}
 
productParts = {}
 
 
for line in parts_data: ##Handles queries regarding parts data & strips the unnecessary information
    splitted_line = line.split(',')
    if len(splitted_line) == 1:
        continue
    ID = splitted_line[0].strip()
    Name = splitted_line[1].strip()
    Price = splitted_line[2].strip()
     
    partNames[ID] = Name
    partPrices[ID] = Price
 
 
 
for line in products_data:          ##Copied from above to handle the product queries & strips unnecessary info.  
    splitted_line = line.split(',') ##This isn't quite finished, need help with this
    if len(splitted_line) == 1:
        continue
    ID = splitted_line[0].strip()
    Name = splitted_line[1].strip()
    Price = splitted_line[2].strip()
     
    productNames[ID] = Name
    productParts[ID] = Price
     
##Below I pulled from an example my teacher gave me but I still need to apply it to this program, need help ##with this
 
##for x in parts_data:
##     print(x)
##     print('-------------------------------')
##
##run = True
##
##while run:
##    command = input("Please give a command\n")
##    
##    if command[0] == 'a':
##        command = command.split(' ')
##        print("Command recieved: " + command[0])
##        print("Searching for: " + command[1])
##        
##    if command[0] == 'b':
##        print("Execute order 66")

