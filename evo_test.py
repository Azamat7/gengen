"""
Not a unittest for now
"""
from evo import EvoGen
from generic import Float, Int, List


def f(a):
    """
    Function that accepts float number
    """
    return a + 2


def insertion_sort(tmp):
    arr = tmp[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def bubble_sort(tmp):
    aux = tmp[:]
    while True:
        relaxed = False
        for i in range(len(aux) - 1):
            if aux[i] > aux[i + 1]:
                t = aux[i]
                aux[i] = aux[i + 1]
                aux[i + 1] = t
                relaxed = True
        if not relaxed:
            break
    return aux


def main():
    e = EvoGen(5, 300)

    worst, t = e.generate_worst_case(insertion_sort,
                                     List(1000, 3000, Int(-400, 400)))
    print(worst, t)

    worst, t = e.generate_worst_case(bubble_sort,
                                     List(1000, 3000, Int(-400, 400)))
    print(worst, t)


if __name__ == "__main__":
    main()
