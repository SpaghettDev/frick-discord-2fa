from os import getcwd
from time import sleep
from typing import Union
from random import choice
from os import mkdir, path, getcwd

# All the functions in the main file for simplicity's sake
def formatgc(arr: list) -> str:
	"""
	A simple function that turns a array into a string. Made this so i don't repeat myself...

	Args:

		arr: list to be formatted into a string.

	Returns:
		String formating of arr
	"""
	return ''.join(map(str, arr))

def genRndmChr(num: int = 0, gty: str = "abcdefghijklmnopqrstuvwxyz0123456789") -> Union[str, None]:
	"""A function that is used in the generator class to generate random characters. Uses the random module.
	
	Args:

		num: The number of times to generate a random character. Default value: 0

		gty: String to be used as random characters. Default value: gttypes['genTypeNorm'] =
		"ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789".

	Returns:
		Formatted version of arr. Or None.
	"""
	arr = []
	if num == 0:
		print("Please enter the number of random characters you want!")
		sleep(5)
		quit()

	for x in range(num):
		arr.append(choice(gty))
	return formatgc(arr)

def genRndmDigit(num: int = 0, gty: str = "0123456789") -> Union[str, None]:
	"""A function that is used in the generator class to generate random characters. Uses the random module.
	
	Args:

		num: The number of times to generate a random digit. Default value: 0

		gty: String to be used as random characters. Default value: gttypes['genTypeNorm'] =
		"0123456789".

	Returns:
		Formatted version of arr. Or None.
	"""
	arr = []
	if num == 0:
		print("Please enter the number of random digits you want!")
		sleep(5)
		quit()

	for x in range(num):
		arr.append(choice(gty))
	return formatgc(arr)

def writeToFile(file: str, mode: str, towrite: str) -> None:
	"""A function that makes a file and writes to it using the open() function. Made to clean up my main file code.
	Return type: None """
	with open(file, mode) as out:
		out.write(towrite)

def createGDir() -> None:
	"""A function that makes a directorie (folder) called "Generated Codes". Made to clean up my main file code.

	Returns:
		None
	"""
	try:
		mkdir(path.join(getcwd() + "/Generated Codes"))
	except PermissionError:
		print("Please grant permission to make folders.")
	except FileExistsError:
		pass

def genBackup(num: int): 
	""""""
	ar = []
	for x in range(num):
		ar.append(genRndmChr(4) + "-" + genRndmChr(4) + "\n")
	return formatgc(ar)

def genNormal(num: int): 
	""""""
	ar = []
	for x in range(num):
		ar.append(genRndmDigit(6) + "\n")
	return formatgc(ar)

def to_color(string, color):
	color_code = {
		'blue': '\033[34m',
		'cyan': '\033[96m',
		'yellow': '\033[33m',
		'green': '\033[32m',
		'red': '\033[31m',
		'black': '\033[30m',
		'magenta': '\033[35m',
		'white': '\033[37m',
		'custom': '\033[0;34;47m'
	}
	return color_code[color] + str(string) + '\033[0m'


createGDir()

if __name__ == "__main__":
	try:
		menu = int(input(to_color("What type of code would you like to generate?\n[1] - 8 Digit Backup Code\n[2] - 6 Digit Normal Code\n ", "blue")))
		if menu == 1:
			t = int(input(to_color("How many discord backup codes? ", "blue")))
			filep = getcwd() + f"/Generated Codes/ {t} backup codes.txt"
			writeToFile(filep, "a", genBackup(t))
			print(to_color("Generated the backup codes.", "cyan"))
			quit()
		elif menu == 2:
			t = int(input(to_color("How many discord normal codes? ", "blue")))
			filep = getcwd() + f"/Generated Codes/ {t} normal codes.txt"
			writeToFile(filep, "a", genNormal(t))
			print(to_color("Generated the normal codes.", "cyan"))
			quit()
		else:
			print("Invalid option entered!")
			
	except BaseException as ex:
		if isinstance(ex, SystemExit) or isinstance(ex, KeyboardInterrupt):
			quit()
