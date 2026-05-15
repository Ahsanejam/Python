import random


friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# 1st Option
# This random.choice is for give random name or number from the lists
print(random.choice(friends))

# 2nd Option
random_index = random.randint(0, 4)
print(friends[random_index])
