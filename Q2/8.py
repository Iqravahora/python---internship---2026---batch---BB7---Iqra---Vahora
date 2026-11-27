# try:
#     a = int(input("Enter first number:"))
#     b = int(input("Enter second number:"))
    
#     result = a/b
    
# except ValueError:
#     print("Invalid input")
    
#     print("Result:", result)
try:
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    
    result = a/b
    
except ValueError:
    print("Invalid output")
    
except ZeroDivisionError:
    print("Cannot divide by zero")
    
    
print("Result:", result)