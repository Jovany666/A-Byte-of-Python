number = 23
guess = int(input('Digite um número inteiro: '))

if guess == number:
    print('parabéns, você advinhou. ') #novo bloco começa aqui
    print('(mas você não ganhou nenhum prémio!)') #novo bloco termina aqui
    
elif guess < number:
    print('Não, o numero era um pouco maior que isso') #outro bloco
    #você pode fazer o que quizer em um outro bloco...

else:
    print('Não, o numero era um pouco menor que isso') #você deve advinhar > numero a alcançar aqui.
    print('feito')
#esta última instrução é sempre executada, depois da instrução if executada.
