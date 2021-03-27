import random
from colorama import Fore, Back, Style, init
init()

def shuffle():
	try:
			file = input("Name of your .txt file : ")
			print("---------")
			lines = open(file).readlines()
			random.shuffle(lines)
			open(file, 'w').writelines(lines)
			print(Fore.YELLOW + file + Fore.GREEN + " has been succesfully shuffled." + Style.RESET_ALL)
			print("---------")
			shuffle()

	except FileNotFoundError:

			print(Fore.RED + "File not found." + Style.RESET_ALL)
			print("---------")
			shuffle()
shuffle()
