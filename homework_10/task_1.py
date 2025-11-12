class Product:
    def __init__(self, name: str, unit_price: float, unit_sold: int = 0 ):
        self.name = name
        self.unit_price = unit_price
        self.unit_sold = unit_sold
        

    def revenue(self):
        return self.unit_price * self.unit_sold
    
    def __str__(self):
        return (f"{self.name}: {self.unit_sold} units at ${self.unit_price:.2f}")
    

chocolate = Product("korona", 5.5, 10)
bakery = Product("lobiani", 2.5, 20)


print(f"{chocolate}, -- {chocolate.revenue()}")
print(f"{bakery}, -- {bakery.revenue()}")