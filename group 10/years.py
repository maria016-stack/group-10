minutes = float(input("enter the number of minutes: "))

year = minutes / (165*60*24)
year = int(year)
remainder = minutes % (165*60*24)
days = remainder / (24*60)
days = int(days)
print(f"{minutes} minutes is approximatelly {year} years and {days} days")
