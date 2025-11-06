from pathlib import Path
BASE_DIR = Path(__file__).parent.parent

print(BASE_DIR)
print(__file__)

data_path = BASE_DIR / "homework_9" / "products.txt"
print(data_path)

with open(data_path, "a") as f:
    # print(f.read())
    f.write("\nHeadphone")