import random
import math
import os

#1.Сгенерировать случайное трехзначное число. Вычислить сумму его цифр.
a = 100;
b = 999;
number_1 =  random.randint(a, b) # Присваиваем случайное число от 100 до 999
sum_number_1 = sum(map(int, str(number_1))) # Разбиваем каждое число 

print (f"The grouped number: {number_1}");
print (f"The sum of the numbers: {sum_number_1}")

#2.Сгенерировать случайное число. Вычислить сумму его цифр.
c = 0
d = 9999
number_2 = random.randint(c, d)  # случайное число от 0 до 9999
sum_number_2 = sum(map(int, str(number_2)))

print(f"Random number: {number_2}")
print(f"Sum of its digits: {sum_number_2}")

#3.Задаётся радиус сферы, найти площадь её поверхности и объём.
# 3. Радиус сферы
r = float(input("Enter the radius of the sphere: "))  # радиус
area_sphere = 4 * math.pi * r ** 2   # площадь
volume_sphere = 4/3 * math.pi * r ** 3  # объём

print(f"Area of sphere: {area_sphere}")
print(f"Volume of sphere: {volume_sphere}")

#4.Задаётся год. Определить, является ли он високосным.
# 4. Проверка года
year = int(input("Enter the year: "))
if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("It's not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("It's not a leap year")

#5.Определить все числа из диапазона 1, N, являющиеся простыми.
N = int(input("Enter the number N: ")) # Вводим верхнюю границу диапазона


# Перебираем все числа от 1 до N
for num in range(2, N + 1):  # начинаем с 2, т.к. 1 не простое
    is_prime = True  # флаг простоты
    # Проверяем, есть ли делители у числа num
    for i in range(2, int(num ** 0.5) + 1):  
        if num % i == 0:
            is_prime = False
            break
    if is_prime: # если число простое,то выводим на экран
        print(num, end=" ")
print()

#6.Пользователь делает вклад в размере X рублей сроком на Y лет под 10% годовых (каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты). Вычислить сумму, которая будет на счету пользователя.
x = float(input("Initial amount X (RUB): "))

y = int(input("Term Y (years): "))

rate = 0.10 # Процентная ставка (10% в виде десятичной дроби)

amount = x # Начальная сумма на счету

# Цикл по каждому году вклада
for _ in range(y):
    amount = amount * (1 + rate) # Увеличиваем сумму на 10% каждый год

print(f"Total on the account: {amount:.2f} rubles.")

#7.Вывести все файлы, находящиеся в папке и её подпапках с помощью их абсолютных имён. Имя папки задаётся абсолютным или относительным именем. (можно использовать os.walk())
folder_path = input("Enter the path to the folder: ")  # Вводим путь к папке

# Проходим по папке и её подпапкам
for root, dirs, files in os.walk(folder_path):
    for file in files:
        # Формируем абсолютный путь к файлу
        full_path = os.path.join(os.path.abspath(root), file)
        print(full_path)
