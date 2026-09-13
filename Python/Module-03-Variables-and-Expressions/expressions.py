# Practical script demonstrating variable types, mathematical operations, and input handling

# 1. Variable Assignment & Type Inspection
integer_var = 42
float_var = 98.6
string_var = "Python for Everybody"

print("Integer Type:", type(integer_var))
print("Float Type:", type(float_var))
print("String Type:", type(string_var))

# 2. Arithmetic Operations
a = 15
b = 4

print("Addition:", a + b)             # 19
print("Standard Division:", a / b)      # 3.75
print("Integer Division:", a // b)     # 3
print("Modulo (Remainder):", a % b)     # 3
print("Exponentiation:", a ** b)        # 50625

# 3. Interactive Input & Type Conversion
raw_hours = input("Enter Worked Hours: ")
raw_rate = input("Enter Hourly Rate: ")

# Convert string inputs to floating point numbers for math
hours = float(raw_hours)
rate = float(raw_rate)

gross_pay = hours * rate
print("Total Calculated Pay:", gross_pay)