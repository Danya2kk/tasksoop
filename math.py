class Math:
    def __init__(self):
        pass

    def addition(self, x, y):
        return x + y

    def subtraction(self, x, y):
        return x - y

    def multiplication(self, x, y):
        return x * y

    def division(self, x, y):
        try:
            return x/y
        except ZeroDivisionError:
            print("На ноль делить нельзя")


math = Math()
print(f"Сложение: {math.addition(2,3)}")
print(f"Вычитание: {math.subtraction(4, 2)}")
print(f"Умножение: {math.multiplication(3, 3)}")
print(f"Деление: {math.division(4, 2)}")
print(f"Деление: {math.division(4, 0)}")
