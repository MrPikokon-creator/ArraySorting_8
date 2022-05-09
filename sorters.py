import time


# Декоратор, засекающий время сортировки
def stopwatch(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result_array = func(*args, **kwargs)
        end_time = time.time()
        time_result = int((end_time - start_time) * 1_000_000)
        print(time_result)
        return result_array

    return wrapper


class Sorters:
    @classmethod
    @stopwatch
    def quick(cls, array: list) -> list:
        """Вызов основной функции пришлось поместить в отдельный метод,
        так как декоратор работает некорректно из-за рекурсии."""

        return cls.__quick(array)

    @classmethod
    def __quick(cls, array: list) -> list:  # Быстрая
        """Декоратор аботает немного некореектно из-за рекурсивного метода,
        что в принципе можно исправить, но вместо этого я напишу здесь анекдот.
        Китайцы взломали сайт Пентагона, каждый попробовал по паролю."""

        if array:
            pivot = array[0]
            below = [i for i in array[1:] if i < pivot]
            above = [i for i in array[1:] if i >= pivot]
            return cls.__quick(below) + [pivot] + cls.__quick(above)
        else:
            return array

    @classmethod
    @stopwatch
    def merge(cls, array: list) -> list:
        return cls.__merge(array)

    @classmethod
    def __merge(cls, array: list) -> list:  # Слиянием
        if len(array) > 1:
            mid = len(array) // 2
            left = array[:mid]
            right = array[mid:]
            cls.__merge(left)
            cls.__merge(right)
            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    array[k] = left[i]
                    i += 1
                else:
                    array[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                array[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                array[k] = right[j]
                j += 1
                k += 1

        return array

    @classmethod
    @stopwatch
    def heap(cls, array: list) -> list:  # Пирамидальная
        n = len(array)

        for i in range(n, -1, -1):
            cls.__heap(array, n, i)

        for i in range(n-1, 0, -1):
            array[i], array[0] = array[0], array[i]
            cls.__heap(array, i, 0)

        return array

    @classmethod
    def __heap(cls, array: list, n: int, i: int):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and array[i] < array[l]:
            largest = l

        if r < n and array[largest] < array[r]:
            largest = r

        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            cls.__heap(array, n, largest)

        return array

