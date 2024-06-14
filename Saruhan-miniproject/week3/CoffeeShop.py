import csv
import os
# Load data from a CSV file into a list of dictionaries
def load_csv_file(path, header):
    data = []
    try:
        with open(path, 'r', newline="") as file:
            reader = csv.DictReader(file, fieldnames=header)
            next(reader)  # Skip header row
            data = [dict(row) for row in reader]
    except Exception as e:
        print(e)
    return data

# Save data from a list of dictionaries to a CSV file
def save_data_to_csv(path, data, header):
    try:
        with open(path, 'w', newline="") as file:  # Use 'w' to overwrite the file
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
    except Exception as e:
        print(e)

# Headers for CSV files
couriers_header = ['name', 'phone']
product_header = ['Product name', 'Price']

# Load couriers and products from CSV files
couriers_list = load_csv_file('/Users/saruhanarac/Desktop/Generation/Saruhan-miniproject/couriers.csv', couriers_header)
my_product_list = load_csv_file('/Users/saruhanarac/Desktop/Generation/Saruhan-miniproject/products.csv', product_header)

# Square bracket is the list
# Curly Bracket is the Dictionary
# Inside the Dictionary we have a Key and value pairs, the first is the key, the second is the value.
# To access an element in a list, you need to use the index value. 
# If it's a dictionary, you need to access the value using the key.

# Sample orders
orderlist = [
    {
        "customer_name": "Denzel Washington",
        "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
        "customer_phone": "0001",
        "courier": 2,
        "status": "preparing",
        "items": "1,2,3,4"
    },
    {
        "customer_name": "James Bond",
        "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
        "customer_phone": "007",
        "courier": 2,
        "status": "preparing",
        "items": "5,3,1,1"
    }
]

# Order statuses
order_status_list = ["Out for delivery", "Pending", "Dispatched", "Delivered"]

# Initial menu options
menu_options = ['0 EXIT', '1 PRINT PRODUCT MENU OPTIONS']

# Printing the main menu options initially
print(menu_options)

while True:
    main_menu_input = input('''MAIN MENU OPTIONS: 
    0. EXIT   
    1. PRODUCTS MENU
    2. COURIERS MENU
    3. ORDERS MENU
    Choose an option: ''')
    
    if main_menu_input == '0':
        # Save data to CSV files before exiting
        save_data_to_csv('/Users/saruhanarac/Desktop/Generation/Saruhan-miniproject/couriers.csv', couriers_list, couriers_header)
        save_data_to_csv('/Users/saruhanarac/Desktop/Generation/Saruhan-miniproject/products.csv', my_product_list, product_header)
         
        #!/usr/local/bin/python3

        # Your Python script code here

        print("Running your project...")
        # Your remaining Python code

        # Clear the terminal
        
        os.system('clear')  # For Unix/Linux/macOS
        # For Windows, use 'cls' instead of 'clear'
        # os.system('cls')

        ('/usr/local/bin/python3 /Users/saruhanarac/Desktop/Generation/Saruhan-miniproject/week3/CoffeeShop.py')
        

        exit()
    
    elif main_menu_input == '1':
        os.system('clear')
        while True:
            product_menu_input = input('''
    0. RETURN TO MAIN MENU 
    1. PRINT PRODUCT LIST 
    2. CREATE NEW PRODUCT
    3. UPDATE PRODUCT 
    4. DELETE PRODUCT
    ''')

            if product_menu_input == '0':
                break
            
            elif product_menu_input == '1':
                os.system('clear')
                print(my_product_list)
            
            elif product_menu_input == '2':
                # Add new product
                os.system('clear')
                new_product_name = input('Enter new product name: ')
                new_product_price = input('Enter product price: ')
                new_product = {'Product name': new_product_name, 'Price': new_product_price}
                my_product_list.append(new_product)
                print(my_product_list)
            
            elif product_menu_input == '3':
                # Update an existing product
                for i in range(len(my_product_list)):
                    print(f'{i}: {my_product_list[i]}')
                
                user_input = int(input("Enter the index of the product you want to update: "))
                new_product_name = input("Enter the new product name: ")
                new_product_price = input("Enter the new product price: ")
                my_product_list[user_input] = {'Product name': new_product_name, 'Price': new_product_price}
                print(my_product_list)
                os.system('clear')
                
            elif product_menu_input == '4':
                os.system('clear')
                # Delete a product
                for i in range(len(my_product_list)):
                    print(f"{i}: {my_product_list[i]}")
                delete_index = int(input("Enter the index of the product you want to delete: "))
                
                if 0 <= delete_index < len(my_product_list):
                    my_product_list.pop(delete_index)
                    print(f"Updated product list: {my_product_list}")
                else:
                    print("Invalid index. Please try again.")
    
    elif main_menu_input == '2':
        os.system('clear')
        while True:
            print("0. RETURN TO MAIN MENU")
            print("1. COURIERS LIST")
            print("2. CREATE NEW COURIER")
            print("3. UPDATE EXISTING COURIER")
            print("4. DELETE COURIER")
            courier_menu_option = input('Choose courier menu option: ')
            
            if courier_menu_option == "0":
                os.system('clear')
                break
            elif courier_menu_option == "1":
                os.system('clear')
                print(couriers_list)
            elif courier_menu_option == '2':
                os.system('clear')
                # Add new courier
                new_courier_name = input('Enter new courier name: ')
                new_courier_phone = input('Enter new courier phone number: ')
                couriers_list.append({'name': new_courier_name, 'phone': new_courier_phone})
                print(couriers_list)
            elif courier_menu_option == '3':
                os.system('clear')
                # Update an existing courier
                for i in range(len(couriers_list)):
                    print(f'{i}: {couriers_list[i]}')
                
                update_existing_courier = int(input("Enter the index of the courier you want to update: "))
                new_courier_name = input("Enter the new name for the courier: ")
                new_courier_phone = input("Enter the new phone number for the courier: ")
                couriers_list[update_existing_courier] = {'name': new_courier_name, 'phone': new_courier_phone}
                print(f"Courier at index {update_existing_courier} has been updated to {new_courier_name}.")
                
                os.system('clear')
            
            elif courier_menu_option == '4':
                os.system('clear')
                # Delete a courier
                for i in range(len(couriers_list)):
                    print(f'{i}: {couriers_list[i]}')
                
                delete_index = int(input("Enter the index of the courier you want to delete: "))
                if 0 <= delete_index < len(couriers_list):
                    deleted_courier = couriers_list.pop(delete_index)
                    print(f"Courier '{deleted_courier['name']}' has been deleted.")
                    print(f"Updated couriers list: {couriers_list}")
                else:
                    print("Invalid index. Please try again.")
            else:
                print("Invalid option. Please try again.")
                os.system('clear')
                
    elif main_menu_input == '3':
        os.system('clear')
        while True:
            option = input('''ORDERS MENU OPTIONS: 
            0. RETURN TO MAIN MENU   
            1. TAKE ORDER
            2. VIEW ORDERS
            3. UPDATE ORDER STATUS
            ''')
            if option == '0':
                os.system('clear')
                break
            
            elif option == '1':
                os.system('clear')
                # Take a new order
                customer_name = input("Enter customer name: ")
                address = input("Enter customer address: ")
                phone_number = input("Enter customer phone number: ")
                courier = input('Choose a Courier: ')
                status = "preparing"
                items = input("Enter the items (separated by commas): ")
                new_order = {
                    "customer_name": customer_name,
                    "customer_address": address,
                    "customer_phone": phone_number, 
                    "courier": courier,
                    "status": status,
                    "items": items
                }
                orderlist.append(new_order)
            
            elif option == '2':
                os.system('clear')
                # View all orders
                print(orderlist)
            
            elif option == '3':
                os.system('clear')
                # Update an order status
                for i in range(len(orderlist)):
                    print(f'{i}: {orderlist[i]}')
                
                update_order_index = int(input("Enter the index of the order status you want to update: "))
                for i in range(len(order_status_list)):
                    print(f'{i}: {order_status_list[i]}')
                
                order_status_index_input = int(input("Enter the index of the new status: "))
                orderlist[update_order_index]['status'] = order_status_list[order_status_index_input]
                print(f"Order status updated to {order_status_list[order_status_index_input]}.")
    
    else:
        print("Invalid option. Please try again.")

# import pymysql
# import os
# from dotenv import load_dotenv
 
# load_dotenv()
# host_name = os.environ.get("mysql_host")
# database_name = os.environ.get("mysql_db")
# user_name = os.environ.get("mysql_user")
# user_password = os.environ.get("mysql_pass")