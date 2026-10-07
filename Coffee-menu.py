import json 
import os
import datetime
import time
import sys
# --------------------------------------------
# === slow print FUNCTION ===
def slow_print(text, delay=0.07):
    """Prints the text character by character with a delay."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()  # Immediately write to the output
        time.sleep(delay)  # Delay between characters
    print()  # Print a newline at the end

# --------------------------------------------
today = datetime.datetime.today()

FILE = "orders.json"

total = 0
orders = []
# --------------Menu List----------------------
menu = {
    "1": ("Espresso", 2.50),
    "2": ("Latte", 3.50),
    "3": ("Cappuccino", 3.00),
    "4": ("Americano", 2.00)
}
# --------------------------------------------
slow_print("Welcome to our coffee shop.", delay=0.07)
print(f"Date: ,{today:%Y,%m,%d}", "\n")
print("=" * 10, "Coffee Menu", "=" * 10)

def save_data(data): # Saving data into json file
    with open(FILE, "w") as f:
        json.dump(orders, f, indent=4)


def load_data(): # Loading data from json file.
    if not os.path.exists(FILE) or os.path.getsize(FILE) == 0:
        return [] 

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)


orders = load_data()

while True: # Project Main loop.
        try:
            for number, item in menu.items():
                name, price = item
                print(f"{number}. {name} - ${price:.2f}")

            print("5. View Order")
            print("6. Checkout")
            print("7. Exit")
            print("=" * 33)

            option = input("Choose an option: ").strip()
            print("\n")

            if option in menu: # Checking if option in menu store name and price then add it and
                name, price = menu[option]
                orders.append((name, price))
                save_data(orders)
                slow_print(f"{name} added to your orders.\n", delay=0.07)

            elif option == "5":
                if not orders:
                    slow_print("- There are no orders yet.\n", delay=0.07)
                    
                else:
                    slow_print("\nYour orders: \n", delay=0.07)

                    for item, price in orders:
                        slow_print(f"- {item}: ${price:.2f}\n", delay=0.07)
                        print("*" * 40)

            elif option == "6":
                if not orders:
                    slow_print("- Your order is empty. Please add items before checkout.\n", delay=0.07)
                else:
                    total = sum(price for item, price in orders)
                    slow_print("Proceeding to checkout...", delay=0.18)
                    slow_print("\nYour checkout: ", delay=0.07)
                    for item , price in orders:
                        slow_print(f"- {item}: ${price:.2f}",  delay=0.07)
                        with open("orders.json", "w") as file: # Create or overwrite orders.json with an empty list.
                            json.dump([], file, indent=2)
                    slow_print(f"Total: ${total:.2f}", delay=0.07)
                    slow_print("Thank you for your orders!", delay=0.07)
                    
                    break
            
            elif option == "7":
                slow_print("Thank you for visiting!", delay=0.07)
                break

            else:
                slow_print("\nYour option does not exist. Please try again.", delay=0.07)

        except:
            slow_print("\nYour option does not exist. Please try again.", delay=0.07)

