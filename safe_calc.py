import sys
if len(sys.argv) >=3:
    num1 = eval(sys.argv[1])
    num2 = eval(sys.argv[2])
    result = num1 + num2
    print(f"sum of {num1} and {num2} is: {result}")
else:
    print("Error: Please provide 2 numbers!")
