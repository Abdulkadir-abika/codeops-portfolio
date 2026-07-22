# 1. Unique cities
cities = ["Addis Ababa", "Hawassa", "Adama", "Addis Ababa", "Hawassa", "Gondar"]
distinct_cities = set(cities)
print(distinct_cities)
print(len(distinct_cities))

# 2. Price report
prices_dict = {"Coffee": 150,
    "Injera": 30,
    "Milk": 85,
    "Bread": 25,
    "Sugar": 110}
for item, price in prices_dict.items():
    print(item, price)

# 3. Tax comprehension
prices = [100, 250, 400, 80]
prices_with_tax = [price * 1.15 for price in prices]
print(prices_with_tax)

# 4. Cheap items
cheap_prices = [price for price in prices if price < 200]
print(cheap_prices)

# 5. Write & read
with open("names.txt", "w") as file:
    file.write("Abebe\nKebede\nAlmaz\n")

with open("names.txt", "r") as file:
    for line in file:
        print(line.strip())

# 6. Safe division
user_input = input("Enter a number : ")
try:
    number = float(user_input)
    print(1000 / number)
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
    