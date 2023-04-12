# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл while

#==================================================

#Решение 1

# number = int(input('Введите число: '))
# i = 1
# factorial = 1

# while i<=number:
#     factorial *= i
#     i += 1
    
# print(factorial)

#==================================================

#Решение 2

number = int(input('Введите число: '))

factorial = 1

while number > 1:
    factorial = factorial * number
    number = number - 1

print(factorial)
