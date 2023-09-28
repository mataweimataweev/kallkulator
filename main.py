import math

o = True



def main():


    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))

    while (o):
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
        choice = int(input())

        if choice == 11:
            break
        if choice == 1:
            result = num1 + num2
        elif choice == 2:
            result = num1 - num2
        elif choice == 3:
            result = num1 * num2
        elif choice == 4:
            if num2!= 0:
                result = num1 / num2
            else:
                print("Деление на 0 невозможно!!")
        elif choice == 5:
            n = int(input("Введите степень: "))
            result = pow(num1, n)
        elif choice == 6:
            result = math.sqrt(num1)
            if num1 < 0:
                print("Число отрицательное, квадраный корень не определён !!!!")
        elif choice == 7:
            result = math.tan(num1)
        elif choice == 8:
            result = math.sin(num1)
        elif choice == 9:
            result = math.cos(num1)
        elif choice == 10:
            num = int(num1)

            if num <= 0:
                print("Факториал определен только для натуральных чисел!")
            else:
                fact = 1
                for i in range(1, num + 1):
                    fact *= i
                result = fact

    print(f"Результат: result")





