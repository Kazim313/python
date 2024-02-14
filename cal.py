class Calculator:
  class Calculator:
    def __init__(self):
        pass

    def add(self, first_number, second_number):
       
        return first_number + second_number

    def subtract(self, minuend, subtrahend):
      
        return minuend - subtrahend

    def multiply(self, multiplicand, multiplier):
       
        return multiplicand * multiplier

    def divide(self, dividend, divisor):
    
        if divisor == 0:
            raise ValueError("Cannot divide by zero!")
        return dividend / divisor


# Calling the main function
if __name__ == "__main__":
    main()


    def add(self, first_number, second_number):
      
        return first_number + second_number

    def subtract(self, minuend, subtrahend):
      
        return minuend - subtrahend

    def multiply(self, multiplicand, multiplier):
       
        return multiplicand * multiplier

    def divide(self, dividend, divisor):
       
        if divisor == 0:
            raise ValueError("Cannot divide by zero!")
        return dividend / divisor

# Main function
def main():
    # Creating an instance of the Calculator class
    calc = Calculator()

    # Example calculations
    first_number =int(input("add first nbr"))
    second_number= input()

    # Performing calculations and printing results
    print("Sum:", calc.add(first_number, second_number))
    print("Difference:", calc.subtract(first_number, second_number))
    print("Product:", calc.multiply(first_number, second_number))
    print("Quotient:", calc.divide(first_number, second_number))

# Calling the main function
if __name__ == "__main__":
    main()
