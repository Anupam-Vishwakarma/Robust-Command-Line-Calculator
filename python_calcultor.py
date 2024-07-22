class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Error: Division by zero is not allowed"

def get_user_input():
    while True:
        try:
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            return a, b
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operation():
    while True:
        choice = input("What do you want to do? Press\n1 for add,\n2 for sub,\n3 for multiplication,\n4 for division): ")
        if choice in ['1', '2', '3', '4']:
            return int(choice)
        else:
            print("Invalid input. Please enter a valid operation.")

def perform_calculation(cal, operation):
    match operation:
        case 1:
            return cal.add()
        case 2:
            return cal.sub()
        case 3:
            return cal.mul()
        case 4:
            return cal.div()

def display_result(result):
    print(f"Your output is {result}")

def main():
    ready = input("Do you want to use the calculator? (yes/no):\n ")
    if ready.lower() == "yes":
        while True:
            a, b = get_user_input()
            operation = get_operation()
            cal = Calculator(a, b)
            result = perform_calculation(cal, operation)
            display_result(result)
            again = input("Do you want to use the calculator again? (yes/no):\n")
            if again.lower() != "yes":
                print("Thank you!")
                break
    else:
        print("Ok! Thank you.")

if __name__ == "__main__":
    main()