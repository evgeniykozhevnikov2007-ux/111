while True:
    try:
        a = float(input("Введіть перше число: "))
        op = input("Введіть операцію (+, -, *, /): ")
        b = float(input("Введіть друге число: "))

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            result = a / b
        else:
            print("Невідома операція")
            continue

        print("Результат:", result)
    except ValueError:
        print("Будь ласка, вводьте числа.")
        continue
    except ZeroDivisionError:
        print("Ділення на нуль неможливе.")
        continue

    again = input("Бажаєте продовжити? (y/yes для продовження): ").lower()
    if again not in ("y", "yes"):
        break
