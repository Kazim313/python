# Printing a String
print("Hello, world!")

# Printing Variables
name = "Alice"
age = 30
print("Name:", name)
print("Age:", age)

# Printing Multiple Values
x = 10
y = 20
print("x =", x, "y =", y)

# Printing Formatted Strings (using f-strings)
name = "Bob"
age = 25
print(f"Name: {name}, Age: {age}")

# Printing with String Concatenation
name = "Charlie"
age = 35
print("Name: " + name + ", Age: " + str(age))

# Printing with String Formatting (using the format() method)
name = "David"
age = 40
print("Name: {}, Age: {}".format(name, age))

# Printing with String Formatting (using positional arguments)
name = "Eve"
age = 45
print("Name: {0}, Age: {1}".format(name, age))

# Printing with String Formatting (using named arguments)
name = "Frank"
age = 50
print("Name: {name}, Age: {age}".format(name=name, age=age))

# Printing with String Formatting (using % operator - legacy method)
name = "Grace"
age = 55
print("Name: %s, Age: %d" % (name, age))
