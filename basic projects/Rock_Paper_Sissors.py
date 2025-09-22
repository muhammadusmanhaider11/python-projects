#rock paper sissors
import random
def play():
    user = input(" 'r' for rock , 'p' for paper ,'s' for sissors\nENTER YOUR CHOICE:")
    computer = random.choice(['r','p','s'])
    print(f"computer :{computer}")
    if user == computer:
        return 'tie'
    if won(user,computer):
        return 'you won'
    return 'you lost'
def won(player,opponent):
    if (player =='r'and opponent =='s') or(player=='s'and opponent=='p')or(player=='p'and opponent=='r'):
        return True
print(play())