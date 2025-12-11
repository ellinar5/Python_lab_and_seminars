import csv #Используется для чтения и записи CSV-файлов с матрицами

#1. Создать базовый класс WorkerBase
    #Атрибут зарплаты (salary).
    #Методы take_salary(amount), _read_matrix(filename), _print_matrix(matrix).

#2.Создать классы Pupa и Lupa
    #Наследуют WorkerBase.
    #Метод do_work(filename1, filename2):
        #Pupa → сложение матриц.
        #Lupa → вычитание матриц.
    #Вывод результатов на экран.

#3.Создать класс Accountant
    #Метод give_salary(worker, amount):
        #Вызывает у работника take_salary(amount).
    #Работает одинаково с Pupa и Lupa (полиморфизм).

#4.Создать CSV-файлы с матрицами
    #Для тестирования работы do_work.

#5.Протестировать
    #Начисление зарплаты.
    #Выполнение матричных операций.
    #Вывод на экран.


# --- Создание файлов с матрицами ---
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

with open("matrix1.csv", "w", newline="") as f:
    writer = csv.writer(f) #Записываем данные матрицы в файлы
    writer.writerows(matrix1)

with open("matrix2.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(matrix2)


class WorkerBase:
    ''' Общий базовый класс для всех работников (Pupa и Lupa) '''

    def __init__(self):
        self.salary = 0 #salary — счётчик зарплаты

    def take_salary(self, amount: int): #Метод для получения зарплаты
        #Инкрементирует внутренний счётчик salary и выводит результат.
        self.salary += amount
        print(f"{self.__class__.__name__} получил зарплату: {amount}. Общая зарплата: {self.salary}")

    def _read_matrix(self, filename: str): #Приватный метод для чтения матрицы из CSV файла.
        with open(filename, newline='') as f:
            reader = csv.reader(f)
            return [[int(cell) for cell in row] for row in reader]

    def _print_matrix(self, matrix): #Приватный метод для красивого вывода матрицы на экран
        for row in matrix:
            print("\t".join(map(str, row)))
        print()


class Pupa(WorkerBase):

    def do_work(self, filename1: str, filename2: str): #do_work считывает две матрицы и поэлементно их суммирует.

        mat1 = self._read_matrix(filename1)
        mat2 = self._read_matrix(filename2)
        result = [[a + b for a, b in zip(r1, r2)] for r1, r2 in zip(mat1, mat2)]
        print(f"{self.__class__.__name__} результат работы (сложение матриц):")
        self._print_matrix(result)


class Lupa(WorkerBase):

    def do_work(self, filename1: str, filename2: str): #do_work считывает две матрицы и поэлементно их вычитает.

        mat1 = self._read_matrix(filename1)
        mat2 = self._read_matrix(filename2)
        result = [[a - b for a, b in zip(r1, r2)] for r1, r2 in zip(mat1, mat2)]
        print(f"{self.__class__.__name__} результат работы (вычитание матриц):")
        self._print_matrix(result)


class Accountant:

    def give_salary(self, worker, amount: int): #Метод give_salary принимает любого работника (Pupa или Lupa)

        worker.take_salary(amount) #Вызывает метод take_salary для начисления зарплаты


# --- Пример использования ---
pupa_worker = Pupa() #создаем объект Pupa
lupa_worker = Lupa() #создаем объект Lupa
accountant = Accountant() #Accountant начисляет зарплату

#Работники выполняют свои матричные операции

accountant.give_salary(pupa_worker, 1000)
accountant.give_salary(lupa_worker, 1500)

pupa_worker.do_work("matrix1.csv", "matrix2.csv")
lupa_worker.do_work("matrix1.csv", "matrix2.csv")
