def func(x):
    print('x is', x)
    x = 2
    print('variável local x mudou para', x)
x = 50
func(x)
print('x continua', x)