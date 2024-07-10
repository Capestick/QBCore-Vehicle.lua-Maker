import os
import sys

def format_vehicle(model, name, brand, price, category, shop):
    return f"{{ model = '{model}', name = '{name}', brand = '{brand}', price = {price}, category = '{category}', type = 'automobile', shop = '{shop}' }},"

def sanitize_input(input_value):
    return input_value.replace("'", "").replace('"', '')

def get_vehicle_details():
    model = sanitize_input(input("Enter the model: "))
    name = sanitize_input(input("Enter the name: "))
    brand = sanitize_input(input("Enter the brand: "))
    price = sanitize_input(input("Enter the price: "))
    category = sanitize_input(input("Enter the category: "))
    shop = sanitize_input(input("Enter the shop: "))
    return model, name, brand, price, category, shop

def process_single_vehicle():
    model, name, brand, price, category, shop = get_vehicle_details()
    formatted_vehicle = format_vehicle(model, name, brand, price, category, shop)
    print("Formatted vehicle:")
    print(formatted_vehicle)
    
    with open("single_vehicle.txt", "w") as file:
        file.write(formatted_vehicle)
    
    print("Your Single Car has been written to single_vehicle.txt Please open the File and put the cars into your QBCore/shared/Vehicle.lua! ")
    print_credits()

def process_car_pack():
    print("Processing car pack...")
    car_models = []
    print("Enter car models one per line. Type 'done' when finished:")
    
    while True:
        car_model = sanitize_input(input())
        if car_model.lower() == 'done':
            break
        car_models.append(car_model)

    default_brand = "addon-vehicle"
    default_price = 50000
    default_category = "addon"
    default_shop = "pdm"

    formatted_vehicles = [
        format_vehicle(model, model.title(), default_brand, default_price, default_category, default_shop)
        for model in car_models
    ]

    print("Formatted vehicles:")
    for vehicle in formatted_vehicles:
        print(vehicle)
    
    with open("car_pack.txt", "w") as file:
        for vehicle in formatted_vehicles:
            file.write(vehicle + "\n")
    
    print("All vehicles have been written to car_pack.txt Please open the File and put the cars into your QBCore/shared/Vehicle.lua! ")
    print_credits()

def print_credits():
    print(r"""
  Kyan Made this! 

  Discord Solo_Capestick
  Github Capestick

  Thanks for using!
    """)

def main():
    print("Is this a couple of vehicles or a car pack?")
    choice = input("Enter 'single' for a couple of vehicles or 'pack' for a car pack: ").strip().lower()
    
    if choice == 'single':
        process_single_vehicle()
    elif choice == 'pack':
        process_car_pack()
    else:
        print("Invalid input. Please enter 'single' or 'pack'.")

if __name__ == "__main__":
    main()
