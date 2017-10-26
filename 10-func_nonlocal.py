def func_outer():
    x = 2
    print('x é', x)

    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    print('O x local mudou para', x)
func_outer()