class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, price, quantity=1):
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'price': price, 'quantity': quantity}

    def remove_item(self, item_name, quantity=1):
        if item_name in self.items:
            if self.items[item_name]['quantity'] > quantity:
                self.items[item_name]['quantity'] -= quantity
            else:
                del self.items[item_name]
        else:
            print(f"Item '{item_name}' not found in the cart.")

    def calculate_total_price(self):
        total_price = sum(item['price'] * item['quantity'] for item in self.items.values())
        return total_price

    def display_cart(self):
        print("Shopping Cart Contents:")
        for item_name, item_details in self.items.items():
            print(f"{item_name} - Quantity: {item_details['quantity']}, Price: ${item_details['price']} each")

# User input to interactively use the ShoppingCart class
cart = ShoppingCart()

while True:
    print("\nOptions:")
    print("1. Add item to cart")
    print("2. Remove item from cart")
    print("3. Display cart")
    print("4. Calculate total price")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        item_name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        quantity = int(input("Enter quantity: "))
        cart.add_item(item_name, price, quantity)
    elif choice == '2':
        item_name = input("Enter item name to remove: ")
        quantity = int(input("Enter quantity to remove: "))
        cart.remove_item(item_name, quantity)
    elif choice == '3':
        cart.display_cart()
    elif choice == '4':
        total_price = cart.calculate_total_price()
        print(f"Total Price: ${total_price}")
    elif choice == '5':
        print("Exit!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")