num1 = input("enter no 1 = ")
num2 = input("enter no 2 = ")

print("press 1 for sum")
print("press 2 for subtract")
print("press 3 for Multiply")
print("press 4 for Division")
selector = input("To Select opration Press Number = ")

if int(selector) == 1:
    sum = int(num1) + int(num2)
    print("Sum of given two numbers is "+str(sum))

elif int(selector) == 2:
    sub = int(num1) - int(num2)
    print("Subtract of given two numbers is "+str(sub))

elif int(selector) == 3:
    mul = int(num1) * int(num2)
    print("Multiplication of given two numbers is "+str(mul))

elif int(selector) == 4:
    div = int(num1) / int(num2)
    print("Division of given two numbers is "+str(div))

else:
    print("invalid input")