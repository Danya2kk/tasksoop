class Product:
    def __init__(self, name_product, name_shop, cost):
        self.__name_product = name_product
        self.__name_shop = name_shop
        self.__cost = cost

    def get_name_product(self):
        return self.__name_product

    def get_name_shop(self):
        return self.__name_shop

    def get_cost(self):
        return self.__cost

    def __str__(self):
        return f"Название товара: {self.__name_product}, Название магазина: {self.__name_shop}, Цена: {self.__cost}$"


class Stack:
    def __init__(self):
        self.__products = []

    def get_products(self):
        return self.__products

    def add_product(self, product):
        self.__products.append(product)

    def find_by_index(self, index):
        return self.__products[index]

    def find_by_name(self, name):
        for product in self.__products:
            if product.get_name_product() == name:
                return product
        return f"Продукта с таким именем нет на складе"

    def sort_by_name(self):
        self.__products.sort(key=lambda product: product.get_name_product())

    def sort_by_name_shop(self):
        self.__products.sort(key=lambda product: product.get_name_shop())

    def sort_by_cost(self):
        self.__products.sort(key=lambda product: product.get_cost())

    def __add__(self, other):
        total = 0
        for product in self.__products:
            total += product.get_cost()
        total += other.get_cost()
        return total


stack = Stack()

product1 = Product("Ноутбук", "ДНС", 2000)
product2 = Product("Монитор", "5 Элемент", 300)
product3 = Product("Iphone 15", "Applestore", 1000)

stack.add_product(product1)
stack.add_product(product2)
stack.add_product(product3)

print("------Список Товаров------")
for product in stack.get_products():
    print(product)
print()

index = int(input("Введите индекс для поиска: "))
print(f"Товар под индексом {index}: ", stack.find_by_index(index))

name = str(input("Введите название товара: "))
print(f"Товар с именем {name}: ", stack.find_by_name(name))
print()

print("Сортирвка по имени: ")
stack.sort_by_name()
for product in stack.get_products():
    print(product)
print()

print("Сортировка по названию магазина: ")
stack.sort_by_name_shop()
for product in stack.get_products():
    print(product)
print()

print("Сортировка по цене товара: ")
stack.sort_by_cost()
for product in stack.get_products():
    print(product)
print()

total = stack + Product("Стол", "Пинскдрев", 200)
print("Цена всех товаров на складе + новый товар: ", total)
