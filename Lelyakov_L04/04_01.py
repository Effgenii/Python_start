import script_my
# Почему Пайтон не приниммает (not support this syntax) модуль если назвать его : 04_01_script ?

productivity = float(input('Введите выработку (час):'))
rate = float(input('Введите ставку (руб/час):'))
bonus = float(input('Введите премию (руб):'))

print ('Заработная плата за неделю', script_my.salary(productivity, rate, bonus), 'рублей')
print (f"Заработная плата за неделю {script_my.salary(productivity, rate, bonus)} рублей")
print ('Заработная плата за неделю {} рублей'.format(script_my.salary(productivity, rate, bonus)))

# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы
# сотрудника. В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
