month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

date_input = input("Enter the date (mm/dd/yyyy): ")
month, day, year = map(int, date_input.split('/'))

print(f"Date Output: {month_names[month - 1]} {day}, {year}")

