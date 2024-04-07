import math


class Sphere:
    def __init__(self, r=1, x=0, y=0, z=0):
        self.r = r
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        return 4 / 3 * 3.14 * self.r ** 3

    def get_square(self):
        return 4 * 3.14 * self.r ** 2

    def get_radius(self):
        return self.r

    def get_center(self):
        return self.x, self.y, self.z

    def set_radius(self, value):
        self.r = value

    def set_center(self, new_x, new_z, new_y):
        self.x = new_x
        self.y = new_y
        self.z = new_z

    def is_point_inside(self, x_point, y_point, z_point):
        res = math.sqrt((x_point - self.x) ** 2 + (y_point - self.y) ** 2 + (z_point - self.z) ** 2)
        if res > self.r:
            return False
        else:
            return True


sp = Sphere(4, 3, 3, 3)
print(f"Сфера с радиусом {sp.get_radius()} и центром с координатами {sp.get_center()}")
print(f"Обьем сферы: {sp.get_volume()}\nПлощадь поверхности сферы: {sp.get_square()}")

point_x = int(input("Введите координату x для точки: "))
point_y = int(input("Введите координату y для точки: "))
point_z = int(input("Введите координату z для точки: "))

if sp.is_point_inside(point_x, point_y, point_y):
    print(f"Точка находится внутри сферы")
else:
    print(f"Данная точка не находится внутри сферы")

sp.set_center(2, 4, 5)
print(f"Новые координата центра сферы: {sp.get_center()}")
