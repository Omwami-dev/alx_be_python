class SimpleCalculator:
    # A simple calculator Class that supports basic arithmetic operations.
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiplication(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            return None
        return a/b