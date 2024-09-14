class Appliance:
    def __init__(self, brand):
        self.brand = brand

    def get_info(self):
        print(f"The brand is {self.brand}. ", end="")

class KitchenAppliance(Appliance):
    def __init__(self, brand, power):
        super().__init__(brand)
        self.power = power

    def get_info(self):
        super().get_info()
        print(f"The power of appliance is {self.power}. ", end="")

class Oven(KitchenAppliance):
    def __init__(self, brand, power, temperature_range):
        super().__init__(brand, power)
        self.temperature_range =  temperature_range

    def get_info(self):
        super().get_info()
        print(f" The range of temperature is {self.temperature_range}. ", end="")

class Microwave(KitchenAppliance):
    def __init__(self, brand, power, capacity):
        super().__init__(brand, power)
        self.capacity = capacity

    def get_info(self):
        super().get_info()
        print(f"The capacity of oven is {self.capacity}.")

Whirlpool =Oven("Whirlpool", "3000W", '150-230')
Panasonic = Microwave("Panasonic", 1200,1.2)
Whirlpool.get_info()
Panasonic.get_info()
