# Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

cranes = int(input('Введите итоговое число журавликов: '))

katyasDone = cranes/2
petyasDone = seregasDone = katyasDone/2

print('Петя сделал: ' + str(petyasDone) + ', Сережа сделал: ' + str(seregasDone) + ', Катя сделала: ' + str(katyasDone))