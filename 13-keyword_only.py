def total (initial=5, *numbers, vegetables):
    count = initial
    for number in numbers:
        count += number
    count += vegetables
    return count
    
print(total(10, 1, 2, 3, vegetables=50))
print(total(10, 1, 2, 3))

#levanta um erro, pois não fornecemos um valor de argumento padrão
para 'vegetables'