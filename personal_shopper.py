from db import AppDataBase
from manage_patron import Patron
from manage_shopper import Shopper
from manage_store import Store
from manage_list import Shoppinglist
from manage_cart import Cart
from manage_inventory import Inventory
import os

db = AppDataBase()
patron = Patron(db)
shopper = Shopper(db)
store = Store(db)
s_list = Shoppinglist(db)
inventory = Inventory(db)
cart = Cart(db)

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
3: View Shopping List
4: Remove Item From Shopping List
5: Receive Items
6: Exit
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
3: View Inventory
4: Exit
"""
def patron_add_list_item():
    patron_id = int(patron.get_id(input("Enter your last name: "))[0])
    
    print('Store ID \t Store Name')
    [print(f'{x[0]}\t\t{x[1]}') for x in inventory.get_stores()]
    store_id = int(input("Enter Store ID: "))
    
    print('Item ID \t Name \t Description \tQuantity \t Price')
    [print(f'{x[0]}\t\t{x[1]}\t{x[2]}\t{x[3]}\t{x[4]}') for x in inventory.get_items(store_id)]
    item_id = int(input("Enter Item ID to add to Shopping list: "))
    qty = int(input("Enter Quantity: "))
    
    s_list.add_item(item_id, patron_id, qty)
    
def patron_view_shopping_list():
    patron_info = patron.get_id(input("Enter your last name: "))

    if patron_info is None:
        print("\nPatron not found.")
        input("Press Enter to Continue")
        return

    patron_id = int(patron_info[0])
    items = s_list.view_list(patron_id)

    if len(items) == 0:
        print("\nYour shopping list is empty.")
        input("Press Enter to Continue")
        return

    print("\nShopping List")
    print("-" * 90)
    print(f"{'List ID':<8} {'Item':<20} {'Store':<15} {'Qty':<5} {'Price':<10} {'Line Total':<10}")
    print("-" * 90)

    for item in items:
        list_item_id = item[0]
        item_name = item[2]
        store_name = item[4]
        quantity = item[5]
        price = float(item[6])
        line_total = float(item[7])

        print(
            f"{list_item_id:<8} "
            f"{item_name:<20} "
            f"{store_name:<15} "
            f"{quantity:<5} "
            f"${price:<9.2f} "
            f"${line_total:<9.2f}"
        )

    print("-" * 90)

    total = float(s_list.calculate_total(patron_id))
    print(f"{'Shopping List Total:':>61} ${total:.2f}")

    input("\nPress Enter to Continue")

def patron_remove_list_item():
    patron_info = patron.get_id(input("Enter your last name: "))

    if patron_info is None:
        print("\nPatron not found.")
        input("Press Enter to Continue")
        return

    patron_id = int(patron_info[0])
    items = s_list.view_list(patron_id)

    if len(items) == 0:
        print("\nYour shopping list is empty.")
        input("Press Enter to Continue")
        return

    print("\nShopping List")
    print("-" * 90)
    print(f"{'List ID':<8} {'Item':<20} {'Store':<15} {'Qty':<5} {'Price':<10} {'Line Total':<10}")
    print("-" * 90)

    valid_list_ids = []

    for item in items:
        list_item_id = item[0]
        item_name = item[2]
        store_name = item[4]
        quantity = item[5]
        price = float(item[6])
        line_total = float(item[7])

        valid_list_ids.append(list_item_id)

        print(
            f"{list_item_id:<8} "
            f"{item_name:<20} "
            f"{store_name:<15} "
            f"{quantity:<5} "
            f"${price:<9.2f} "
            f"${line_total:<9.2f}"
        )

    print("-" * 90)

    list_item_id = int(input("Enter the List ID of the item you want to remove: "))

    if list_item_id not in valid_list_ids:
        print("\nThat List ID is not in your shopping list.")
        input("Press Enter to Continue")
        return

    rows_removed = s_list.remove_item(list_item_id)

    if rows_removed > 0:
        print("\nItem removed from shopping list.")
    else:
        print("\nItem could not be removed.")

    input("Press Enter to Continue")

def patron_update_info():
    fname = input("Enter your first name: ")
    lname = input("Enter your lastname: ")
    patron.addinfo(fname, lname)
    

def patron_menu():
    exit = 0
    while (exit != 6):
        os.system('cls')
        print(_patron_menu)
        menu = int(input('Please Select to Procede: '))
    
        match menu:
            case 1:
                patron_update_info()
            case 2:
                patron_add_list_item()
            case 3:
                patron_view_shopping_list()
            case 4:
                patron_remove_list_item()
            case 5:
                print("Receive Items is not ready yet.")
                input("Press Enter to Continue")
            case 6:
                exit = 6

def shopper_shop():
    store_id = 0
    
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
                
def store_add_inventory_item():
    store_id = int(store.get_id(input("Enter store name: "))[0])
    item_name = input("Enter item name: ")
    item_desc = input("Enter item description: ")
    qty = int(input("Enter Quantity: "))
    price = float(input("Enter Price: $"))
    
    inventory.add_item(item_name, item_desc, store_id, qty, price)
    
def store_view_inventory():
    store_id = int(store.get_id(input("Enter store name: "))[0])
    
    print('Item ID \t Name \t Description \tQuantity \t Price')
    [print(f'{x[0]}\t\t{x[1]}\t{x[2]}\t{x[3]}\t{x[4]}') for x in inventory.get_items(store_id)]
    input("Press Enter to Continue")
    
def store_menu():
    exit = 0
    while (exit != 4):
        os.system('cls')
        print(_store_menu)
        menu = int(input('Please Select to Procede: '))
    
        match menu:
            case 1:
                exit=4
            case 2:
                store_add_inventory_item()
            case 3:
                store_view_inventory()
            case 4:
                exit = 4   

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