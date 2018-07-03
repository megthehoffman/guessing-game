"""A number-guessing game."""

# Put your code here
from random import randint

def is_matching_number():
	rand_num = randint(1,100)
	#print(rand_num)

	guess = input("Pick a number between 1 and 100. ")
	guesses = 1

	while True:
		try:
			guess = int(guess)	
			if guess == rand_num:
				break
			elif guess > 100 or guess < 1:
				print("You fool, we asked for a number between 1 and 100. Try again.")
			elif guess > rand_num:
				print ("Your guess is too high, try again.")
			else:
				print ("Your guess is too low, try again.")	
		except:
			print("Please input a valid integer.")
		
		guesses += 1
		guess = input("Your guess? ")

	print("Well done, " + name + "! It only took you " + str(guesses) + " tries!")

	return guesses

print("Hello player!")
name = input("What is your name? ")

best_score = is_matching_number()

while True:
	play_again = input("Do you want to play again? Enter Y or N. ")
	play_again = play_again.lower()

	if play_again == 'y':
		score = is_matching_number()
		if score < best_score:
			best_score = score
			print("New high score, " + name + "! " +str(best_score) + " tries")
	elif play_again == 'n':
		break
	else:
		print("Please enter valid input.")

print("Thanks for playing, " + name + "! Your best score was " + str(best_score) + " tries.")



