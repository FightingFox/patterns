"""ПАТТЕРНЫ ПОВЕДЕНИЯ"""

"""
Цепочка обязанностей - chain of responsibility

Цепочка обязанностей - паттерн поведения объектов.
Позволяет избежать привязки отправителя запроса к его получателю, давая
шанс обработать запрос нескольким объектам. Связывает объекты-получатели
в цепочку и передает запрос вдоль этой цепочки, пока его не обработают.
"""


class Human:

    favorite_food = None
    next_human = None

    def eating(self, eat):
        if eat == self.favorite_food:
            return f'{self.__class__} eat it'
        else:
            if self.next_human is not None:
                return self.next_human.eating(eat)
            else:
                return 'Nobody eat it'


class Tom(Human):

    favorite_food = 'egg'


class Ann(Human):

    favorite_food = 'cheese'


human_1 = Tom()
human_2 = Ann()
human_1.next_human = human_2

human_1.eating('egg')
human_1.eating('cheese')
human_1.eating('frog')


"""
Команда - command

Команда - паттерн поведения объектов.
Инкапсулирует запрос как объект, позволяя тем самым задавать параметры
клиентов для обработки соответствующих запросов, ставить запросы в очередь
или протоколировать их, а также поддерживать отмену операций.
"""


class Button:

    def __init__(self, command):

        self.command = command

    def right_mouse_button(self):
        return self.command.right()

    def left_mouse_button(self):
        return self.command.left()


class Window:

    @staticmethod
    def left():
        return 'Left click on window'

    @staticmethod
    def right():
        return 'Right click on window'


class Popover:

    @staticmethod
    def left():
        return 'Left click on popover'

    @staticmethod
    def right():
        return 'Right click on popover'


b1 = Button(command=Window)
b2 = Button(command=Popover)
b1.left_mouse_button()
b1.right_mouse_button()
b2.left_mouse_button()
b2.right_mouse_button()


# """
# Интерпретатор - interpreter
#
# Интерпретатор - паттерн поведения классов.
# Для заданного языка определяет представление его грамматики,
# а также интерпретатор предложений этого языка.
# Суть идеи - микро-язык внутри языка.
# """


class InterpreterContext:

    def __init__(self, expression):
        self.expression_tiems = expression.split(sep=' ')

    @staticmethod
    def _eq(x, y):
        return x == y

    def interpret(self):

        for num, exp in enumerate(self.expression_tiems):
            if exp == 'eq':
                return self._eq(
                    self.expression_tiems[num-1],
                    self.expression_tiems[num+1]
                )


context = InterpreterContext('1 eq 1')
context.interpret()


"""
Итератор - iterator

Итератор - паттерн поведения объектов.
Предоставляет способ последовательного доступа ко всем элементам 
составного объекта, не раскрывая его внутреннего представления.
"""


class Cursor:

    def __init__(self, iterable_object):
        self.iterable_object = iterable_object

    @staticmethod
    def __sq(digit):
        return digit * digit

    def sq_iter(self):
        yield from [self.__sq(digit) for digit in self.iterable_object]


c = Cursor(range(10))
c.sq_iter()


# """
# Посредник - mediator
#
# Посредник - паттерн поведения объектов.
# Определяет объект, инкапсулирующий способ взаимодействия множества
# объектов. Посредник обеспечивает слабую связанность системы,
# избавляя объекты от необходимости явно ссылаться друг на друга и
# позволяя тем самым независимо изменять взаимодействия между ними.
# """


class Pizza:

    slise = 6


class Human:

    def __init__(self, name):
        self.name = name

    def eat(self):
        Pizza.slise -= 1
        return f'{self.name} eat pizza'

    def make(self):
        Pizza.slise += 1
        return f'{self.name} make pizza'


tom = Human('Tom')
ann = Human('Ann')
mario = Human('Mario')
tom.eat()
mario.make()
ann.eat()


# """
# Хранитель - memento
#
# Хранитель - паттерн поведения объектов.
# Не нарушая инкапсуляции, фиксирует и выносит за пределы объекта его
# внутреннее состояние так, чтобы позднее можно было восстановить в нем объект.
# """


class Memory:

    def __init__(self):
        self.memory_dict = {}

    def save(self, obj: object):
        self.memory_dict = obj.__dict__.copy()

    def load(self, obj: object):
        obj.__dict__ = self.memory_dict
        self.memory_dict = {}


class Code:

    def __init__(self, data):
        self.data = data


code = Code(1)
memory = Memory()
memory.save(code)
code.data = 2
memory.load(code)


# """
# Наблюдатель - observer
#
# Наблюдатель - паттерн поведения объектов.
# Определяет зависимость типа «один ко многим» между объектами таким образом,
# что при изменении состояния одного объекта все зависящие от него оповещаются
# об этом и автоматически обновляются.
#
# Реализация так себе, надо доработать.
# """
#

class Observer:

    value = 1

    def __init__(self, value, observers=()):
        self.value = value
        self.observers = observers

    def update(self):
        for obj in self.observers:
            obj.value = self.value


class Table(Observer):

    def get_value(self):
        return self.value


t1 = Table(1)
t2 = Table(1, (t1, ))
t1.get_value()
t2.get_value()
t2.value = 2
t2.update()
t1.get_value()
t2.get_value()


# """
# Состояние - state
#
# Состояние - паттерн поведения объектов.
# Позволяет объекту варьировать свое поведение в зависимости от внутреннего
# состояния. Извне создается впечатление, что изменился класс объекта.
# """


class Door:

    def __init__(self, open_d, close_d):
        self.open = open_d(self)
        self.close = close_d(self)
        self.methods = self.close

    def switch_method(self):
        self.methods.activate()
        return self.methods.status


class OpenDoor:

    status = 'closed'

    def __init__(self, door: Door):
        self.door = door

    def activate(self):
        self.door.methods = self.door.close


class ClosedDoor:

    status = 'open'

    def __init__(self, door: Door):
        self.door = door

    def activate(self):
        self.door.methods = self.door.open


door = Door(OpenDoor, ClosedDoor)
door.switch_method()
door.switch_method()
door.switch_method()
door.switch_method()


# """
# Стратегия - strategy
#
# Стратегия - паттерн поведения объектов.
# Определяет семейство алгоритмов, инкапсулирует каждый из них и делает их
# взаимозаменяемыми. Стратегия позволяет изменять алгоритмы независимо от
# клиентов, которые ими пользуются.
# """


class TextParser:

    def __init__(self, text):
        self.text = text

    def parse(self, strategy):

        return strategy(self) if strategy else self.text


# Алгоритм 1
def split_semicolon(obj: TextParser):

    return obj.text.split(';')


# Алгоритм 2
def split_comma(obj: TextParser):

    return obj.text.split(',')


text = TextParser('qwer,ty;qwer,ty')
text.parse(split_semicolon)
text.parse(split_comma)


# """
# Шаблонный метод - template method
#
# Шаблонный метод — паттерн поведения классов.
# Шаблонный метод определяет основу алгоритма и позволяет подклассам
# переопределить некоторые шаги алгоритма, не изменяя его структуру в целом.
# """
#

# Единственный настраиваемый алгоритм
class Algorithm:

    def __init__(
            self,
            foo_1,
            foo_2,
            foo_3,
            value
                 ):

        self.foo_1 = foo_1
        self.foo_2 = foo_2
        self.foo_3 = foo_3
        self.value = value

    def run(self):

        result = self.foo_1(self.value)
        result = self.foo_2(result)
        result = self.foo_3(result)

        return result


algorithm = Algorithm(
    lambda x: x*10,
    lambda x: x*100,
    lambda x: x*1000,
    1
)
algorithm.run()


# """
# Посетитель - visitor
#
# Посетитель - паттерн поведения объектов.
# Описывает операцию, выполняемую с каждым объектом из некоторой структуры.
# Паттерн посетитель позволяет определить новую операцию, не изменяя
# классы этих объектов.
# """


class Work:

    def visit(self, obj: object):

        name = f'worker_{obj.__class__.__name__.lower()}'
        method = getattr(self, name, None)
        return method() if method else 'It not worker'

    def worker_tom(self):
        return 'It Tom'


class Tom:
    pass


class Ann:
    pass


tom = Tom()
ann = Ann()
visit_work = Work()
visit_work.visit(tom)
visit_work.visit(ann)
