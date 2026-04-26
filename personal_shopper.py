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
4: Receive Items
5: Exit
"""

_shopper_menu = """
Shopper Menu

1: Update Info
2: Shop
3: View Cart
4: Exit
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
    
def view_shopping_list(patron_id:int, store_id:int=None):
    items = s_list.view_list(patron_id, store_id)

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
    return items

    
def patron_view_shopping_list():
    patron_info = patron.get_id(input("Enter your last name: "))

    if patron_info is None:
        print("\nPatron not found.")
        input("Press Enter to Continue")
        return

    patron_id = int(patron_info[0])
    
    view_shopping_list(patron_id)

    input("\nPress Enter to Continue")
    
def patron_update_info():
    fname = input("Enter your first name: ")
    lname = input("Enter your lastname: ")
    patron.addinfo(fname, lname)
    

def patron_menu():
    exit = 0
    while (exit != 5):
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
                exit = 5
            case 5:
                exit = 5

def shopper_shop():
    shopper_id = int(shopper.get_id(input("Enter your last name: "))[0])
    
    if shopper_id is None:
        print("\nShopper not found.")
        input("Press Enter to Continue")
        return
        
    stores = s_list.view_list_stores()
    print("\nAvailable Stores")
    print("-" * 90)
    print(f"{'Store ID':<10} {'Store':<20}")
    print("-" * 90)
     
    for store in stores:
        sl_store_id = store[0]
        sl_store_name = store[1]
        print(
            f"{sl_store_id:<10} "
            f"{sl_store_name:<20} "
        )
    print("-" * 90)
    store_id = int(input("Enter Store ID to shop: "))
    
    patrons = s_list.view_list_patrons(store_id)
    print("\nAvailable Patrons")
    print("-" * 90)
    print(f"{'Patron ID':<10} {'First Name':<20} {'Last Name':<20}")
    print("-" * 90)
    for patron in patrons:
        sl_patron_id = patron[0]
        sl_patron_fname = patron[1]
        sl_patron_lname = patron[2]
        print(
            f"{sl_patron_id:<10} "
            f"{sl_patron_fname:<20} "
            f"{sl_patron_lname:<20} "
        )
    print("-" * 90)
    patron_id = int(input("Enter Patron ID to shop for: "))
    
    sl_items = view_shopping_list(patron_id, store_id)
    input("Press Enter to ADD ITEMS TO CART AND CHECKOUT")
    
    for item in sl_items:
        sl_item_id = item[0]
        
        cart.add_item(sl_item_id, shopper_id)
        
    print('Items added to Cart and Checkout complete')
    input("Press Enter to Continue")
    
def shopper_view_cart():
    shopper_id = int(shopper.get_id(input("Enter your last name: "))[0])
    
    if shopper_id is None:
        print("\nShopper not found.")
        input("Press Enter to Continue")
        return
    
    cart_items = cart.view_cart(shopper_id)
    print("\nShopping Cart")
    print("-" * 90)
    print(f"{'Cart Item ID':<14} {'List Item ID':<14} {'Patron First Name':<20} {'Patron Last Name':<20}")
    print("-" * 90)
    for item in cart_items:
        sc_item_id = item[0]
        sl_item_id = item[1]
        patron_fname = item[2]
        patron_lname = item[3]
        print(
            f"{sc_item_id:<14} "
            f"{sc_item_id:<14} "
            f"{patron_fname:<20} "
            f"{patron_lname:<20} "
        )
    print("-" * 90)
    input("Press Enter to Continue")
    
def shopper_menu():
    exit = 0
    while (exit != 4):
        os.system('cls')
        print(_shopper_menu)
        menu = int(input('Please Select to Procede: '))
    
        match menu:
            case 1:
                exit=4
            case 2:
                shopper_shop()
            case 3:
                shopper_view_cart()
            case 4:
                exit = 4
                
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