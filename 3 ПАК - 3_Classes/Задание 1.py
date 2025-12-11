#1. Перенести все операции по работе с количеством объектов из класса Apple в класс Item
#ИДЕЯ РЕШЕНИЯ ЗАДАЧИ:
#1. Перенести  в класс Item работус количеством объектов и чтобы это решение было уневерсальное (у наследников не будет дублирования)
#2. В Item должно хранится текущие и максимальное количество

#2.Дополнить класс Item остальными опрерациями сравнения (>, <=, >=, ==), вычитания, а также выполнение операций +=, *=, -=. Все изменения количества должны быть в переделах [0, max_count]
#ИДЕЯ РЕШЕНИЯ ЗАДАЧИ:
#1.Добавим магические методы:

#__eq__, __lt__, __le__, __gt__, __ge__ → сравнение по количеству.

#__sub__, __isub__ → вычитание.

#__add__, __iadd__ → сложение.

#__mul__, __imul__ → умножение количества.

#При этом все операции должны работать только в пределах [0, max_count].


#3.Создать ещё 2 класса съедобных фруктов и 2 класса съедобных не фруктов


#4. Создать класс Inventory, который содержит в себе список фиксированной длины. Заполнить его None. Доступ в ячейку осуществляется по индексу.
#4.1 Добавить возможность добавлять в него съедобные объекты в о5пределённые ячейки.
#4.2 Добавить возможность уменьшать количество объектов в списке.
#4.3 При достижении нуля, объект удаляется из инвентаря.

#ИДЕЯ РЕШЕНИЯ ЗАДАЧИ:
#1.Класс Inventory имеет фиксированную длину, хранит None или объекты еды.



class Item:
    """Базовый класс для предметов.
    Отвечает за хранение и управление количеством экземпляров.
    """

    def __init__(self, count=0, max_count=16):
        # текущее и максимальное допустимое количество
        self._count = count
        self._max_count = max_count

    # --- Свойства ---
    @property #Значения хранятся как приватные атрибуты
    def count(self): #Позволяет безопасно получать количество предметов через item.count
        """Текущее количество экземпляров."""
        return self._count

    @count.setter
    def count(self, val):
        """Безопасно установить новое количество (с проверкой лимита)."""
        if 0 <= val <= self._max_count:
            self._count = val
        else:
            raise ValueError(
                f"Количество {val} вне допустимого диапазона 0…{self._max_count}" #проверка на границы 0…max
            )

    @property
    def max_count(self):
        """Максимальное количество экземпляров."""
        return self._max_count

    @property #Только для чтения: максимальное количество предметов
    def is_empty(self):
        """True, если предметов нет."""
        return self._count == 0

    @property #Только для чтения: максимальное количество предметов
    def is_full(self):
        """True, если достигнут максимум."""
        return self._count == self._max_count

    # --- Методы изменения количества ---

    def update_count(self, val):
        """Установить количество через метод (аналог сеттера)."""
        self.count = val
        return True

    def increase_count(self, n=1):
        """Увеличить количество (не больше max_count)."""
        self.count = min(self._count + n, self._max_count)

    def decrease_count(self, n=1):
        """Уменьшить количество (не меньше 0)."""
        self.count = max(self._count - n, 0)

    def reset_count(self, to_max=False):
        """Сбросить количество (по умолчанию в ноль, можно в max)."""
        self.count = self._max_count if to_max else 0

    # --- Магические методы сравнения ---

    def __len__(self): #len(obj) возвращает текущее количество
        return self._count
    
    def __eq__ (self,other): #==
        #Позволяют сравнивать предметы по количеству (count), Сравнивает либо с другим Item, либо с числом
        return self.count == (other.count if isinstance(other, Item) else other)
    
    def __lt__(self, other):#<
        return self.count < (other.count if isinstance(other, Item) else other)

    def __le__(self, other):#<=
        return self.count <= (other.count if isinstance(other, Item) else other)

    def __gt__(self, other): #>
        return self.count > (other.count if isinstance(other, Item) else other)

    def __ge__(self, other): #>=
        return self.count >= (other.count if isinstance(other, Item) else other)
    
    def __ne__(self, other):
        """Неравенство (для корректной работы !=)."""
        return not self == other


    # --- Арифметические операции ---
    # Позволяют выполнять +, -, * с объектами Item или числами.

    def __add__(self, other):
        """Сложение (возвращает новый объект)."""
        #Возвращает новый объект того же класса
        #Ограничивает результат max_count
        value = self.count + (other.count if isinstance(other, Item) else other)
        return self.__class__(count=min(value, self.max_count), max_count=self.max_count)

    def __iadd__(self, other):
        """Сложение с присваиванием."""
        value = self.count + (other.count if isinstance(other, Item) else other)
        self.count = min(value, self.max_count)
        return self

    def __sub__(self, other):
        """Вычитание (возвращает новый объект)."""
        value = self.count - (other.count if isinstance(other, Item) else other)
        return self.__class__(count=max(value, 0), max_count=self.max_count)

    def __isub__(self, other):
        """Вычитание с присваиванием."""
        value = self.count - (other.count if isinstance(other, Item) else other)
        self.count = max(value, 0)
        return self

    def __mul__(self, other):
        """Умножение (возвращает новый объект)."""
        value = self.count * (other.count if isinstance(other, Item) else other)
        return self.__class__(count=min(value, self.max_count), max_count=self.max_count)

    def __imul__(self, other):
        """Умножение с присваиванием."""
        value = self.count * (other.count if isinstance(other, Item) else other)
        self.count = min(value, self.max_count)
        return self

    
class Fruit(Item):
    def __init__(self, ripe=True, **kwargs):
        super().__init__(**kwargs)
        self._ripe = ripe #спелость фрукта


class Food(Item):
    def __init__(self, saturation, **kwargs):
        super().__init__(**kwargs)
        self._saturation = saturation #насыщенность пищи энергией
        
    @property #True, если еда пригодна к употреблению.
    def eatable(self):
        return self._saturation > 0
    

class Pineapple (Fruit, Food): 

    def __init__(self, ripe=True, count=1, max_count=32, color='brown-green', saturation=8): 
        super().__init__(saturation=saturation, ripe=ripe, count=count, max_count=max_count) 
        self._color = color 

    @property 
    def color(self):
        return self._color 

    def __str__(self): #Позволяет печатать объект как строку
        """ Вызов как строки """ 
            
        return f'Stack of {self.count} {self.color} pineapple' 

class Pear (Fruit, Food): 

    def __init__(self, ripe=True, count=1, max_count=32, color='green', saturation=8): 
        super().__init__(saturation=saturation, ripe=ripe, count=count, max_count=max_count) 
        self._color = color 
    
    @property 
    def color(self):
        return self._color 

    def __str__(self): #Позволяет печатать объект как строку

        """ Вызов как строки """ 
            
        return f'Stack of {self.count} {self.color} pear' 


class Carrot (Food): 

    def __init__(self, count=1, max_count=32, saturation=11): 
        super().__init__(saturation=saturation, count=count, max_count=max_count)  

    def __str__(self): #вПозволяет печатать объект как строку
        """ Вызов как строки """ 
            
        return f'Stack of {self.count} carrot' 

class Bread (Food): 

    def __init__(self, count=1, max_count=32, saturation=20): 
        super().__init__(saturation=saturation, count=count, max_count=max_count)  

    def __str__(self): #Позволяет печатать объект как строку

        """ Вызов как строки """ 
            
        return f'Stack of {self.count} bread' 

class Inventory:
    def __init__(self, size=5): #Хранит предметы в ячейках
        self._slots = [None] * size #size — количество слотов

    def __getitem__(self, index): #позволяет писать inv[i]
        return self._slots[index]

    def __setitem__(self, index, item): #позволяет писать inv[i]
        if isinstance(item, Item) or item is None:
            self._slots[index] = item
        else:
            raise ValueError("Можно добавлять только объекты Item или None")

    def add_item(self, index, item):
        """Добавить объект в ячейку."""
        #Добавляет предмет в слот
        #Если в слоте тот же тип → суммирует количество.
        #Если слот занят другим предметом → ошибка.

        if self._slots[index] is None:
            self._slots[index] = item
        elif isinstance(self._slots[index], item.__class__):
            # если тот же тип — суммируем количество
            self._slots[index] += item
        else:
            raise ValueError("Ячейка занята другим предметом!")

    def decrease_item(self, index, n=1):
        """Уменьшить количество предметов в ячейке."""
        #Уменьшает количество предметов.
        #Если стало пусто → ставит None.

        if self._slots[index] is not None:
            self._slots[index].decrease_count(n)
            if self._slots[index].is_empty:
                self._slots[index] = None

    def __str__(self): #Выводит все предметы инвентаря в читаемом виде
        return str([str(item) if item else None for item in self._slots])

# Магические методы python
class Apple(Fruit, Food): 

    def __init__(self, ripe=True, count=1, max_count=32, color='green', saturation=10): 
        super().__init__(saturation=saturation, ripe=ripe, count=count, max_count=max_count) 
        self._color = color 

    @property 
    def color(self):
        return self._color 
        
    @property 
    def eatable(self): 
        return super().eatable and self._ripe 
        
    def __call__(self): #делают объект экземпляра класса похожим на функцию, вызывая уменьшение количества яблок при съедании
        """ Вызов как функции """
        if self.eatable:
            new_count = max(self.count - 1, 0) #седаем одно яблоко
            self.update_count(new_count)

    def __str__(self): #возвращает строковое представление яблока ("Stack of X red/green apples").

        """ Вызов как строки """ 
            
        return f'Stack of {self.count} {self.color} apples' 
                 
                 
    def __len__(self): #позволяет получать длину объекта как его количество экземпляров
         
        """ Получение длины объекта """ 
         
        return self.count 
        
apple = Apple(True, count=5, color='red') 
pineapple = Pineapple(count=3) 
bread = Bread(count=2) 

inv = Inventory(size=3) 
inv.add_item(0, apple) 
inv.add_item(1, pineapple) 
inv.add_item(2, bread) 
print(inv) # [Stack of 5 red apples, Stack of 3 bananas, Stack of 2 bread] 
inv.decrease_item(0, 2) 
print(inv) # [Stack of 3 red apples, Stack of 3 bananas, Stack of 2 bread]

a = Pineapple(True, count=5)
b = Pineapple(True, count=3)
c = 4
d = Apple(True, count=5)
e = Apple(True, count=10)


print(a > b)  # True
print(a < c)  # False
print(a == 5) # True
print(a != b) # True
print(a + b)
print(d + e)
