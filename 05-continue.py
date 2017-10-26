while True:
    s = input('Entre com algo: ')
    if s == 'sair':
        break
    if len(s) < 3:
        print('Muito pequeno')
        continue
    print('A entrada é de tamanho suficiente')
    #faça outros tipos de processo aqui...