# Integer conversion
print(int("123"))  # 123
# print(int("12.3"))  # Error
print(int(12.3))  # 12
print(int(True))  # 1
print(int(False))  # 0

# Float conversion
print(float("123"))  # 123.0
print(float("12.3"))  # 12.3
print(float(12))  # 12.0
print(float(True))  # 1.0
print(float(False))  # 0.0

# String conversion
print(str(123))  # '123'
print(str(12.3))  # '12.3'
print(str(True))  # 'True'
print(str(False))  # 'False'
print(str(None))  # 'None'

# Boolean conversion
print(bool(123))  # True
print(bool(0))  # False
print(bool("True"))  # True
print(bool(""))  # False
print(bool([]))  # False




# Get five numbers from the user
num1 = int(input("6"))
num2 = int(input("7"))
num3 = int(input("8 "))
num4 = int(input("9"))
num5 = int(input("10"))

# Perform arithmetic operations
sum_result = num1 + num2 + num3 + num4 + num5
product_result = num1 * num2 * num3 * num4 * num5
difference_result = num1 - num2 - num3 - num4 - num5
division_result = num1 / num2 / num3 / num4 / num5
integer_division_result = num1 // num2 // num3 // num4 // num5
modulus_result = num1 % num2 % num3 % num4 % num5

# Print the results
print("Sum: ", sum_result)
print("Product: ", product_result)
print("Difference: ", difference_result)
print("Division: ", division_result)
print("Integer Division: ", integer_division_result)
print("Modulus: ", modulus_result)