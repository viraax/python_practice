# Petia Nikolova
# July 26, 2018

def main():
	
	usr_str = str(input("Enter a word to see if it is a palindrome: ")).lower()
	
	new_str = usr_str[:]
	reverse_str = usr_str[::-1]
	
	if new_str == reverse_str:
		print("This word is a palindrome!!!!!!")
	else:
		print("Nah, this ain't no palindrome.")


main()
