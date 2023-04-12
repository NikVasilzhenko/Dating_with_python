# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.

numberOfStudents1 = int(input('Введите количество учеников в 1-м классе: '))
numberOfStudents2 = int(input('Введите количество учеников в 2-м классе: '))
numberOfStudents3 = int(input('Введите количество учеников в 3-м классе: '))

numberOfTables1 = (numberOfStudents1 + 1)//2
numberOfTables2 = (numberOfStudents2 + 1)//2
numberOfTables3 = (numberOfStudents3 + 1)//2
totalTables = numberOfTables1 + numberOfTables2 + numberOfTables3

print('Понадобится парт: ' + str(totalTables))