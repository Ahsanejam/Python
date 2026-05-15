import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
# Method - 1
# lists = []
#
# letters_of = [random.choice(letters) for x in range(nr_letters)]
# symbols_of = [random.choice(symbols) for y in range(nr_symbols)]
# numbers_of = [random.choice(numbers) for z in range(nr_numbers)]
#
# for letter in letters_of:
#     lists.append(letter)
# for syb in symbols_of:
#     lists.append(syb)
# for num in numbers_of:
#     lists.append(num)
# print(lists)
# random.shuffle(lists)
# print(lists)
#
# password = ""
# for x in lists:
#     password += x
# print(f"Your password is : {password}")

# Method - 2
password_lists = []
for x in range(0, nr_letters):
    password_lists.append(random.choice(letters))
for y in range(0, nr_symbols):
    password_lists.append(random.choice(symbols))
for z in range(0, nr_numbers):
    password_lists.append(random.choice(numbers))

print(password_lists)

random.shuffle(password_lists)
print(password_lists)

password = ""
for pas in password_lists:
    password += pas
print(f"Your password is : {password}")


# Method - 3
# password_lists = []
# # print(random.choices(numbers, k=3))
#
# rand_letters = random.choices(letters, k=nr_letters)
# rand_symbols = random.choices(symbols, k=nr_symbols)
# rand_numbers = random.choices(numbers, k=nr_numbers)
#
# for let in rand_letters:
#     password_lists.append(let)
# for sym in rand_symbols:
#     password_lists.append(sym)
# for num in rand_numbers:
#     password_lists.append(num)
#
# print(password_lists)
# random.shuffle(password_lists)
# print(password_lists)
#
# password = ""
# for passw in password_lists:
#     password += passw
# print(f"Your password is : {password}")
