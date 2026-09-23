print("=" * 50)
print("       КАЛЬКУЛЯТОР С УСЛОВНЫМИ КОНСТРУКЦИЯМИ")
print("=" * 50)

# ========== ОСНОВНОЙ ЦИКЛ ==========
while True:
    print("\nВыберите режим работы:")
    print("1. Арифметические операции (+, -, *, /, //, %, **)")
    print("2. Операторы сравнения (==, !=, >, <, >=, <=)")
    print("3. Логические операторы (and, or, not)")
    print("4. Операторы принадлежности (in, not in)")
    print("5. Операторы тождественности (is, is not)")
    print("0. Выход")

    try:
        mode = input("\nВаш выбор: ").strip()

        #  РЕЖИМ 1: АРИФМЕТИКА 
        if mode == "1":
            print("\n--- Арифметические операции ---")
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            op = input("Введите оператор (+, -, *, /, //, %, **): ").strip()

            if op == "+":
                result = a + b
                print(f"Результат: {a} + {b} = {result}")
            elif op == "-":
                result = a - b
                print(f"Результат: {a} - {b} = {result}")
            elif op == "*":
                result = a * b
                print(f"Результат: {a} * {b} = {result}")
            elif op == "/":
                if b == 0:
                    print("Ошибка: деление на ноль!")
                else:
                    result = a / b
                    print(f"Результат: {a} / {b} = {result}")
            elif op == "//":
                if b == 0:
                    print("Ошибка: целочисленное деление на ноль!")
                else:
                    result = a // b
                    print(f"Результат: {a} // {b} = {result}")
            elif op == "%":
                if b == 0:
                    print("Ошибка: остаток от деления на ноль!")
                else:
                    result = a % b
                    print(f"Результат: {a} % {b} = {result}")
            elif op == "**":
                result = a ** b
                print(f"Результат: {a} ** {b} = {result}")
            else:
                print("Ошибка: неизвестный оператор!")

        #  РЕЖИМ 2: СРАВНЕНИЕ 
        elif mode == "2":
            print("\n--- Операторы сравнения ---")
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            op = input("Введите оператор (==, !=, >, <, >=, <=): ").strip()

            if op == "==":
                result = a == b
                print(f"{a} == {b} → {result}")
            elif op == "!=":
                result = a != b
                print(f"{a} != {b} → {result}")
            elif op == ">":
                result = a > b
                print(f"{a} > {b} → {result}")
            elif op == "<":
                result = a < b
                print(f"{a} < {b} → {result}")
            elif op == ">=":
                result = a >= b
                print(f"{a} >= {b} → {result}")
            elif op == "<=":
                result = a <= b
                print(f"{a} <= {b} → {result}")
            else:
                print("Ошибка: неизвестный оператор сравнения!")

        #  РЕЖИМ 3: ЛОГИЧЕСКИЕ 
        elif mode == "3":
            print("\n--- Логические операторы ---")
            print("Введите два логических значения (True/False или 1/0)")
            
            val1 = input("Первое значение: ").strip().lower()
            val2 = input("Второе значение: ").strip().lower()
            
            # Преобразуем ввод в bool
            if val1 in ("true", "1", "да", "yes"):
                a = True
            elif val1 in ("false", "0", "нет", "no"):
                a = False
            else:
                print("Ошибка: некорректное первое значение!")
                continue
                
            if val2 in ("true", "1", "да", "yes"):
                b = True
            elif val2 in ("false", "0", "нет", "no"):
                b = False
            else:
                print("Ошибка: некорректное второе значение!")
                continue

            op = input("Введите оператор (and, or, not): ").strip().lower()

            if op == "and":
                result = a and b
                print(f"{a} and {b} → {result}")
            elif op == "or":
                result = a or b
                print(f"{a} or {b} → {result}")
            elif op == "not":
                # not применяется только к первому значению
                result = not a
                print(f"not {a} → {result}")
            else:
                print("Ошибка: неизвестный логический оператор!")

        #  РЕЖИМ 4: ПРИНАДЛЕЖНОСТЬ 
        elif mode == "4":
            print("\n--- Операторы принадлежности (in / not in) ---")
            text = input("Введите строку (или список через пробел): ")
            item = input("Что ищем: ")

            # Пробуем как список чисел, иначе как строку
            try:
                sequence = [float(x) for x in text.split()]
                item = float(item)
            except ValueError:
                sequence = text   # работаем со строкой

            op = input("Оператор (in / not in): ").strip().lower()

            if op == "in":
                result = item in sequence
                print(f"{item} in {sequence} → {result}")
            elif op == "not in":
                result = item not in sequence
                print(f"{item} not in {sequence} → {result}")
            else:
                print("Ошибка: используйте 'in' или 'not in'!")

        #  РЕЖИМ 5: ТОЖДЕСТВЕННОСТЬ 
        elif mode == "5":
            print("\n--- Операторы тождественности (is / is not) ---")
            print("Создадим два объекта и сравним их идентичность")
            
            # Демонстрация is / is not
            a = input("Введите значение A: ")
            b = input("Введите значение B (может быть тем же): ")

            # Создаём объекты
            obj1 = a
            obj2 = b
            obj3 = a          # тот же объект, что и obj1

            print(f"\nobj1 = '{obj1}' (id = {id(obj1)})")
            print(f"obj2 = '{obj2}' (id = {id(obj2)})")
            print(f"obj3 = '{obj3}' (id = {id(obj3)})")

            op = input("\nОператор (is / is not): ").strip().lower()

            if op == "is":
                print(f"obj1 is obj2 → {obj1 is obj2}")
                print(f"obj1 is obj3 → {obj1 is obj3}")
            elif op == "is not":
                print(f"obj1 is not obj2 → {obj1 is not obj2}")
                print(f"obj1 is not obj3 → {obj1 is not obj3}")
            else:
                print("Ошибка: используйте 'is' или 'is not'!")

        #  ВЫХОД 
        elif mode == "0":
            print("\nДо свидания!")
            break

        else:
            print("Ошибка: выберите пункт от 0 до 5!")

    except ValueError:
        print("Ошибка: введено не число!")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
