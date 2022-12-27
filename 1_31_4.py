'''По заданной формуле члена ряда с номером k составить две программы:
а) программу вычисления суммы первых n членов заданного ряда;
б) программу вычисления всех членов ряда, не меньших заданного числа E.'''



def sum_search():
    n = int(input("Введите целочисленное N: "))

    total_sum = 0

    for k in range(1, n + 1):
        # Находим сумму первых n членов заданного ряда
        total_sum += 2 * k + 1 / (2 * k ** 2 + 1) * k

    return total_sum


def members_of_series():
    e = float(input("Введите число E: "))
    k = 1
    while True:
        # Вычисление всех членов ряда, которые не меньше e
        total = 2 * k + 1 / (2 * k ** 2 + 1) * k
        k += 1
        if total >= e:
            # Если выражение не меньше числа e, то выводим выражение
            print(total)
        else:
            break


if __name__ == "__main__":
    while True:
        try:
            print(sum_search())
            members_of_series()
        except Exception:
            pass
