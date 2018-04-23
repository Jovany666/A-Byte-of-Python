number = 23
running = True

while running:
    guess = int(input('Entre com um número: '))

    if guess == number:
        print('parabéns, você advinhou.')
        running = False #isto faz o loop while parar
    elif guess < number:
        print('não, é um pouco maior que este.')
    else:
        print('Não, é um pouco menor que este.')
else:
    print('o  loop while terminou.')
    print('fim')
