from db import AppDataBase
#from manage_patron import Patron
#from manage_shopper import Shopper
#from manage_store import Store
#from manage_list import Shoppinglist
#from manage_cart import Cart
#from manage_inventory import Inventory
import os

db = AppDataBase()
#p1 = People(db)

_main_menu = """
Welcome to Personal Shopper

1: Patron
2: Shopper
3: Store
4: Exit
"""
_patron_menu = """
Patron Menu

1: Update Info
2: Add to Shopping List
3: Receive Items
4: Exit
"""

_shopper_menu = """
Shopper Menu

1: Update Info
2: Shop
3: Exit
"""

_store_menu = """
Store Menu

1: Update Info
2: Update Inventory
3: Exit
"""

def patron_update_info():
    fname = input("Enter your first name: ")
    lname = input("Enter your lastname: ")

def patron_menu():
    exit = 0
    while (exit != 4):
        os.system('cls')
        print(_patron_menu)
        menu = int(input('Please Select to Procede: '))
    
        match menu:
            case 1:
                exit = 4
            case 2:
                exit = 4
            case 3:
                exit = 4
            case 4:
                exit = 4

def shopper_menu():
    exit = 0
    while (exit != 3):
        os.system('cls')
        print(_shopper_menu)
        menu = int(input('Please Select to Procede: '))
    
        match menu:
            case 1:
                exit=3
            case 2:
                exit=3
            case 3:
                exit = 3
                
def store_menu():
    exit = 0
    while (exit != 3):
        os.system('cls')
        print(_store_menu)
        menu = int(input('Please Select to Procede: '))
    
        match menu:
            case 1:
                exit=3
            case 2:
                exit=3
            case 3:
                exit = 3     

def main_menu():
    exit = 0
    while (exit != 4):
        os.system('cls')
        print(_main_menu)
        menu = int(input('Please Select to Procede: '))
        exit_while = menu
        
        match menu:
            case 1: 
                patron_menu()
            case 2:
                shopper_menu()
            case 3:
                store_menu()
            case 4:
                exit = 4

if __name__ == "__main__":
    main_menu()

    print('Good Bye')
"""
#p1.addinfo()

res=db.execute("SELECT * FROM customer")
print(res.fetchall())

res= db.execute('SELECT StoreID, StoreName FROM store')
print('Store ID \t Store Name')
[print(f'{x[0]}\t\t{x[1]}') for x in res.fetchall()]

res = db.execute('SELECT CustomerID, CustomerFirstName, CustomerLastName FROM customer')
print('ID \t First \t Last')
[print(f'{x[0]}\t{x[1]}\t{x[2]}') for x in res.fetchall()]

customerID = input('Enter customer ID: ')
res = db.execute(f'SELECT * FROM customer WHERE CustomerID = {customerID}')
print(res.fetchall())

#print(p1.name)
#print(p1.age)
#print(p1.address)
#
#res = db.execute(
    #'''
    #SELECT * 
    #FROM shoppingcart sc 
    #JOIN shoppinglist sl ON sc.ShoppingListItem = sl.ListItemID
    #JOIN inventory i ON i.ItemID = sl.InventoryItem
    #JOIN customer c ON c.CustomerID = sl.Customer
    #JOIN shopper s ON s.ShopperID = sc.Shopper
    #JOIN store st ON i.ItemStore = st.StoreID;
    #'''
    #)
#print(res.fetchall())
#
# Execute query to get table names
#res = db.execute("SELECT name FROM sqlite_master WHERE type='table';")
# Print the list of tables
#print(res.fetchall())
"""