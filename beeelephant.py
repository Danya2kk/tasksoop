class BeeEl:

    def __init__(self, bee, elephant):
        self.bee = bee
        self.elephant = elephant

    def fly(self):
        return self.bee >= self.elephant

    def trumpet(self):
        if self.elephant >= self.bee:
            return "tu-tu-doo-doo"
        else:
            return "wzzzzzz"

    def eat(self, meal, value):
        if meal == "nectar":
            self.elephant = max(0, self.elephant - value)
            self.bee = min(100, self.bee + value)

        elif meal == "grass":
            self.elephant = min(100, self.elephant + value)
            self.bee = max(0, self.bee - value)


bee_el = BeeEl(30, 70)
print(bee_el.fly())
print(bee_el.trumpet())

bee_el.eat("nectar", 20)
print(bee_el.bee, bee_el.elephant)

bee_el.eat("grass", 40)
print(bee_el.bee, bee_el.elephant)