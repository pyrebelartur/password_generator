import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Create separate lists
chosen_letters = []
chosen_symbols = []
chosen_numbers = []

# Add random letters
for i in range(nr_letters):
    random_letter = random.choice(letters)
    chosen_letters.append(random_letter)

# Add random symbols
for i in range(nr_symbols):
    random_symbol = random.choice(symbols)
    chosen_symbols.append(random_symbol)

# Add random numbers
for i in range(nr_numbers):
    random_number = random.choice(numbers)
    chosen_numbers.append(random_number)

# Combine all lists into one
password_list = chosen_letters + chosen_symbols + chosen_numbers

# Shuffle the list so characters are in random order
random.shuffle(password_list)

# Join the list into one string
password = ''
for char in password_list:
    password += char

# Show the password
print(f"Your generated password is: {password}")