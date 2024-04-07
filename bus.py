class Bus:
    def __init__(self, max_seats, max_speed):
        self.speed = 0
        self.max_seats = max_seats
        self.max_speed = max_speed
        self.surnames = []
        self.free_seats = max_seats
        self.dict_seats = {i: None for i in range(1, max_seats + 1)}

    def add_speed(self, value):
        if self.speed + value <= self.max_speed:
            print(f"Скорость автобуса увеличилась с {self.speed} до {self.speed + value}")
            self.speed += value
        else:
            print("Не возможно набрать скорость выше максимальной")
            print(f"Скорость автобуса увеличилась с {self.speed} до максимума {self.max_speed}")
            self.speed = self.max_speed

    def reduce_speed(self, value):
        if self.speed - value >= 0:
            print(f"Скорость автобуса снизилась с {self.speed} до {self.speed - value}")
            self.speed -= value
        else:
            print("Автобус не может ехать с скоростью меньше 0. Автобус остановился")
            self.speed = 0


    def boarding_passengers(self, *args):
        for passenger in args:
            if self.free_seats > 0:
                for seat, name in self.dict_seats.items():
                    if name is None:
                        self.surnames.append(passenger)
                        self.dict_seats[seat] = passenger
                        self.free_seats -= 1
                        print(f"Пассажир {passenger} сел в автобус на месте {seat}")
                        break
            else:
                print("Автобус полон")
                break

    def unboarding_passengers(self, *args):
        for passenger in args:
            if passenger in self.surnames:
                for seat, name in self.dict_seats.items():
                    if name == passenger:
                        self.surnames.remove(passenger)
                        self.free_seats += 1
                        self.dict_seats[seat] = None
                        print(f"Пассажир {passenger} высадился из автобуса")
            else:
                print(f"Пассаижира {passenger} нет в автобусе")

    def __contains__(self, item):
        return item in self.surnames

    def __str__(self):
        return (f"Информация об автобусе:\nСкорость: {self.speed}\nМаксимальная скорость: {self.max_speed}\n"
                f"Всего сидений: {self.max_seats}\nСвободных сидений: {self.free_seats}\n"
                f"Пассажиры: {self.surnames}\n"
                f"Статус сидений: {self.dict_seats}")

    def __iadd__(self, other):
        self.boarding_passengers(other)
        return self

    def __isub__(self, other):
        self.unboarding_passengers(other)
        return self


bus = Bus(5, 100)
bus.boarding_passengers("Danik", "Vanya", "Maksim")
print(bus)
bus.unboarding_passengers("Danik", "Vanya", "Zhenya")
print(bus)
bus.boarding_passengers("Vera")
print(bus)
bus += "Alice"
print(bus)
bus -= "Alice"
print(bus)
print("Vera" in bus)
print("Alice" in bus)

bus.add_speed(60)
print(f"Автобус едет со скоростью ", bus.speed, "км/ч")
bus.add_speed(60)
print(f"Автобус едет со скоростью ", bus.speed, "км/ч")
bus.reduce_speed(90)
print(f"Автобус едет со скоростью ", bus.speed, "км/ч")
bus.reduce_speed(20)
print(f"Автобус едет со скоростью ", bus.speed, "км/ч")