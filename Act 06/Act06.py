class Item:
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price
    
    def __str__(self):
        return f"{self.item_id:<6} | {self.name:<25} | {self.description:<50} | PHP {self.price:>6.2f}"

class ItemManagement:
    def __init__(self):
        self.items = {
            "000001": Item("000001", "Okin-UwU", "Okinawa milk tea with a twist of caramel", 130),
            "000002": Item("000002", "WinterMhieLon", "Wintermelon milk tea with a rich creamy taste", 115),
            "000003": Item("000003", "Cheesecake Taro, Pare!", "Taro milk tea topped with cheesecake foam", 135),
            "000004": Item("000004", "Matcha-Yuh! Tayo", "Authentic Japanese matcha milk tea", 125),
            "000005": Item("000005", "Thai Yo Nalang", "Traditional Thai milk tea with a strong flavor", 120),
        }
    
    def view_items(self):
        if not self.items:
            print("No items available.")
            return
        print("=" * 100)
        print(f"{'ID':<6} | {'Name':<25} | {'Description':<50} | {'Price'}")
        print("=" * 100)
        for item in self.items.values():
            print(item)
        print("=" * 100)
    
    def add_item(self, item_id, name, description, price):
        if item_id in self.items:
            print("Error: Item ID already exists.")
            return
        
        try:
            if len(item_id) != 6 or not item_id.isdigit():
                raise ValueError("Item ID must be a 6-digit number.")
            price = float(price)
            if price <= 0:
                raise ValueError("Price must be a positive number.")
            self.items[item_id] = Item(item_id, name, description, price)
            print("Item added successfully!")
        except ValueError as e:
            print("Error:", e)
    
    def update_item(self, item_id, name=None, description=None, price=None):
        if item_id not in self.items:
            print("Error: Item ID not found.")
            return
        
        if name:
            self.items[item_id].name = name
        if description:
            self.items[item_id].description = description
        if price:
            try:
                price = float(price)
                if price <= 0:
                    raise ValueError("Price must be a positive number.")
                self.items[item_id].price = price
            except ValueError as e:
                print("Error:", e)
                return
        
        print("Item updated successfully!")
    
    def delete_item(self, item_id):
        if item_id not in self.items:
            print("Error: Item ID not found.")
            return
        del self.items[item_id]
        print("Item deleted successfully!")

def main():
    manager = ItemManagement()
    while True:
        print("=" * 40)
        print("\tICTea Management System")
        print("=" * 40)
        print("1. Add Item")
        print("2. View Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")
        print("=" * 40)
        choice = input("\nEnter your choice: ")

        if choice == "1":
            item_id = input("Enter 6-digit item ID: ")
            name = input("Enter item name: ")
            description = input("Enter item description: ")
            price = input("Enter item price: ")
            print("=" * 40)
            manager.add_item(item_id, name, description, price)
        elif choice == "2":
            manager.view_items()
        elif choice == "3":
            item_id = input("Enter item ID to update: ")
            name = input("Enter new name (press enter to skip): ")
            description = input("Enter new description (press enter to skip): ")
            price = input("Enter new price (press enter to skip): ")
            print("=" * 40)
            manager.update_item(item_id, name or None, description or None, price or None)
        elif choice == "4":
            item_id = input("Enter item ID to delete: ")
            print("=" * 40)
            manager.delete_item(item_id)
        elif choice == "5":
            print("Exiting... Thank you for using our program!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()