class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible!")
        self._celsius = value

temp = Temperature(25)
print(temp.celsius)  # ✅ 25
temp.celsius = -100  # ✅ Allowed
temp.celsius = -300  # ❌ Error: Below absolute zero
