n = int(input('Введите число :'))

if n == 0:
    print('Нуль')
else:
    if n < 0:
        a = 'Отрицательное'
    else:
        a = 'Положительное'
        
    if n%2 != 0:
        b = 'нечетное'
    else:
        b = 'четное'
    print(a + ' ' + b)

