import random
from game_data import data
from art import logo, vs

def random_generate():
    generate_lists = random.choice(data)
    return generate_lists
count_score = 0
A = random_generate()
B = random_generate()


continue_running = True
while continue_running:
    if count_score >= 1:
        print("\n" * 20)
    print(logo)
    if count_score >= 1:
        print(f"You're right! Current score: {count_score}.")
    print(f"Compare A: {A["name"]}, a {A["description"]}, from {A["country"]}")
    print(vs)
    print(f"Against B: {B["name"]}, a {B["description"]}, from {B["country"]}")

    followers = input("Who has more followers? Type 'A' or 'B': ").upper()

    if followers == 'A':
        if A["follower_count"] >= B["follower_count"]:
            count_score += 1
            print(A["follower_count"])
            print(B["follower_count"])
            A = B
        else:
            print(A["follower_count"])
            print(B["follower_count"])
            print("\n"* 20)
            print(logo)
            print(f"Sorry, that's wrong. Final score: {count_score}")
            continue_running = False

    if followers == 'B':
        if B["follower_count"] >= A["follower_count"]:
            count_score += 1
            print(A["follower_count"])
            print(B["follower_count"])
            A = B
        else:
            print(A["follower_count"])
            print(B["follower_count"])
            print("\n" * 20)
            print(logo)
            print(f"Sorry, that's wrong. Final score: {count_score}")
            continue_running = False
    B = random_generate()
    if B == A:
        B = random_generate()


