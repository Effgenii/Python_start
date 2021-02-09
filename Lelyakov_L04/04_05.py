from functools import reduce

def mult (el_1, el_2):
    return (el_1 * el_2)

list_my = [el for el in list(range(100, 1001)) if el % 2 == 0]

print (reduce(mult, (list_my)))

# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
