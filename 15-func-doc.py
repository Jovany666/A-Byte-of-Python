#coding: utf-8

def printMax(x, y):
	'''imprime o maior entre dois números.

	os dois valores devem ser intereiros.'''
	x = int (x) #converte para inteiro, se possível
	y = int (y)

	if x > y:
		print(x, 'é o máximo')
	else:
		print(y, 'é o máximo')

printMax(3, 5)
print(printMax.__doc__)