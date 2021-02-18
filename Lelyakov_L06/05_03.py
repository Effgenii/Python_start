# -*- coding: cp1251 -*-

class Worker:
    name = str
    surname = str
    position = str
    _income = dict
class Position(Worker):
    def __init__(self, name, surname, position, wage: float, bonus: float):
        self.name = str(name)
        self.surname = str(surname)
        self.position = str(position)
        self._income = {'wage': wage, 'bonus': bonus}
    def get_full_name (self):
        return self.name + ' ' + self.surname
    def get_total_income (self):
        return (self._income['wage']+ self._income['bonus'])

ii = Position('����','������', '��������' ,1000, 100)
pp = Position('����','�e����', '�����������',1100, 150)
print (ii.get_full_name(), ii.position, ii.get_total_income())
print (pp.get_full_name(), pp.position, pp.get_total_income())

# 3. ����������� ������� ����� Worker (��������), � ������� ���������� ��������: name, surname,
# position (���������), income (�����). ��������� ������� ������ ���� ���������� � ��������� �� �������,
# ���������� ��������: ����� � ������, ��������, {"wage": wage, "bonus": bonus}. ������� ����� Position
# (���������) �� ���� ������ Worker. � ������ Position ����������� ������ ��������� ������� �����
# ���������� (get_full_name) � ������ � ������ ������ (get_total_income). ��������� ������ �������
# �� �������� ������ (������� ���������� ������ Position, �������� ������, ��������� �������� ���������,
# ������� ������ �����������).