# Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).

chocBarsWidth = int(input('Введити длину плитки шоколада (в квадратах): '))
chocBarsHeight = int(input('Введити ширину плитки шоколада (в квадратах): '))
chocBarsPiece = int(input('Введити длину куска плитки шоколада (в квадратах): '))

if (chocBarsPiece%chocBarsWidth==0 or chocBarsPiece%chocBarsHeight==0):
    print('Да, можно отломить')
else:
    print('Нет, неполучится отломить')