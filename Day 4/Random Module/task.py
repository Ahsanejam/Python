import random
# import my_module
#
# random_integer = random.randint(1, 10)
# print(random_integer)
#
# print(my_module.my_favourite_number)


# Create random floating point number
# This random function can't take any input , * 10 means from number 0.0 <= Number < 10
# means smaller than 10 and greater than 0

# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)



# This uniform in-build function is for to find random float number from a <= Number <= b
# means any number in between or equals to

# random_float = random.uniform(1, 10)
# print(random_float)

# Heads and Tails program
# 0 means heads and 1 means tails
coins_flips = random.randint(0, 1)
if coins_flips == 0:
    print("Heads")
else:
    print("Tails")
