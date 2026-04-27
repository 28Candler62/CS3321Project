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

def patron_add_list_item():
    patron_id = int(patron.get_id(input("Enter your last name: "))[0])
    stores = inventory.get_stores()
    
    if len(stores) == 0:
        print("\nNo Stores Found.")
        input("Press Enter to Continue")
        return
    
    print(
        "\nStore List\n"
        f"{"-" * 90}\n"
        f"{'Store ID':<10} {'Store Name':<20}\n"
        f"{"-" * 90}"
    )
    
    for store in stores:    
        inv_store_id = store[0]
        inv_store_name = store[1]
        
        print(
            f"{inv_store_id:<10} "
            f"{inv_store_name:<20} "
        )
        
    store_id = int(input("Enter Store ID: "))
    
    view_store_inventory(store_id)
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

def patron_receive_items():
    patron_info = patron.get_id(input("Enter your last name: "))

    if patron_info is None:
        print("\nPatron not found.")
        input("Press Enter to Continue")
        return

    patron_id = int(patron_info[0])
    received_items = s_list.view_received_items(patron_id)

    if len(received_items) == 0:
        print("\nNo checked-out items are ready to receive.")
        input("Press Enter to Continue")
        return

    print("\nItems Ready to Receive")
    print("-" * 120)
    print(f"{'Cart ID':<8} {'List ID':<8} {'Item':<20} {'Store':<15} {'Qty':<5} {'Price':<10} {'Line Total':<12} {'Shopper':<20}")
    print("-" * 120)

    valid_list_ids = []

    for item in received_items:
        cart_item_id = item[0]
        list_item_id = item[1]
        item_name = item[2]
        store_name = item[4]
        quantity = item[5]
        price = float(item[6])
        line_total = float(item[7])
        shopper_name = item[8] + " " + item[9]

        valid_list_ids.append(list_item_id)

        print(
            f"{cart_item_id:<8} "
            f"{list_item_id:<8} "
            f"{item_name:<20} "
            f"{store_name:<15} "
            f"{quantity:<5} "
            f"${price:<9.2f} "
            f"${line_total:<11.2f} "
            f"{shopper_name:<20}"
        )

    print("-" * 120)

    print("\n1: Receive one item")
    print("2: Receive all items")
    print("3: Cancel")

    choice = int(input("Please Select to Proceed: "))

    if choice == 1:
        list_item_id = int(input("Enter the List ID of the item received: "))

        if list_item_id not in valid_list_ids:
            print("\nThat List ID is not ready to receive.")
            input("Press Enter to Continue")
            return

        rows_removed = s_list.receive_item(patron_id, list_item_id)

        if rows_removed > 0:
            print("\nItem received and removed from shopping list.")
        else:
            print("\nItem could not be received.")

    elif choice == 2:
        rows_removed = s_list.receive_all_items(patron_id)
        print(f"\n{rows_removed} item(s) received and removed from shopping list.")

    elif choice == 3:
        print("\nReceive items cancelled.")

    else:
        print("\nInvalid option.")

    input("Press Enter to Continue")

def patron_update_info():
    fname = input("Enter your first name: ")
    lname = input("Enter your lastname: ")
    patron.addinfo(fname, lname)
    
def patron_menu():
    exit = 0
    while (exit != 6):
        os.system('cls')
        print(
            f'\nPatron Menu\n'
            f'{"-" * 90}\n'
            f'1: Update Info\n'
            f'2: Add to Shopping List\n'
            f'3: View Shopping List\n'
            f'4: Receive Items\n'
            f'5: Exit\n'
            f'{"-" * 90}\n'
        )
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
                patron_receive_items()
            case 6:
                exit = 6

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
            f"{sl_item_id:<14} "
            f"{patron_fname:<20} "
            f"{patron_lname:<20} "
        )
    print("-" * 90)
    input("Press Enter to Continue")
    
def shopper_menu():
    exit = 0
    while (exit != 4):
        os.system('cls')
        print(
            f'\nShopper Menu\n'
            f'{"-" * 90}\n'
            f'1: Update Info\n'
            f'2: Shop\n'
            f'3: View Cart\n'
            f'4: Exit\n'
            f'{"-" * 90}\n'
        )
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
    
def view_store_inventory(store_id:int=None):
    items = inventory.get_store_inventory(store_id)

    if len(items) == 0:
        print("\nNo Items in Store Inventory.")
        input("Press Enter to Continue")
        return

    print("\nStore Inventory")
    print("-" * 90)
    print(f"{'Item ID':<10} {'Name':<20} {'Description':<20} {'Qty':<5} {'Price':<10}")
    print("-" * 90)

    for item in items:
        inventory_id = item[0]
        item_name = item[1]
        description = item[2]
        quantity = item[3]
        price = float(item[4])

        print(
            f"{inventory_id:<10} "
            f"{item_name:<20} "
            f"{description:<20} "
            f"{quantity:<5} "
            f"${price:<10.2f} "
        )

    print("-" * 90)
    
def store_view_inventory():
    store_id = int(store.get_id(input("Enter store name: "))[0])
    
    view_store_inventory(store_id)
    input("Press Enter to Continue")
    
def store_menu():
    exit = 0
    while (exit != 4):
        os.system('cls')
        print(
            f'\nStore Menu\n'
            f'{"-" * 90}\n'
            f'1: Update Info\n'
            f'2: Update Inventory\n'
            f'3: View Inventory\n'
            f'4: Exit\n'
            f'{"-" * 90}\n'
        )
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
        print(
            f'\nWelcome to Personal Shopper\n'
            f'{"-" * 90}\n'
            f'1: Patron\n'
            f'2: Shopper\n'
            f'3: Store\n'
            f'4: Exit\n'
            f'{"-" * 90}\n'
        )
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