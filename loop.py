"""
A = input("What is your name ")
b = input("what is your age ")
if int(b) < 8:
    print(f"{ A } is a kid")
elif int(b) >= 8 and int(b) < 12:
    print(f"{ A } is school boy")
else :
    print(f"{ A } adult")

"""

#shapes

num = 9
j=0
A= input("what is you name ")
print("You have 6 times to try")

while j <= 5 :
    x = input("put a bat in number ")
    if int(x) == 9:
        print(f"great Dear {A} you win the Bat ")
        break
    j =j+1
else :print(f"sorry dear {A} you lost best of luck for next bat ")
