# Petia Nikolova
# 15.07.2018
def main():

	list_num = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	new_list = []

	print("--- 1 ---")	
	for x in list_num:
		if (x < 5):
			print(x)

	print("--- 2 ---")
	for x in list_num:
		if (x < 5):
			new_list.append(x)
	print(new_list)

	print("--- 3 ---") 
	
	while True:
		try:
			user_num = int(input("Enter a number & I will check the list for any smaller numbers "))
			if user_num < 1 or user_num > 1000000:
 				raise ValueError #this will send it to the print message and back to the input option
			break
		except ValueError:
			print("Invalid integer. The number must be in the range of 1 - 1 million.")


	user_new_list = []
	for x in list_num:
		if (x < user_num):
			user_new_list.append(x)
	print(user_new_list)

main()
