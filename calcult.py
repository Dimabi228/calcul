# Простая программа для демонстрации операторов
# Используем if-elif-else и обработку ошибок

print("=== Демонстрация операторов Python ===")
print("1 - Арифметические операторы")
print("2 - Операторы сравнения")
print("3 - Логические операторы")
print("4 - Операторы in / not in")
print("5 - Операторы is / is not")
print("0 - Выход")

# Главный цикл программы
while True:
    try:
        # Спрашиваем у пользователя, что он хочет посмотреть
        choice = input("\nВыбери номер (0-5): ")

        if choice == "0":
            print("Выход из программы")
            break   # выходим из цикла while

        # ========== 1. Арифметические операторы ==========
        elif choice == "1":
            print("\n--- Арифметические операторы ---")
            a = float(input("Введи первое число: "))
            b = float(input("Введи второе число: "))

            print("Сложение:       a + b  =", a + b)
            print("Вычитание:      a - b  =", a - b)
            print("Умножение:      a * b  =", a * b)
            print("Деление:        a / b  =", a / b)
            print("Целочисленное:  a // b =", a // b)
            print("Остаток:        a % b  =", a % b)
            print("Степень:        a ** b =", a ** b)

        # ========== 2. Операторы сравнения ==========
        elif choice == "2":
            print("\n--- Операторы сравнения ---")
            x = float(input("Введи первое число: "))
            y = float(input("Введи второе число: "))

            if x == y:
                print(x, "==", y, "→ числа равны")
            else:
                print(x, "==", y, "→ числа НЕ равны")

            if x != y:
                print(x, "!=", y, "→ числа разные")
            else:
                print(x, "!=", y, "→ числа одинаковые")

            if x > y:
                print(x, ">", y, "→ первое больше")
            elif x < y:
                print(x, "<", y, "→ первое меньше")
            else:
                print("Числа равны")

            if x >= y:
                print(x, ">=", y, "→ больше или равно")
            if x <= y:
                print(x, "<=", y, "→ меньше или равно")

        # ========== 3. Логические операторы ==========
        elif choice == "3":
            print("\n--- Логические операторы ---")
            print("Введи True или False")

            a = input("Первое значение (True/False): ")
            b = input("Второе значение (True/False): ")

            # Превращаем текст в настоящие True/False
            a = (a == "True")
            b = (b == "True")

            print("a =", a, "  b =", b)

            if a and b:
                print("a and b → True (оба True)")
            else:
                print("a and b → False")

            if a or b:
                print("a or b  → True (хотя бы одно True)")
            else:
                print("a or b  → False")

            if not a:
                print("not a   → True (a было False)")
            else:
                print("not a   → False (a было True)")

        # ========== 4. Операторы принадлежности ==========
        elif choice == "4":
            print("\n--- Операторы in / not in ---")
            fruits = ["яблоко", "банан", "груша"]
            print("Список фруктов:", fruits)

            fruit = input("Какой фрукт проверить? ")

            if fruit in fruits:
                print(fruit, "есть в списке")
            else:
                print(fruit, "нет в списке")

            if fruit not in fruits:
                print(fruit, "отсутствует в списке")
            else:
                print(fruit, "присутствует в списке")

        # ========== 5. Операторы тождественности ==========
        elif choice == "5":
            print("\n--- Операторы is / is not ---")

            a = [1, 2, 3]
            b = [1, 2, 3]   # новый список (другой объект)
            c = a           # это тот же самый объект

            print("a =", a)
            print("b =", b)
            print("c =", c)

            if a is b:
                print("a is b → True (один объект)")
            else:
                print("a is b → False (разные объекты)")

            if a is c:
                print("a is c → True (один и тот же объект)")
            else:
                print("a is c → False")

            if a is not b:
                print("a is not b → True (это разные объекты)")

        # Если ввели что-то другое
        else:
            print("Ошибка! Введи число от 0 до 5")

    # Обработка ошибок
    except ValueError:
        print("Ошибка! Нужно вводить числа.")
    except ZeroDivisionError:
        print("Ошибка! Нельзя делить на ноль.")
    except Exception as e:
        print("Произошла ошибка:", e)