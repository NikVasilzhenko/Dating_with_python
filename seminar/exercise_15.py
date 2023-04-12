# Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза

userNumb = int(input('Введите число арбузов: '))

minMelonWeight = 30000
maxMelonWeight = 0

for i in range(userNumb):
    nextMelonWeight = int(input('Ведите вес ' + str(i+1) + ' арбуза: '))
    if nextMelonWeight > maxMelonWeight:
        maxMelonWeight = nextMelonWeight
    elif nextMelonWeight < minMelonWeight:
        minMelonWeight = nextMelonWeight

print('Самый тяжелы: ' + str(maxMelonWeight) + ', самый легкий: ' + str(minMelonWeight))