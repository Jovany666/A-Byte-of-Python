# coding: utf-8

#Esta é a minha lista de compras

shoplista = ['maçã', 'manga', 'cenoura', 'banana']

print('Eu tenho', len(shoplista), 'intes para comprar.')

print('Estes intens são:', end=' ')

for item in shoplista:
	print(item, end=' ')

print('\nTambém tenho que comprar arroz.')
shoplista.append('arroz')
print('Minha lista de compras é agora', shoplista)

print('Vou colocar a minha lista em ordem agora')
shoplista.sort()
print('A minha lista ordenada agora é', shoplista)

print('O primeiro item que comprei é', shoplista[0])
olditem = shoplista[0]
print('Eu comprei o', olditem)
print('Minha lista de compras é agora', shoplista)