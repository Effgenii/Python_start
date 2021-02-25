# -*- coding: cp1251 -*-

class Car:
    speed = float
    color = str
    name = str
    is_police = bool(0)
    def __init__(self, speed, color, name):
        self.speed = int(speed)
        self.color = color
        self.name = name

    def go (self):
        print ('������', self.name, '�������')

    def stop (self):
        print ('������', self.name, '������������')

    def turn (self, direction):
        if direction == 'right':
            print('������', self.name, '��������� �������')
        elif direction == 'left':
            print('������', self.name, '��������� ������')
        else:
            print('������� �������� �� ����������, ������', self.name, '���� �����')

    def show_speed (self):
        print ('������', self.name, '���� �� ���������', self.speed)

    def check_police (self):
        if self.is_police == 1:
            print ('������', self.name,'����������� ������')
        else:
            print ('������', self.name,'�� ����������� ������')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('������', self.name, '���� � ����������� ��������')
        else:
            print ('�������� ������', self.name, '� �����')

class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('������', self.name, '���� � ����������� ��������')
        else:
            print('�������� ������', self.name, '� �����')
class PoliceCar(Car):
    is_police = 1

zaz = TownCar(70, 'Blue', 'ZAZ')
bmw = SportCar(360, 'Red', 'BMW')
renault = WorkCar(30, 'Grey', 'Renault')
police = PoliceCar(250,'White', 'Audi-Police')

zaz.turn('right')
zaz.show_speed()
zaz.check_police()
bmw.show_speed()
renault.turn('left')
renault.turn('������')
renault.show_speed()
police.check_police()



# 4. ���������� ������� ����� Car. � ������� ������ ������ ���� ��������� ��������: speed, color, name,
# is_police (������). � ����� ������: go, stop, turn(direction), ������� ������ ��������, ���
# ������ �������, ������������, ��������� (����). ������� ��������� �������� �������: TownCar,
# SportCar, WorkCar, PoliceCar. �������� � ������� ����� ����� show_speed, ������� ������ ����������
# ������� �������� ����������. ��� ������� TownCar � WorkCar �������������� ����� show_speed.
# ��� �������� �������� ����� 60 (TownCar) � 40 (WorkCar) ������ ���������� ��������� � ���������� ��������.
# �������� ���������� �������, ��������� �������� ���������. ��������� ������ � ���������, ��������
# ���������. ��������� ����� ������� � ����� �������� ���������.