import random
#1. Вводится строка. Определить является ли она палиндромом и вывести соответствующее сообщение. - А роза упала на лапу Азора
# 1) Удалите знаки препинания и пробелы
# 2) Приведите к одному регистру
# 3) Сравните строку с перевернутой версией

text_before = input("Enter any suggestion:")

print("\n")

text_after = text_before.replace(' ', '').lower () #удаляет все пробелы и перевод его в нижний регистр


print (f"The entered sentence without spaces {text_after}\n")

reversed_string = text_after[::-1] #переварачиваем строку и перевод его в нижний регистр

print (f"The inverted application received from the user {reversed_string}\n")


if text_after == reversed_string:
    print (f"This offer {text_before}  It is a palindrome.\n")
else:
    print (f"This sentence {text_before} is not a palindrome\n")


#2. В строке, состоящей из слов, разделенных пробелом, найти самое длинное слово
# 1) создать пустой список
# 2) При каждом встречающимся пробеле каждый раз заносить в список
# 3) У каждого слова вывести длинну
# 4)вывести максимальное из списка

text_before = input("Enter any suggestion: ")

print("\n")  

words = []

for word in text_before.split():  # split() делит по пробелам
    words.append(word)

print("Word lengths:")
for word in words:
    print(f"Word: '{word}', length: {len(word)}")

if words:  # проверяем, что список не пуст
    max_len = max(len(word) for word in words)
    print(f"Max word length: {max_len}\n")
else:
    print("The list of words is empty.\n")


#3. Генерируется список случайных целых чисел. Определить, сколько в нем четных чисел, а сколько нечетных.

N = int(input("Enter any length of the list: "))
numbers = [random.randint(-999, 999) for _ in range(N)]
print()

print(f"Generated list: {numbers}\n")


even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:  # если число делится на 2 без остатка
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print(f"The number of even numbers: {even_count} \n")
print(f"The number of odd numbers: {odd_count} \n")

#4. Дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову. 
#   Все слова в словаре различны. Заменить в строке все слова, входящие в словарь, как ключи, на их синонимы.

# словарь синонимов
synonyms = {
"science": "theory",
"oceanarium": "dolphinarium",
"programmer": "software developer"
}

# строка, в которой нужно заменить слова
text = input("enter a sentence with these words - science, oceanarium and programmer: ")
#Программист изучает науку о морских обитателях в океанарии - The programmer studies the science of marine life in the oceanarium

# разбиваем строку на слова
words = text.split()

# заменяем слова, которые есть в словаре как ключи, на их синонимы
new_words = []
for word in words:
    if word in synonyms:
        new_words.append(synonyms[word])
    else:
        new_words.append(word)

# собираем обратно строку
new_text = " ".join(new_words)

print(f"The line after the replacement: {new_text} \n")


#5.Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи. В этой задаче нельзя использовать циклы — используйте рекурсию.
def fib(n):
    #Возвращает n-е число Фибоначчи (нумерация с 0)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# пример использования:
n = int(input("Enter the number n:"))
print()
print(f"{n}-e Fibonacci number = {fib(n)}\n")

#6. Сосчитайте количество строк, слов и букв в произвольном текстовом файле. (слова разделены пробелом, \n не считается символом)
def count_file_stats(filename):
    #Считает количество строк, слов и букв в файле
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    # количество строк
    lines = text.splitlines()
    num_lines = len(lines)

    # количество слов (разделены пробелами)
    words = text.split()
    num_words = len(words)

    # количество букв (убираем \n и пробелы)
    letters_only = [ch for ch in text if ch.isalpha()]
    num_letters = len(letters_only)

    return num_lines, num_words, num_letters


# пример использования
filename = input("Enter the file name: ")
lines, words, letters = count_file_stats(filename)

print(f"Number of Rows: {lines} \n")
print(f"Number of Words: {words} \n")
print(f"Number of Letters: {letters} \n")

#7. Создайте итератор, выводящий бесконечную геометрическую прогрессию. 
#   Параметры прогрессии задаются через аргументы генератора
def geometric_progression(a, r):
    
    #Бесконечная геометрическая прогрессия.
    #a — первый член,
    #r — знаменатель прогрессии.
    
    current = a
    while True:
        yield current  # отдаём текущее значение
        current *= r   # умножаем на знаменатель


# пример использования:
gp = geometric_progression(2, 3)  # 2, 6, 18, 54, ...

for i in range(10):  # выводим первые 10 членов
    print(f"Endless geometric progression: {next(gp)}")
