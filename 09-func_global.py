def func():
    global x

    print('x é', x)
    x = 2
    print('variável global x mudou para', x)
x = 50
func()
print('O valor de x é', x)