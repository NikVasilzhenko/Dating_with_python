# Найдите сумму цифр трехзначного числа.

number = int(input('Введите трехзначное число: '))

units = number%10
tens = (number%100 - units)//10
hundreds = (number-units-tens)//100

print(hundreds + tens + units)