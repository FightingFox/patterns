# """СТРУКТУРНЫЕ ПАТТЕРНЫ"""
#
# """
# Адаптер - adapter
#
# Адаптер - паттерн, структурирующий классы и объекты.
# Преобразует интерфейс одного класса в интерфейс другого, который
# ожидают клиенты.
# Адаптер обеспечивает совместную работу классов с
# несовместимыми интерфейсами, которая без него была бы невозможна.
# """
#
#
# class Cat:
#
#     @staticmethod
#     def meow():
#         return 'meow'
#
#
# class Dog:
#
#     @staticmethod
#     def woof():
#         return 'woof'
#
#
# class Adapter:
#
#     def __init__(self, obj, **methods):
#         self.obj = obj
#         self.__dict__.update(methods)
#
#
# Cat.meow()
# meow_dog = Adapter(Dog, meow=Cat.meow)
# meow_dog.meow()
#
#
# """
# Мост - bridge
#
# Мост - паттерн, структурирующий объекты.
# Отделяет абстракцию от её реализации так, чтобы то и другое можно было
# изменять независимо.
# """
#
#
# class Interface1:
#
#     @staticmethod
#     def foo():
#         return 1
#
#
# class Interface2:
#
#     @staticmethod
#     def foo():
#         return 2
#
#
# class Bridge:
#
#     def __init__(self, interface):
#         self.interface = interface
#
#     def foo(self):
#         return self.interface.foo()
#
#
# u1 = Bridge(Interface1)
# u2 = Bridge(Interface2)
# print (u1.foo())
# print(u2.foo())


"""
Компоновщик - composite

Компоновщик - паттерн, структурирующий объекты.
Компонует объекты в древовидные структуры для представления иерархий
часть-целое. Позволяет клиентам единообразно трактовать индивидуальные и
составные объекты.
"""


class Text:

    def __init__(self, text):
        self.text = text

    def print(self):
        return self.text


class Texts(Text):

    def __init__(self, text):
        self.texts = [Text(text)]

    def print(self):
        for text in self.texts:
            text.print()

    def extend(self, data):
        self.texts.extend(data)


t = Text('single_1')
tt = Texts('single_2')
tt.extend((t, Text('single_3')))

#
# """
# Декоратор - decorator
#
# Декоратор - паттерн, структурирующий объекты.
# Динамически добавляет объекту новые обязанности.
# Является гибкой альтернативой порождению подклассов
# с целью расширения функциональности.
# """
#
#
# class WrappedObject:
#
#     def __init__(self, value):
#         self.value = value
#
#     def read(self):
#         return self.value
#
#
# class Wrapper(WrappedObject):
#
#     def __init__(self, value: WrappedObject):
#
#         self.value = f'----{value.read()}----'
#
#
# wo = WrappedObject('text')
# w = Wrapper(wo)
#
#
# """
# Фассад - facade
#
# Фасад - паттерн, структурирующий объекты.
# Предоставляет унифицированный интерфейс вместо набора интерфейсов
# некоторой подсистемы.
# Фасад определяет интерфейс более высокого уровня,
# который упрощает использование подсистемы.
# """
#
#
# class Egg:
#
#     @staticmethod
#     def buy():
#         return 'Egg buyed'
#
#     @staticmethod
#     def crush():
#         return 'Egg crushed'
#
#
# class Cheese:
#
#     @staticmethod
#     def buy():
#         return 'Cheese buyed'
#
#     @staticmethod
#     def grate():
#         return 'Cheese grated'
#
#
# class FriedEggsFacade:
#
#     def __init__(self,
#                  egg: Egg,
#                  cheese: Cheese):
#         self.egg_1 = egg()
#         self.egg_2 = egg()
#         self.cheese = cheese()
#
#     def make_fried_eggs(self):
#
#         pan = [
#             self.egg_1.crush(),
#             self.egg_2.crush(),
#             self.cheese.grate()
#         ]
#
#         return pan
#
#
# f = FriedEggsFacade(Egg, Cheese)
# f.make_fried_eggs()
#
#
# # """
# # Приспособленец - flyweight
# #
# # Приспособленец - паттерн, структурирующий объекты.
# # Использует разделение для эффективной поддержки множества мелких
# # объектов.
# # """
#
#
# class Symbol:
#     pool = {}
#
#     def __new__(cls, value):
#         if pool_item := cls.pool.get(value):
#             # print('From pool')
#             return pool_item
#         else:
#             # print('New object')
#             new_object = object.__new__(Symbol)
#             new_object.value = value
#             cls.pool.update({value: new_object})
#             return cls
#
#
# s1 = Symbol(1)
# s2 = Symbol(2)
# s3 = Symbol(1)
# s4 = Symbol(2)
#
#
# # """
# # Заместитель - proxy
# #
# # Заместитель - паттерн, структурирующий объекты.
# # Является суррогатом другого объекта и контролирует доступ к нему.
# # """
#
#
# class Image:
#
#     def load(self):
#         return 'Very long loading'
#
#     def see(self, user):
#         return self.load()
#
#
# class ProxyPreview(Image):
#
#     def load(self):
#         return 'Fast loading'
#
#     def see(self, user):
#         if user == 'admin':
#             return super().load()
#         else:
#             return 'Failed permissions'
#
#
# real = Image()
# proxy = ProxyPreview()
# real.load()
# proxy.load()
# real.see('admin')
# proxy.see('admin')
# proxy.see('not_admin')
#
#
#
