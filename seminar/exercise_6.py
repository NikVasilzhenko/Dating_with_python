# Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

ticketNumber = str(input('Введите номер билета (6-значное число): '))

leftHalf = int(ticketNumber[0]) + int(ticketNumber[1]) + int(ticketNumber[2])
rightHalf = int(ticketNumber[3]) + int(ticketNumber[4]) + int(ticketNumber[5])

if leftHalf == rightHalf:
    print('Это счастливый билет')
else:
    print('Это простой билет')