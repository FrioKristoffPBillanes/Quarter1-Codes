#icl this is by chatgpt cuz copilot is trash
def check(value):
    try:
        return float(value)
    except ValueError:
        print("Invalid input.")
        exit(0)

num1 = check(input("Enter your first number: "))
num2 = check(input("Enter your second number: "))
num3 = check(input("Enter your third number: "))

result = num1 + num2 + num3
fres = round(result, 2)
print(f"The sum of the numbers is: {result}")