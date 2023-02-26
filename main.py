# Asking the user for a number
def get_number_input(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Неверный формат числа. Попробуйте еще раз.")

# We ask the user for a mathematical operator
def get_operation_input():
    while True:
        oper = input("Введите операцию (+, -, *, /, %): ")
        if oper in ["+", "-", "*", "/", "%"]:
            return oper
        else:
            print("Неверная операция. Попробуйте еще раз.")

# We do mathematical operations depending on the operator
def perform_operation(num1, num2, oper):
    if oper == "+":
        return num1 + num2
    elif oper == "-":
        return num1 - num2
    elif oper == "*":
        return num1 * num2
    elif oper == "/":
        return num1 / num2
    elif oper == "%":
        return num1 % num2

# Updateable function
def update_result(result):
    while True:
        choice = input("\nХотите продолжить? (да/нет): ")
        if choice.lower() == "да":
            num = get_number_input("Введите число: ")
            oper = get_operation_input()
            result = perform_operation(result, num, oper)
            print(f"Результат: {result}")
        elif choice.lower() == "нет":
            return result
        else:
            print("Неверный выбор. Попробуйте еще раз.")

# Function that fires at startup
def start():
    num1 = get_number_input("Введите первое число: ")
    num2 = get_number_input("Введите второе число: ")
    oper = get_operation_input()
    result = perform_operation(num1, num2, oper)
    print(f"\nРезультат: {result}")
    update_result(result)

# Let's start!
start()