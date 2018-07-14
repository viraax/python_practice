# Petia Nikolova
# 13.07.2018

def main():

	print("\n")	
	name = input("What is your name? ")
	age = int(input("Hey {0}! How old are you? ".format(name)))

	while ((age < 1) or (age > 125)):
		print("That was invalid! Try again!")
		age = int(input("Hey {0}! How old are you? ".format(name)))

	repeat = int(input("Enter a number more than 1 & up to 100 "))
	while ((repeat < 1) or (repeat > 100)):
		repeat = int(input("Enter a number more than 1 & up to 100 "))

	years_left = (100-age)
	for i in range(0, repeat):
		print("You will turn 100 in about", years_left, "years! \n")
	
main()
