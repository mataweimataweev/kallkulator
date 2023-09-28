import math
o = True
while o:
    try:
        print("Выберите действие:")
        print("1 - сложение")
        print("2 - вычитание")
        print("3 - умножение")
        print("4 - деление")
        print("5 - возведение в степень")
        print("6 - квадратный корень")
        print("7- тангенс")
        print("8 - синус")
        print("9 - косинус ")
        print("10 - факториал")
        print("11 - выход")
        choice = int(input("Введите операцию:"))
        if choice == 1:
            num1 = int(input("Введите первое число: "))
            num2 = int(input("Введите второе число: "))
            result = num1 + num2
            print(result)
        elif choice == 2:
            num1 = int(input("Введите первое число: "))
            num2 = int(input("Введите второе число: "))
            result = num1 - num2
            print(result)
        elif choice == 3:
            num1 = int(input("Введите первое число: "))
            num2 = int(input("Введите второе число: "))
            result = num1 * num2
            print(result)
        elif choice == 4:
            num1 = int(input("Введите первое число: "))
            num2 = int(input("Введите второе число: "))
            if num2 != 0:
                result = num1 / num2
                print(result)
            else:
                print("Деление на 0 невозможно!!")
        elif choice == 5:
            num1 = int(input("Введите первое число: "))
            n = int(input("Введите степень: "))
            result = pow(num1, n)
        elif choice == 6:
            num1 = int(input("Введите первое число: "))
            result = math.sqrt(num1)
            print(result)
            if num1 < 0:
                print("Число отрицательное, квадраный корень не определён !!!!")
        elif choice == 7:
            num1 = int(input("Введите первое число: "))
            result = math.tan(num1)
            print(result)
        elif choice == 8:
            num1 = int(input("Введите первое число: "))
            result = math.sin(num1)
            print(result)
        elif choice == 9:
            num1 = int(input("Введите первое число: "))
            result = math.cos(num1)
            print(result)
        elif choice == 10:
            num1 = int(input("Введите первое число: "))
            num = int(num1)
            if num <= 0:
                print("Факториал определен только для натуральных чисел!")
            else:
                fact = 1
                for i in range(1, num + 1):
                    fact *= i
                result = fact
                print(result)
        elif choice == 11:
            break
    except ValueError:
        print("errrrrror")
print(f"Результат: result")
