from random import *

def bingo():
	max = input("Maximum: ")
	try:
		max = int(max)
	except:
		error = True
		while error:
			print("Veuillez indiquer un nombre entier.")
			max= input("Maximum: ")
			try:
				max=int(max)
				error = False
			except:
				error=True
	to_find = randint(0, max)
	number = input("-->  ")
	try:
		number = int(number)
	except:
		error=True
		while error:
			number = input("Veuillez indiquer un entier.\n-->  ")
			try:
				number=int(number)
				error=False
			except:
				error=True				
	while number != to_find:
		if number < to_find:
			print("Trop bas.")
		else:
			print("Trop haut.")
		number = input("-->  ")
		try:
			number=int(number)
		except:
			error=True
			while error:
				number=input("Veuillez indiquer un entier.\n-->  ")
				try:
					number=int(number)
					error=False
				except:
					error=True
	print(f"Gagné ! Le nombre était {to_find}.")
