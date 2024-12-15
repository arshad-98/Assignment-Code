class Calculator:
    def _init_(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def calculate(self):
        if self.operation == 'addition':
            return self.a + self.b
        elif self.operation == 'subtraction':
            return self.a - self.b
        elif self.operation == 'multiplication':
            return self.a * self.b
        elif self.operation == 'division':
            if self.b != 0:
                return self.a / self.b
            else:
                return "Cannot divide by zero."
        else:
            return "Invalid operation."

a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))
operation = input("Enter the operation (addition, subtraction, multiplication, division): ").lower()

calc = Calculator(a, b, operation)

result = calc.calculate()
print(f"The result of the {operation} is: {result}")