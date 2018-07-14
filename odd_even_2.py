# Petia Nikolova 
# 14.07.2018

def main():
	while True:
		try:
			number = int(input('Enter a number: '))
			if number < 1 or number > 1000000:
				raise ValueError #send it to the print message and back to the input option
			break
		except ValueError:
			print("Invalid integer. The number must be in the range of 1 - 1 million.")	
	
	if (number % 4 == 0):
		print("Your number is divisible by 4! ")
	elif (number % 2 == 0):
		print("Your number is even! ")
	else:
		print("Your number is odd! ")

	
	while True:
		try:
			num1 = int(input('Enter a number: '))
			if num1 < 1 or num1 > 1000000:
				raise ValueError 
			break
		except ValueError:
			print("Invalid integer. The number must be in the range of 1 - 1 million.")	

	
	while True:
		try:
			num2 = int(input('Enter a number: '))
			if num2 < 1 or num2 > 1000000:
				raise ValueError 
			break
		except ValueError:
			print("Invalid integer. The number must be in the range of 1 - 1 million.")	


	if (num1 % num2 == 0):
		print("These numbers can be divided! The answer is", int((num1 / num2)))
	else:
		print("These numbers do not divide well. Sorry, try again! ")

main()
