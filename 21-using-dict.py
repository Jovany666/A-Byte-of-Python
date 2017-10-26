

# 'ab' é diminuitivo para 'a'ddress'b'ook

ad = { 'Swaroop'    : 'swaroop@swaroopch.com',
		'Larry'     : 'larry@wall.org',
		'Matsumoto' : 'matz@ruby-lang.org',
		'Spammer'   : 'spammer@hotmail.com'
	}

print("Swaroop's address is", ab['Swaroop'])

#Deletando um par key/value
del ab['Spammer']

print('\nThere are {0} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
	print('Contact {0} at {1}'.format(nome, address))

#adicionando um par key/value
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab: #ou ab.has_key('Guido')
	print("\nGuido's address is", ab[Guido])