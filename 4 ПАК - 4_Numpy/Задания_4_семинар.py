import argparse
import sys
import numpy as np

# -----------------------------
# 1) Сортировка по частоте
# -----------------------------
def sort_by_frequency(arr, descending=True):
    """
    Возвращает массив той же длины, элементы сгруппированы по значению, группы отсортированы
    по частоте встречаемости (по убыванию, если descending=True).
    При равных частотах порядок групп определяется индексом первого вхождения.
    """
    arr = np.asarray(arr)
    if arr.size == 0:
        return arr.copy()
    uniq, counts, first_idx = np.unique(arr, return_counts=True, return_index=True)
    # keys: последний — первичный. Хотим первичный = -counts (при descending), вторичный = first_idx
    if descending:
        keys = (first_idx, -counts)
    else:
        keys = (-first_idx, counts)
    order = np.lexsort(keys)  # primary = -counts (последний элемент)
    uniq_sorted = uniq[order]
    counts_sorted = counts[order]
    result = np.repeat(uniq_sorted, counts_sorted)
    # длина должна совпадать
    assert result.size == arr.size
    return result

# -----------------------------
# 2) Уникальные цвета
# -----------------------------
def count_unique_colors(image):
    """
    Считает уникальные цвета в изображении shape=(h,w,3), dtype=np.uint8.
    """
    image = np.ascontiguousarray(image)
    pixels = image.reshape(-1, 3)
    uniq = np.unique(pixels, axis=0)
    return uniq.shape[0]

def count_unique_colors_packed(image):
    """
    Быстрая версия: упаковывает RGB в 24-битное целое и считает уникальные значения.
    Работает быстрее для больших изображений.
    """
    arr = image.astype(np.uint32)
    packed = (arr[...,0] << 16) | (arr[...,1] << 8) | arr[...,2]
    uniq = np.unique(packed)
    return uniq.size

# -----------------------------
# 3) Плавающее (скользящее) среднее
# -----------------------------
def moving_average(vec, k):
    """
    Возвращает массив той же длины: первые (k-1) элементы = np.nan, затем скользящие средние длины k.
    """
    vec = np.asarray(vec, dtype=float)
    if k <= 0:
        raise ValueError("k must be >= 1")
    if k == 1:
        return vec.astype(float)
    conv = np.convolve(vec, np.ones(k, dtype=float)/k, mode='valid')
    prefix = np.full(k-1, np.nan, dtype=float)
    return np.concatenate([prefix, conv])

# -----------------------------
# 4) Тройки — стороны треугольника
# -----------------------------
def triangles_from_rows(mat):
    """
    mat: array shape (n,3). Возвращает подмножество строк, где тройки могут быть сторонами треугольника.
    """
    mat = np.asarray(mat, dtype=float)
    if mat.size == 0:
        return mat.reshape(0,3)
    if mat.ndim != 2 or mat.shape[1] != 3:
        raise ValueError("Матрица должна быть формы (n,3)")
    a, b, c = mat[:,0], mat[:,1], mat[:,2]
    mask = (a + b > c) & (a + c > b) & (b + c > a) & (a > 0) & (b > 0) & (c > 0)
    return mat[mask]

# -----------------------------
# 5) Решение системы линейных уравнений A x = b (без np.linalg.solve)
# -----------------------------
def solve_system_by_inverse(A, b):
    """
    Решает A x = b используя np.linalg.inv (не np.linalg.solve).
    Проверяет на сингулярность.
    """
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float)
    if A.shape[0] != A.shape[1]:
        raise ValueError("Матрица A должна быть квадратной")
    det = np.linalg.det(A)
    if np.isclose(det, 0.0):
        raise np.linalg.LinAlgError("Матрица вырождена (det ~ 0), нельзя найти обратную")
    invA = np.linalg.inv(A)
    x = invA.dot(b)
    return x

# -----------------------------
# 6) SVD
# -----------------------------
def svd_decompose(A):
    """
    Возвращает U, S, VT = np.linalg.svd(A)
    """
    A = np.asarray(A, dtype=float)
    U, S, VT = np.linalg.svd(A)
    return U, S, VT







