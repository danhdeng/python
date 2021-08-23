import random

def play():
    user = input("what is your 'r' for rock, 'p' for paper, 's' for scissors\n ")
    computer = random.choice(['r', 'p', 's'])
    person = {
        "name": "dan",
        "age": 32,
        "address": "Canada"
    }

    print(person["name"])

    if user == computer:
        return 'It\'s a tie'

    if is_win(user, computer):
        return 'you won!'

    return 'you lost';

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True

print(play())
