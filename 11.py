class Calculator:
    def __init__(self, number1, operator, number2):
        self.operator = operator
        self.num1 = number1
        self.num2 = number2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2


def main():
    n1 = int(input("First Number : "))
    op = input("Operator : ")
    n2 = int(input("Second Number : "))

    calculator = Calculator(n1, op, n2)

    if calculator.operator == "+":
        print(calculator.add())
    elif calculator.operator == "-":
        print(calculator.subtract())
    elif calculator.operator == "*":
        print(calculator.multiply())
    elif calculator.operator == "/":
        print(calculator.divide())
    else:
        print("Invalid Operator. Try again")
        main()


main()
