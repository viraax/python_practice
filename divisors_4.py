# Petia Nikolova
# June 16, 2018

def main():
	

	while True:
		try:
			user_num = int(input("Enter the number that you want to see the divisors for: "))
			if user_num < 1 or user_num > 1000000:
				raise ValueError 
			break
		except ValueError:
			print("Invalid integer. The number must be in the range of 1 - 1 million.")	

	
	x = list(range(1, user_num+1))
	divisor_list =[]

	for num in x:
		if user_num % num == 0:
			divisor_list.append(num)

	print(divisor_list)

main()
