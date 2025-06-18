# A division calculator that can handle errors like division by zero and non-numeric inputs
# Create two python modules:
# 1. robust_division_calculator
#2. main.py

def safe_divide(numerator,denominator):
     try:
          num = float(numerator)
          den = float(denominator)
          if den == 0:
               return "Error: can not divide by zero."
          return f"The result of the division is {num / den}"
     except ValueError:
          return "Error: Please enter numeric values only."