print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
# calculate price of size pizza
if size == 'S':
    price = 15
elif size == 'M':
    price = 20
else:
    price = 25

if extra_cheese == 'Y':
    price += 1

if pepperoni == 'Y':
    if size == 'M' or size == 'L':
        price += 3
    else:
        price += 2

print(f"Your final bill is: ${price}.")