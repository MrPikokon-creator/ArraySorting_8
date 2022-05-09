import random
import time

from sorters import Sorters


array_lengths = (100, 1_000, 2_500, 5_000, 10_000)  # Длины генерируемых списков | 1_000 - холостой прогон


def main():
    for length in array_lengths:
        print(f'- - - {length:,d} элементов - - -')
        array = [random.randint(0, length) for i in range(length)]  # Заполнение случайными числами от 0 до длины списка

        print('Быстрая:\t\t', end='')
        Sorters.quick(array.copy())

        print('Слиянием:\t\t', end='')
        Sorters.merge(array.copy())

        print('Пирамидальная:\t', end='')
        Sorters.heap(array.copy())

        print()


if __name__ == '__main__':
    main()