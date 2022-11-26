import art
import random

def compare(num, guess):
	if num == guess:
		print("Spot on. Your guess was correct.")
	elif num > guess:
		print("Too low.")
	elif num < guess:
		print("Too high.")

print(art.logo)

print("\nI am thinking of a number from 1 to 100. Dare to guess?")
num = random.randint(1, 101)

while True:
	level = input("Choose a level 'easy' or 'hard': ").lower()
	if level == 'easy':
		attempts = 10
		break
	elif level == 'hard':
		attempts = 5
		break
	else:
		print("\nIncorrect entry. Try again")
print(f"\nYou have {attempts} chances to get this right.")

game_over = False


while attempts > 0 and game_over == False:
	guess = int(input(f"\nYour have {attempts} attempts left. Make a guess: "))
	compare(num, guess)
	attempts -= 1
	if num == guess:
		game_over = True

if attempts == 0:
	print("Too bad, you lost.")
print(f"My number was: {num}")
