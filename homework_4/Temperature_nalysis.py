
import datetime

temperatures = [2, 4, 8, 5, 14, 19, 12]

start_date = datetime.date(2025, 10, 6)

sum = 0

for i, temp in enumerate(temperatures):
    print(f"{start_date.strftime('%d/%m/%Y/ (%A)')}: {temp} °C")
    start_date += datetime.timedelta(days=1)
    sum += temp

print(f"Average temerature: {round(sum / len(temperatures))}")

start_date2 = datetime.date(2025, 10, 6)

coldest_index = temperatures.index(min(temperatures))
hottest_index = temperatures.index(max(temperatures))

coldest_day = start_date2 + datetime.timedelta(days=coldest_index)
hottest_day =  start_date2 + datetime.timedelta(days=hottest_index)

print(f"Coldest day was {min(temperatures)} °C on {coldest_day.strftime('%d/%m/%Y/ (%A)')}")
print(f"Hottest day was {max(temperatures)} °C on {hottest_day.strftime('%d/%m/%Y/ (%A)')}")

