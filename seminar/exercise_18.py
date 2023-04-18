# Требуется найти в массиве A[1..N] самый близкий по величине элемент 
# к заданному числу X. Пользователь в первой строке вводит натуральное число N – 
# количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

N = int(input('Введите колличество элементов в массиве: '))
iter = 0
array = []

while iter < N:
    array.append(int(input('Введите значение ' + str(iter + 1) + '-го элемента: ')))
    iter +=1
    
X = int(input('Введите искомое значение: '))

lessSibling = min(array)
moreSibling = max(array)
searchNumb = 0
isEqually = False

for i in array:
    if i == X:
        isEqually = True
        searchNumb = i
        break
    if i < X:
        if i > lessSibling:
            lessSibling = i
    if i > X:
        if i < moreSibling:
            moreSibling = i    

if isEqually == True:
    print('Самый близкий по величине элемент :' + str(searchNumb))
else:
    if (X - lessSibling) >= (moreSibling - X):
        print('Самый близкий по величине элемент :' + str(moreSibling))
    else:
        print('Самый близкий по величине элемент :' + str(lessSibling))