"""A number-guessing game."""

# Put your code here
from random import randint

def calculate_score(guesses,a,b):
	converted_score = int((10-guesses)/(10/(b-a)))
	print("Your score is " + str(converted_score) + ".")

	return converted_score

def is_matching_number():
	""" Play game to guess matching number"""
	a = int(input("You are going to guess an integer in a range, but you get to pick the range! What would you like the lower bound to be? "))
	b = int(input("What would you like the upper bound to be? "))

	rand_num = randint(a,b)
	#print(rand_num)

	guesses = 0
	guess = input("Pick a number between " + str(a) + " and " + str(b) + ". ")

	while True:
		guesses += 1
		try:
			guess = int(guess)	
			if guess == rand_num:
				print("Well done, " + name + "! It only took you " + str(guesses) + " tries!")
				break
			elif guess > b or guess < a:
				print("You fool, we asked for a number between " + str(a) + " and " + str(b) + ". Try again. ")
			elif guess > rand_num:
				print ("Your guess is too high, try again.")
			else:
				print ("Your guess is too low, try again.")	
		except:
			print("Please input a valid integer.")

		if guesses >= 10:
			print("Too many tries! Game over.")
			break

		print("You have " + str(10-guesses) + " remaining.")
		guess = input("Your guess? ")

	return calculate_score(guesses,a,b)

def play_again(first_score):
	best_score = first_score
	while True:
		play_again = input("Do you want to play again? Enter Y or N. ")
		play_again = play_again.lower()

		if play_again == 'y':
			score = is_matching_number()
			if score > best_score:
				best_score = score
				print("New high score, " + name + "! Your score is " + str(best_score) + " points.")
		elif play_again == 'n':
			break
		else:
			print("Please enter valid input.")
	return best_score


print("Hello player!")
name = input("What is your name? ")

first_score = is_matching_number()
final_score = play_again(first_score)
print("Thanks for playing, " + name + "! Your best score was " + str(final_score) + " points.")






