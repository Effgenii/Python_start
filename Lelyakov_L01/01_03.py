# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369

n = int(input("Введите число n:"))
# Предполагаем что число целое, положительное, и не делаем дополнительных проверок и преобразований
x = n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n))
# можно было считать и с помощью цикла, но для трех шагов проще так
print(x)
