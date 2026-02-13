import json
import os
from datetime import datetime

def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] {func.__name__} executed at {datetime.now()}")
        return func(*args, **kwargs)
    return wrapper

class Product:
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def set_price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.__price = price

    def set_stock(self, stock):
        if stock < 0:
            raise ValueError("Stock cannot be negative")
        self.__stock = stock

    def get_details(self):
        return f"ID: {self.__product_id}, Name: {self.__name}, Price: {self.__price}, Stock: {self.__stock}"

    def to_dict(self):
        return {
            "type": "Product",
            "product_id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }



class Electronics(Product):
    def __init__(self, product_id, name, price, stock, warranty_years):
        super().__init__(product_id, name, price, stock)
        self.__warranty_years = warranty_years

    def get_details(self):  
        return super().get_details() + f", Warranty: {self.__warranty_years} years"

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Electronics"
        data["warranty_years"] = self.__warranty_years
        return data


class Grocery(Product):
    def __init__(self, product_id, name, price, stock, expiry_date):
        super().__init__(product_id, name, price, stock)
        self.__expiry_date = expiry_date

    def get_details(self):  
        return super().get_details() + f", Expiry: {self.__expiry_date}"

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Grocery"
        data["expiry_date"] = self.__expiry_date
        return data



class InventoryIterator:
    def __init__(self, products):
        self._products = products
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._products):
            result = self._products[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration


class Inventory:
    def __init__(self):
        self.__products = []

    def __iter__(self):
        return InventoryIterator(self.__products)

    @log_action
    def add_product(self, product):
        self.__products.append(product)
        print("Product added successfully!")

    @log_action
    def remove_product(self, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id:
                self.__products.remove(product)
                print("Product removed successfully!")
                return
        raise Exception("Product not found")

    @log_action
    def update_stock(self, product_id, new_stock):
        for product in self.__products:
            if product.get_product_id() == product_id:
                product.set_stock(new_stock)
                print("Stock updated successfully!")
                return
        raise Exception("Product not found")

    def search_product(self, name):
        results = [p for p in self.__products if name.lower() in p.get_name().lower()]
        return results

    def save_to_file(self, filename="inventory.json"):
        data = [product.to_dict() for product in self.__products]
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print("Inventory saved!")

    def load_from_file(self, filename="inventory.json"):
        if not os.path.exists(filename):
            return
        with open(filename, "r") as f:
            data = json.load(f)

        for item in data:
            if item["type"] == "Electronics":
                product = Electronics(
                    item["product_id"],
                    item["name"],
                    item["price"],
                    item["stock"],
                    item["warranty_years"]
                )
            elif item["type"] == "Grocery":
                product = Grocery(
                    item["product_id"],
                    item["name"],
                    item["price"],
                    item["stock"],
                    item["expiry_date"]
                )
            else:
                product = Product(
                    item["product_id"],
                    item["name"],
                    item["price"],
                    item["stock"]
                )
            self.__products.append(product)
        print("Inventory loaded!")



def main():
    inventory = Inventory()
    inventory.load_from_file()

    while True:
        try:
            print("\n===== Inventory Menu =====")
            print("1. Add Electronics")
            print("2. Add Grocery")
            print("3. Remove Product")
            print("4. Update Stock")
            print("5. Search Product")
            print("6. List All Products")
            print("7. Save & Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                p = Electronics(
                    input("ID: "),
                    input("Name: "),
                    float(input("Price: ")),
                    int(input("Stock: ")),
                    int(input("Warranty Years: "))
                )
                inventory.add_product(p)

            elif choice == "2":
                p = Grocery(
                    input("ID: "),
                    input("Name: "),
                    float(input("Price: ")),
                    int(input("Stock: ")),
                    input("Expiry Date: ")
                )
                inventory.add_product(p)

            elif choice == "3":
                inventory.remove_product(input("Enter Product ID: "))

            elif choice == "4":
                inventory.update_stock(
                    input("Enter Product ID: "),
                    int(input("New Stock: "))
                )

            elif choice == "5":
                results = inventory.search_product(input("Enter Name: "))
                for product in results:
                    print(product.get_details())

            elif choice == "6":
                for product in inventory:
                    print(product.get_details())

            elif choice == "7":
                inventory.save_to_file()
                print("Goodbye!")
                break

            else:
                print("Invalid choice!")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
