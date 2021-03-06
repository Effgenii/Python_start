# список продуктов, содержит кортежи, каждый из кортежей включает клюс и словарь с параметрами
products = []
# счетчик ключей
n = int(1)
while True:
    name = str(input('Введите наименование товара: '))
    cost = float(input('Введите цену: '))
    number = int(input('Введите количество: '))
    measure = str(input('Введите единицы измерения: ' ))
    prod_dict = {'name': name, 'cost': cost, 'number': number, 'measure': measure}
    products.append(tuple([n, prod_dict]))
    n += 1
    des = int(input('Товар добавлен в список, добавить новый? (1/0)'))
    if des != 1:
        break
print('список товаров:', (products))
statistic = {}
for product in products:
    for item_key, item_value in product[1].items():
        if item_key in statistic:
            statistic[item_key].append(item_value)
        else:
            statistic[item_key] = [item_value]

print ('Аналитика', statistic)


# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер
# товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика
# товара, например название, а значение — список значений-характеристик, например список названий
# товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
