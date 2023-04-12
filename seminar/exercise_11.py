# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.

userNumb = int(input('Введите число: '))

lastFibNumb = 0
primFibNumb = 1 
indexCounter = 1

while primFibNumb <= userNumb:
    nextFibNumb = lastFibNumb + primFibNumb
    lastFibNumb = primFibNumb
    primFibNumb = nextFibNumb
    indexCounter = indexCounter + 1

if userNumb == lastFibNumb:
    print(indexCounter)
else:
    print('-1')