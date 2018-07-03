"""A number-guessing game."""

# Put your code here
from random import randint

print("Hello player!")
name = input("What is your name? ")

rand_num = randint(1,100)

guess = int(input("Pick a number between 1 and 100. "))

guesses = 1
while guess != rand_num:
	if guess > rand_num:
		print ("Your guess is too high, try again.")
	else:
		print ("Your guess is too low, try again.")
	guesses += 1

	guess = int(input("Your guess? "))

print("Well done, " + name + "! It only took you " + str(guesses) + " tries!")


