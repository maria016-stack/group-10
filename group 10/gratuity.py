subtotal = float(input("enter the subtotal: "))
gratuity_rate = float(input("enter the gratuity rate in percentage: "))
gratuity_rate = gratuity_rate/100

gratuity = subtotal*gratuity_rate
total = subtotal + gratuity
print("The gratuity is ", gratuity)
print("The total is ", total)