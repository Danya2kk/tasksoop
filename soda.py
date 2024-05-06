class Soda:
    def __init__(self, flavor=None):
        self.flavor = flavor

    def __str__(self):
        if self.flavor:
            return f"у вас есть газировка с {self.flavor} вкусом"
        else:
            return "у вас обычная газировка"


soda1 = Soda("клубничный")
print(soda1)

soda2 = Soda()
print(soda2)
