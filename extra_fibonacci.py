# Petia Nikolova
# July 27, 2018

def main():
	
	usr_n = int(input("Which n-th do you want to know? "))

	first = 0
	second = 1

	while usr_n < 0:
		usr_n = int(input("Enter a positive number. Which n-th do you want to know? "))
	
	if usr_n == 0:
		print(first)
	elif usr_n == 1:
		print(second)
	else:
		for x in range(2,usr_n):
			current = first + second
			first = second
			second = current
		print(second)
main()
