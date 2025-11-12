from task_1 import Product 

class PerishableProduct(Product):
    def __init__(self, name, unit_price, expiry_date, unit_sold = 0):
        super().__init__(name, unit_price, unit_sold,)
        self.expiry_date = expiry_date

    def is_expired(self, today):
        return today > self.expiry_date
        


    def __str__(self):
        return (f"{self.name}: {self.unit_sold} units at ${self.unit_price:.2f}, expires on {self.expiry_date}")    
    
some_product = PerishableProduct("milk", 6.7,"2025-11-24", 10)
print(some_product, some_product.is_expired("2025-11-25"))
print(some_product, some_product.is_expired("2025-11-07"))