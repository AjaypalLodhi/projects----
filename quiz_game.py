print("Welcome!")
play = input("Do you want to participate in quiz? ")
if play.lower() != "yes":
	quit()
inst = "\nYour task is to get 50% marks for win the quiz, there is minus\
marking 1\ 4 makrks will be deduct if wrong answer."
print(inst)
print()
score = 0
x = 0
#1
Answer = input("What does ERP stand for? ")
if Answer.lower() == "enterprize resource planning":
	print("Correct")
	score += 1
	x += 1

else: 
	print("Incorrect")
	score -= 0.25
#2
Answer = input("What is the full form of NCR? ")
if Answer.lower() == "national capital region":
	print("Correct")
	score += 1
	x += 1
else: 
	print("Incorrect")
	score -= 0.25
#3
Answer = input("What is the full form of CID? ")
if Answer.lower() == "crime investigation department":
	print("Correct")
	score += 1
	x += 1
else: 
	print("Incorrect")
	score -= 0.25
#4
Answer = input("What does TRP stand for? ")
if Answer.lower() == "television rating point":
	print("Correct")
	score += 1
	x += 1
else: 
	print("Incorrect")
	score -= 0.25
#5
Answer = input("What is the full form of AM? ")
if Answer.lower() == "anti meridiem":
	print("Correct")
	score += 1
	x += 1
else: 
	print("Incorrect")
	score -= 0.25
#6
Answer = input("What is the full form of PM? ")
if Answer.lower() == "post meridiem":
	print("Correct")
	score += 1
	x += 1
else: 
	print("Incorrect")
	score -= 0.25
#7
Answer = input("What does DP stand for? ")
if Answer.lower() == "display picture":
	print("Correct")
	score += 1
	x += 1
else: 
	print("Incorrect")
	score -= 0.25
#8
Answer = input("What does IPL stand for? ")
if Answer.lower() == "post meridiem":
	print("Correct")
	score += 1
	x += 1
else: 
	print("Incorrect")
	score -= 0.25
if score<0:
	score = 0
percentage = (score/8)*100
if percentage >= 50:
    print("Congratulations you win the quize!")
else: print("Oops! you are fail.., Try again.")
print("you got "+ str(x) + " questions correct. ")
print("your score is " + str(score)+".")
print("your percent score is " + str(percentage) + "%.")

