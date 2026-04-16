import random
from game_data import data
import art

def details(account,label):
    account_name = account["name"]
    account_desc =account["description"]
    account_country =account["country"]
    return f"Compare {label}: {account_name},a {account_desc},from {account_country}"

def details_2(account,label):
    account_name = account["name"]
    account_desc =account["description"]
    account_country =account["country"]
    return f"Against {label}: {account_name},a {account_desc},from {account_country}"

def get_account():
    account = random.choice(data)
    return account

def is_correct(guess,a_followers,b_followers):
    if a_followers > b_followers:
        return guess == "A"
    else:
        return guess == "B"

# def is_correct():

game_start = True
count = 0

account_a =get_account()
account_b = get_account()

while game_start:
    while account_a == account_b:
        account_b = get_account()


    print(art.logo)
    print(details(account_a,"A"))
    print(art.vs)
    print(details_2(account_b,"B"))
    guess = input("Who has more followers? Type 'A' or 'B':").upper()
    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]
    if is_correct(guess,a_followers,b_followers):
        count += 1
        account_a = account_b
        account_b = get_account()
        print(f"You're right! Current score: {count}.")

    else:
        print(f"Sorry, that's wrong.Final score : {count}")
        game_start = False







