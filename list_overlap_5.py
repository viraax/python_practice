# Petia Nikolova
# July 25, 2018

import random

def main():
	
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

	c = []

	for num in a:
		if num in b:
			if num not in c:
				c.append(num)


	print("This is the first set list: ", a)
	print("This is the second set list: ", b)


	print("\nThe lists share these common numbers: ", c)

	rand_list1 = []
	rand_list2 = []

	rand_list3 = []

	for num1 in range(15):
		rand_list1.append(random.randint(0, 50))
	for num2 in range(23):
		rand_list2.append(random.randint(0, 50))

	for num in rand_list1:
		if num in rand_list2:
			if num not in rand_list3:
				rand_list3.append(num)

	print("\n\nThis is the first random set: ", rand_list1)
	print("This is the second random set: ", rand_list2)

	print("\nThe random lists share these common numbers: ", rand_list3)
main()
