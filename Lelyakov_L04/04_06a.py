import script_my

num = int(input('Введите начальное значение списка:'))
interval = int(input('Введите конечное значение (не более 100):'))
print (script_my.lin_genetrator(num, interval+1))


# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,

# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что
# создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
