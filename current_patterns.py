"""ПОРОЖДАЮЩИЕ ПАТТЕРНЫ"""


"""
Абстрактная фабрика - abstract factory

Абстрактная фабрика - паттерн, порождающий объекты.
Предоставляет интерфейс для создания семейств взаимосвязанных
или взаимозависимых объектов, не специфицируя их конкретные классы.
"""


class Wiget:
    SIZE = 0


class Window(Wiget):
    SIZE = 5


class PopOver(Wiget):
    SIZE = 2


def abstract_factory(wiget_type):
    if wiget_type == 'window':
        wiget = Window

    else:
        wiget = PopOver

    return wiget()


window = abstract_factory('window')
a = Window()
print(a)
print(window)
popover = abstract_factory('popover')


"""
Строитель - builder

Строитель - паттерн, порождающий объекты.
Отделяет конструирование сложного объекта от его представления, так что
в результате одного и того же процесса конструирования могут получаться разные
представления.
Идеологически это напоминает слои в Docker.
"""


class Home:

    def __init__(self):
        self.rooms = 0
        self.windows = 0
        self.roof = None

    def make_rooms(self, count):
        self.rooms = count

    def make_windows(self, count):
        self.windows = count


class RedRoof:
    COLOR = 'red'


class GreenFoor:
    COLOR = 'green'


def build(rooms, windows, roof):
    my_home = Home()
    my_home.make_rooms(rooms)
    my_home.make_windows(windows)
    if roof == 'red':
        my_home.roof = RedRoof()
    else:
        my_home.roof = GreenFoor()
    return my_home


home = build(5, 10, 'green')


"""
Фабричный метод - factory

Фабричный метод - паттерн, порождающий классы.
Определяет интерфейс для создания объекта, но оставляет подклассам
решение о том, какой класс инстанцировать.
Фабричный метод позволяет классу делегировать инстанцирование подклассам.
Паттерн близок паттерну абстрактной фабрики и нередко является его составляющей.
Отличие от абстрактной фабрики в том, что создаётся инстанс одного и того же
класса.
"""


class Cat:

    def __init__(self, color):
        self.color = color
        print(self.color)

    @classmethod
    def call_black_cat(cls):
        return cls('black')

    @classmethod
    def call_white_cat(cls):
        return cls('white')


cat = Cat.call_black_cat()
cat1 = Cat.call_white_cat()
print (type(cat))
print (type(cat1))


"""
Проторип - prototype

Прототип - паттерн, порождающий объекты.
Задает виды создаваемых объектов с помощью экземпляра-прототипа и создает
новые объекты путем копирования этого прототипа.
"""


class Prototype:

    def __init__(self, **attr_dict):
        self.__dict__.update(attr_dict)

    def copy(self, **attr_dict):
        copy_instance = self.__class__(**self.__dict__)
        copy_instance.__dict__.update(attr_dict)
        return copy_instance


p = Prototype(a=1)
c1 = p.copy(b=2)


"""
Синглтон - singleton

Синглтон - паттерн, порождающий объекты.
Гарантирует, что у класса есть только один экземпляр, и предоставляет к нему
глобальную точку доступа.
"""


class MetaSingleton:

    default = {'value': None}

    def __init__(self):
        self.__dict__ = self.default


class Singleton(MetaSingleton):

    def __init__(self, value=None):
        super().__init__()
        if value:
            self.value = value


s1 = Singleton()
s2 = Singleton()
