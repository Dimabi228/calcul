print("=== КАЛЬКУЛЯТОР ===")
print("1. Арифметические операторы")
print("2. Операторы сравнения")
print("3. Логические операторы")
print("4. Операторы in / not in")
print("5. Операторы is / is not")
print("0. Выход")

while True:
    try:
        choice = input("\nВыбери пункт (0-5): ")

        if choice == "0":
            print("Выход из программы")
            break

#1.Арифметические операторы
        elif choice == "1":
            print("\n--- Арифметические операторы ---")
            a = float(input("Первое число: "))
            b = float(input("Второе число: "))
            op = input("Операция (+, -, *, /, //, %, **): ")

            if op == "+":
                print(a, "+", b, "=", a + b)
            elif op == "-":
                print(a, "-", b, "=", a - b)
            elif op == "*":
                print(a, "*", b, "=", a * b)
            elif op == "/":
                if b == 0:
                    print("Ошибка: деление на ноль!")
                else:
                    print(a, "/", b, "=", a / b)
            elif op == "//":
                if b == 0:
                    print("Ошибка: деление на ноль!")
                else:
                    print(a, "//", b, "=", a // b)
            elif op == "%":
                if b == 0:
                    print("Ошибка: деление на ноль!")
                else:
                    print(a, "%", b, "=", a % b)
            elif op == "**":
                print(a, "**", b, "=", a ** b)
            else:
                print("Неизвестная операция!")

#2. Операторы сравнения 
        elif choice == "2":
            print("\n--- Операторы сравнения ---")
            x = float(input("Первое число: "))
            y = float(input("Второе число: "))

            if x == y:
                print(x, "==", y, "→ True (равны)")
            else:
                print(x, "==", y, "→ False")

            if x != y:
                print(x, "!=", y, "→ True (не равны)")
            else:
                print(x, "!=", y, "→ False")

            if x > y:
                print(x, ">", y, "→ True")
            elif x < y:
                print(x, "<", y, "→ True")
            else:
                print("Числа равны")

            if x >= y:
                print(x, ">=", y, "→ True")
            else:
                print(x, ">=", y, "→ False")

            if x <= y:
                print(x, "<=", y, "→ True")
            else:
                print(x, "<=", y, "→ False")

# 3. Логические операторы
        elif choice == "3":
            print("\n--- Логические операторы ---")
            print("Введи True или False")

            a = input("Первое значение: ") == "True"
            b = input("Второе значение: ") == "True"

            print("a =", a, "  b =", b)

            if a and b:
                print("a and b → True")
            else:
                print("a and b → False")

            if a or b:
                print("a or b → True")
            else:
                print("a or b → False")

            if not a:
                print("not a → True")
            else:
                print("not a → False")

#4. Операторы принадлежности 
        elif choice == "4":
            print("\n--- Операторы in / not in ---")
            numbers = [10, 20, 30, 40, 50]
            print("Список чисел:", numbers)

            num = float(input("Какое число проверить: "))

            if num in numbers:
                print(num, "есть в списке")
            else:
                print(num, "нет в списке")

            if num not in numbers:
                print(num, "отсутствует в списке")
            else:
                print(num, "присутствует в списке")

        elif choice == "5":
            print("\n--- Операторы is / is not ---")

            a = [1, 2, 3]
            b = [1, 2, 3]   
            c = a           

            print("a =", a)
            print("b =", b)
            print("c =", c)

            if a is b:
                print("a is b → True")
            else:
                print("a is b → False (разные объекты)")

            if a is c:
                print("a is c → True (один объект)")
            else:
                print("a is c → False")

            if a is not b:
                print("a is not b → True")
            else:
                print("a is not b → False")

        else:
            print("Ошибка! Введи число от 0 до 5")

    except ValueError:
        print("Ошибка: нужно вводить числа!")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль!")
    except Exception as e:
        print("Произошла ошибка:", e)