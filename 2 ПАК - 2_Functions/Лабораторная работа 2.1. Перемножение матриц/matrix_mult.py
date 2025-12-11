import os

def read_matrices_from_file():
    
    # путь к файлу matrix_input.txt рядом со скриптом
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, 'matrix_input.txt')

    with open(input_path, 'r', encoding='utf-8') as file:
        lines = file.readlines() #считаваем все строки матриц

    blocks = ''.join(lines).strip().split('\n\n') #склеваем все матрицы в одной строку, убирает лишние пробелы/переводы строк с начала и конца всей строки, разбиваем матрицы
    matrices = []
    for block in blocks: #перебираем каждую матрицу по очереди
        rows = block.strip().split('\n') #Убираем лишние пробелы с краёв блока и делим по переводам строки.
        matrix = [list(map(int, row.split())) for row in rows] #делим строку на список, каждую строку превращает в число и в конце делаем список
        matrices.append(matrix) #Добавляем готовую матрицу (список списков) в общий список.

    if len(matrices) != 2: #проверям что у нас в файле именно 2 матрицы
        raise ValueError("Файл должен содержать ровно две матрицы")

    return matrices[0], matrices[1]


def multiply_matrices(a, b):
    # Проверка на корректность строк для матрицы, чтобы не оказалось, что это рванный список
    if any(len(row) != len(a[0]) for row in a): #перебираем строки матрицы,сравниваем длину текущий строки с длиной первой строки
        raise ValueError("Матрица A имеет некорректные размеры")
    if any(len(row) != len(b[0]) for row in b):
        raise ValueError("Матрица B имеет некорректные размеры")

    m, n = len(a), len(a[0])
    n2, k = len(b), len(b[0])
    #m — количество строк в матрице a
    #n — количество столбцов в матрице a
    #n2 — количество строк в матрице b
    #k — количество столбцов в матрице b

    if n != n2: #проверка:  Матрица A (m×n) можно умножать на B (n×k) только если n (столбцы A) = n2 (строки B). Иначе умножение не определено.
        raise ValueError("Число столбцов A должно равняться числу строк B")
   
    #матрица для результатов
    c = [[0] * k for _ in range(m)] #Создаём список из m строк, каждая строка — список из k нулей,размер результата всегда m×k (строки первой × столбцы второй)
    for i in range(m):            # перебираем строки A
        for j in range(k):        # перебираем столбцы B
            for r in range(n):    # суммируем произведения
                c[i][j] += a[i][r] * b[r][j]

    return c


def write_matrix_to_file(matrix):
    # аналогично формируем путь к выходному файлу
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, 'matrix_output.txt')

    with open(output_path, 'w', encoding='utf-8') as file:
        for row in matrix: #Перебираем каждую строку матрицы (каждая строка — список чисел)
            file.write(' '.join(map(str, row)) + '\n') #каждое число в row превращаем в строку (иначе join не сможет их соединить).
            #склеиваем элементы списка в одну строку с пробелом между ними.
            


def main():
    a, b = read_matrices_from_file()
    result = multiply_matrices(a, b)
    write_matrix_to_file(result)

if __name__ == "__main__":
    main()