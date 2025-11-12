
from pathlib import Path
BASE_DIRE = Path(__file__).parent.parent

data_path = BASE_DIRE / "homework_10" / "sample.csv" 
# some_product = PerishableProduct(2.5, 5, "2025-11-24")
# print(some_product)

class Super_product:
    def __init__(self, name: str, region: str, unit_price: float, unit_sold: int, expiry_date: str):
        self.name = name
        self.region = region
        self.unit_price = unit_price
        self.unit_sold = unit_sold
        self.expiry_date = expiry_date

    def __str__(self):
        return f"{self.name}, {self.region}, {self.unit_price}, {self.unit_sold}, {self.expiry_date}"
        
df = {}       
with open(data_path) as f:
    header = f.readline().strip()
    for head in header:
        head = Super_product("Milk","Kakheti", 3.5, 10, 2025-11-10)
        print(header)


    # chai araa chai
    # fu sheni chai tu ar svi axla dilaobit 
    # pederastivit didi ambavi ra 