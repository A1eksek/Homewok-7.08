#Singleton
# class Singleton:
#     _instance = None
#
#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super(Singleton, cls).__new__(cls)
#         return cls._instance
#
#     def __init__(self):
#         # Этот конструктор вызывается только при первом создании экземпляра
#         pass
#
# # Использование
# singleton1 = Singleton()
# singleton2 = Singleton()
#
# print(singleton1 is singleton2)  # Выведет: True, так как это один и тот же экземпляр

########################################################

from abc import ABC, abstractmethod


# Интерфейсы продуктов
class Chair(ABC):
    @abstractmethod
    def sit_on(self):
        pass


class Sofa(ABC):
    @abstractmethod
    def lie_on(self):
        pass


# Конкретные продукты для стиля "Модерн"
class ModernChair(Chair):
    def sit_on(self):
        return "Сидеть на модернистском кресле"


class ModernSofa(Sofa):
    def lie_on(self):
        return "Лежать на модернистском диване"


# Конкретные продукты для стиля "Классика"
class ClassicChair(Chair):
    def sit_on(self):
        return "Сидеть на классическом кресле"


class ClassicSofa(Sofa):
    def lie_on(self):
        return "Лежать на классическом диване"


# Интерфейс Абстрактной Фабрики
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_sofa(self):
        pass


# Конкретная фабрика для стиля "Модерн"
class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return ModernChair()

    def create_sofa(self):
        return ModernSofa()


# Конкретная фабрика для стиля "Классика"
class ClassicFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return ClassicChair()

    def create_sofa(self):
        return ClassicSofa()


# Клиентский код
def client_code(factory: FurnitureFactory):
    chair = factory.create_chair()
    sofa = factory.create_sofa()

    print(chair.sit_on())
    print(sofa.lie_on())


# Использование
print("Модерн:")
client_code(ModernFurnitureFactory())

print("\nКлассика:")
client_code(ClassicFurnitureFactory())
#
