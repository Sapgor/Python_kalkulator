import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: деление на ноль"
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Ошибка: извлечение корня из отрицательного числа"
    return math.sqrt(x)

def factorial(x):
    if x < 0:
        return "Ошибка: факториал отрицательного числа не определен"
    if x == 0:
        return 1
    return x * factorial(x - 1)

def sine(x):
    return math.sin(x)

def cosine(x):
    return math.cos(x)

def tangent(x):
    if abs(math.cos(x)) < 1e-15:
        return "Ошибка: тангенс не существует для угла, где косинус близок к нулю"
    return math.tan(x)

while True:
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Квадратный корень")
    print("7. Факториал")
    print("8. Синус")
    print("9. Косинус")
    print("10. Тангенс")
    print("0. Выход")

    choice = input("Введите номер операции: ")

    if choice == '0':
        break

    if choice in ('1', '2', '3', '4', '5'):
        while True:
            try:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
                break
            except ValueError:
                print("Ошибка: введено не число")
    elif choice in ('6', '7', '8', '9', '10'):
        while True:
            try:
                num1 = float(input("Введите число: "))
                break
            except ValueError:
                print("Ошибка: введено не число")

    if choice == '1':
        print("Результат:", add(num1, num2))
    elif choice == '2':
        print("Результат:", subtract(num1, num2))
    elif choice == '3':
        print("Результат:", multiply(num1, num2))
    elif choice == '4':
         print("Результат:", divide(num1, num2))
    elif choice == '5':
        print("Результат:", power(num1, num2))
    elif choice == '6':
        print("Результат:", square_root(num1))
    elif choice == '7':
        print("Результат:", factorial(int(num1)))
    elif choice == '8':
        print("Результат:", sine(num1))
    elif choice == '9':
        print("Результат:", cosine(num1))
    elif choice == '10':
        print("Результат:", tangent(num1))
    else:
        print("Ошибка: Неверная операция")