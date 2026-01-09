import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []
# appends random letter
for ch in range(nr_letters):
    letter = random.choice(letters)
    password_list.append(letter)

# appends random symbol
for sym in range(nr_symbols):
    symbol = random.choice(symbols)
    password_list.append(symbol)

# appends random number
for num in range(nr_numbers):
    number = random.choice(numbers)
    password_list.append(number)

# shuffles the password list
random.shuffle(password_list)

# assigns password_list as string
password = "".join(password_list)

# Outputs shuffled password
print(f"Your password is: {password}")





