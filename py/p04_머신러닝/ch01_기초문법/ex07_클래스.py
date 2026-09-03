class FourCal:
    value=100

    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
    def change_value(self, value):
        self.value = value

a = FourCal()
b = FourCal()
a.setdata(10, 20)
b.setdata(30, 40)
print(type(a))
print(a.add())

FourCal.setdata(a, 1, 2)
print(a.add())
print("a:", a.value)
print("b:", b.value)
a.change_value(500)
print(a.value)
a.value=100000
print(a.value)
