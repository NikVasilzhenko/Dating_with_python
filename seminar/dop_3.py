x0 = int(input("Координата x начальной клетки: "))
y0 = int(input("Координата y начальной клетки: "))
x1 = int(input("Координата x конечной клетки: "))
y1 = int(input("Координата y конечной клетки: "))

if (x1 == x0+1 or x1 == x0-1) and (y1 == y0+2 or y1 == y0-2):
    print('Может попасть')
elif (x1 == x0+2 or x1 == x0-2) and (y1 == y0+1 or y1 == y0-1):
    print('Может попасть')
else:
    print('Неможет попасть')