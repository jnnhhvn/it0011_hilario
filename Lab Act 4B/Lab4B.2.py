file = open("Lab Act 4B\currency.csv", "r")
lines = file.readlines()
file.close()

lines.pop(0)
cur_rate = {}
index = 0
while index < len(lines):
    cur = lines[index].strip().split(",")
    cur_rate[cur[0]] = float(cur[2])
    index += 1

usd_amount = float(input("How much dollar do you have? "))
currency = input("What currency you want to have? ").upper()

if currency in cur_rate:
    converted = usd_amount * cur_rate[currency]
    print(f"\nDollar: {usd_amount:.2f} USD")
    print(f"{currency}: {converted:}")
else:
    print("Currency not found.")