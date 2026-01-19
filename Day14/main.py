import random
import art
from game_data import data

def data_info(acc):
    """Takes a dictionary and returns it into displayable format"""
    name = acc["name"]
    description = acc["description"]
    country = acc["country"]
    return f"{name}, a {description}, from {country}"

print(art.logo)
score = 0
data_b = random.choice(data)

# create a loop to make the game repeatable
while True:
    ## generate a random data from game_data

    ## swapping data_b and data_a
    data_a = data_b
    data_b = random.choice(data)

    ## preventing duplicate data
    if data_b == data_a:
        data_b = random.choice(data)

    print(f"Compare A: {data_info(data_a)}")
    print(art.vs)

    print(f"Against B: {data_info(data_b)}.")

    ## generate user guess
    user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    ## clear the screen
    print("\n" * 15)
    print(art.logo)

    follower_count_of_a = data_a["follower_count"]
    follower_count_of_b = data_b["follower_count"]

    ## compare follower count
    if user_guess == "A":
        if follower_count_of_a > follower_count_of_b:
            score += 1
            print(f"You are right! Current score:  {score}\n")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break
    elif user_guess == "B":
        if follower_count_of_b > follower_count_of_a:
            score += 1
            print(f"You are right! Current score:  {score}\n")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break

