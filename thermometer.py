class Thermometer:
    def __init__(self, temperature):
        self.temperature = temperature

    def check_temperature(self):
        assert 0 <= self.temperature <= 49, "Temperature is unexpected"
        
        if self.temperature >= 35 and self.temperature <= 38:
            print("Normal temperature")
        else:
            print("Abnormal temperature")

# Example usage:
temperature = 38
thermometer = Thermometer(temperature)

try:
    thermometer.check_temperature()
except AssertionError as e:
    print(e)
