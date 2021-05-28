# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class MyComlex:
    def __init__(self, Re, Im):
        self.Re = Re
        self.Im = Im

    def __str__(self):
        return f"{self.Re}+{self.Im}j"

    def __add__(self, other):
        return MyComlex(self.Re+other.Re,self.Im+other.Im)

    def __mul__(self, other):
        return MyComlex(self.Re * other.Re - self.Im*other.Im, self.Im * other.Re+self.Re*other.Im)


c1 = MyComlex(2,5)
c1_ = 2+5j

c2 = MyComlex(5,3)
c2_ = 5+3j

c3=c1+c2
c3_=c1_+c2_
c4=c1*c2
c4_=c1_*c2_
print(f"c1 = {c1}")
print(f"c2 = {c2}")
print(f"c1+c2 = {c3}")
print(f"c1*c2 = {c4}")

print(c3_)
print(c4_)