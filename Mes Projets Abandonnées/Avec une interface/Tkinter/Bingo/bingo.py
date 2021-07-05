from random import *

running = True

while running:
	max = input("Maximum: ")
	try:
		max = int(max)
	except:
		error = True
		while error:
			print(" \nVeuillez indiquer un nombre entier.")
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
			number = input(" \nVeuillez indiquer un entier.\n-->  ")
			try:
				number=int(number)
				error=False
			except:
				error=True				
	while number != to_find:
		if number < to_find:
			print(" \nTrop bas.")
		else:
			print(" \nTrop haut.")
		number = input("-->  ")
		try:
			number=int(number)
		except:
			error=True
			while error:
				number=input(" \nVeuillez indiquer un entier.\n-->  ")
				try:
					number=int(number)
					error=False
				except:
					error=True
	print(f" \nGagné ! Le nombre était {to_find}.")
