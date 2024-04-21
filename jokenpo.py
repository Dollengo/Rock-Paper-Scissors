import random

# 1 = Rock; 2 = Paper, 3 = Scissors.
adv = random.randint(1, 3)
player = input("Write 'rock' for rock, 'paper' for paper and 'scissors' for scissors: ").lower()
print(" ")
print("################################")
print(" ")
print(f"You: {player.upper()}")

if adv == 1:
    advplay = "rock"
    print("Adversary: ROCK")

elif adv == 2:
    advplay = "paper"
    print("Adversary: PAPER")

elif adv == 3:
    advplay = "scissors"
    print("Adversary: SCISSORS")

print(" ")
print("###############################")
print(" ")

if player == 'rock' and advplay == 'scissors':
    print("Win.")

elif player == 'rock' and advplay == 'paper':
    print("Game over.")

elif player == 'rock' and advplay == 'rock':
    print("Drew.")

elif player == 'paper' and advplay == 'scissors':
    print("Game over.")

elif player == 'paper' and advplay == 'paper':
    print("Drew.")

elif player == 'paper' and advplay == 'rock':
    print("Win.")

elif player == 'scissors' and advplay == 'scissors':
    print("Drew.")

elif player == 'scissors' and advplay == 'rock':
    print("Game over.")

elif player == 'scissors' and advplay == 'paper':
    print("Win.")