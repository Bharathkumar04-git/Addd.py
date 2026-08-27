import sys

def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    num1 = int(input("Enter First Number :"))
    num2 = int(input("Enter Second Number :"))
    result = add_numbers(num1, num2)
    print("=================================")
    print("Addition Result")
    print("=================================")
    print(f"First Number : {num1}")
    print(f"Second Number: {num2}")
    print(f"Sum : {result}")