import random
top_of_range = input("Enter a number ")

if top_of_range.isdigit():
	top_of_range = int(top_of_range)
	
	if top_of_range<=0:
		print("Please type a number larger than 0 next time.")
		quit()
else: print("Type a number next time")

random_number = random.randint(0, top_of_range)
guesses = 0
while True:
	guesses += 1
	guess = input("Make a guess ")
	if guess.isdigit():
		guess = int(guess)
	else:
		print("please guess a number next time ")
		continue
	if guess == random_number:
		print("You got it!")
		break
	elif guess > random_number:
		print("You guess larger than random number ")
	elif guess < random_number:
		print("You guess below than random number ")
print("you got it in", guesses, "guesses")
	