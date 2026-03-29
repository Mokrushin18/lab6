def divide_100(x):
    return 100 / x

try:
    num = float(input("Введите число: "))
    result = divide_100(num)
    print("Результат:", result)
except ValueError:
    print("Ошибка: введено не число")
except ZeroDivisionError:
    print("Ошибка: деление на ноль")
