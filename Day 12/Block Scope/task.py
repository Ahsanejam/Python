# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]
#
# def create_enemy():
#     new_enemy = ""
#     if game_level < 5:
#         new_enemy = enemies[0]
#
#     print(new_enemy)

# def prime(num):
#     if num < 2:
#         return False
#     for i in range(2, num-1):
#         if num % i == 0:
#             return False
#     return True
# print(prime(75))

def prime(num):
    for i in range(2, num-1):
        if num % i == 0:
            return False
    return True
print(prime(75))