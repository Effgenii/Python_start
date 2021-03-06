import json
list_f = []
pivot = {}
list_result = []
average_profit = {}
with open("lesson7.txt", "r") as in_file:
    content = [line.rstrip() for line in in_file.readlines()]
    for el in content:
        el = (el.split(' '))
        if int(el[2])-int(el[3]) >= 0:
            list_f.append(int(el[2])-int(el[3]))
            print ((el[0]),': выручка', int(el[2]), 'минус издержки', int(el[3]), ' = ' ,int(el[2])-int(el[3]))
# из условия задачи неясно - добавлять ли фирмы с убытками в один словарь с остальными или создавать отдельный.
# если в отдельный - то добавляем проверку на отрицательное значение прибыли и добаляем в отдельный словарь.
        pivot[el[0]] = (int(el[2])-int(el[3]))
    print ('средняя прибыль', sum(list_f)/len(list_f))
    average_profit ['average_profit'] = (sum(list_f)/len(list_f))
    list_result.append (pivot)
    list_result.append (average_profit)
    print (list_result)
with open ("out_file.json", "w") as write_f:
    json.dump(list_result, write_f)


# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные
# о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю
# прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее
# в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.