class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def add(self, other):
        assert self.denominator != 0 and other.denominator != 0, "Denominator cannot be zero"
        
        # Find a common denominator
        common_denominator = self.denominator * other.denominator
        
        # Calculate the new numerators
        new_numerator1 = self.numerator * other.denominator
        new_numerator2 = other.numerator * self.denominator
        
        # Add the numerators
        result_numerator = new_numerator1 + new_numerator2
        
        return Fraction(result_numerator, common_denominator)

# Example usage:
fraction1 = Fraction(1, 2)
fraction2 = Fraction(1, 4)
result = fraction1.add(fraction2)
print("Result:", result.numerator, "/", result.denominator)
