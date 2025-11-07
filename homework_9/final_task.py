import datetime
from pathlib import Path
BASE_DIR = Path(__file__).parent.parent

data_path = BASE_DIR / "homework_9" / "sales.csv"

df = {}
with open(data_path,) as f:
    headers = f.readline().strip().split(",")
    for header in headers:
        df[header] = []

    for line in f.readlines():
        for i, cell in enumerate(line.strip().split(",")):
            header = headers[i]
            # print(i, cell)

            if header == "date":
                cell = datetime.datetime.strptime(cell, "%Y-%m-%d").date()
            elif header == "units_sold": 
                cell = int(cell)
            elif header == "unit_price":
                cell = float(cell)
            elif header == "region":
                for head in headers:
                    head = "North"
                    # cell = head            aqedan unda gavagrdzelo 4.filter and print
                
            df[header].append(cell)

print(f"Total units sold: {sum(df["units_sold"])}")
print(f"Average unit price: {sum(df["unit_price"]) / len(df)}")
print(f"Most popular product: {max(df["product"])}")
print(f"Total revenure per region: {sum(df["units_sold"]) + sum(df["unit_price"]) / len(df)}")
print(f"In North keyboard units sold were {df["region"]}")