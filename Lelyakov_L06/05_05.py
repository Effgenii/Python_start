# -*- coding: cp1251 -*-
class Stationery:
    title = str()
    def draw (self):
        print('������ ���������')
class Pen(Stationery):
    def draw(self):
        print('������ ������')
class Pencil(Stationery):
    def draw(self):
        print('������ ����������')
class Handle(Stationery):
    def draw(self):
        print('������ ��������')

x = Stationery()
pen = Pen()
pencil = Pencil()
handle = Handle()
x.draw()
pen.draw()
pencil.draw()
handle.draw()


# 5. ����������� ����� Stationery (������������ ��������������). ���������� � ��� ������� title
# (��������) � ����� draw (���������). ����� ������� ��������� ������� ���������.� ������� ���
# �������� ������ Pen (�����), Pencil (��������), Handle (������). � ������ �� ������� �����������
# ��������������� ������ draw. ��� ������� �� ������� ������ ������ �������� ���������� ���������.
# ������� ���������� ������� � ���������, ��� ������� ��������� ����� ��� ������� ����������.
