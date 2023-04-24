# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12 

n = int(input('Введите кол-во элементов первого множества: '))
m = int(input('Введите кол-во элементов вторго множества: '))
firstArray = []
secArray = []
i_n = i_m = 0

while i_n < n:
    addedNumb1 = int(input('Введите элемент первого множества (' + str(i_n + 1) + ' из ' + str(n) + ' ): '))
    firstArray.insert(i_n, addedNumb1)
    i_n += 1
    
while i_m < m:
    addedNumb2 = int(input('Введите элемент второго множества (' + str(i_m + 1) + ' из ' + str(m) + ' ): '))
    secArray.insert(i_m, addedNumb2)
    i_m += 1


firstMult = set(firstArray)
secMult = set(secArray)
intersMult = firstMult.intersection(secMult)
intersArray = list(intersMult)
print(sorted(intersArray))