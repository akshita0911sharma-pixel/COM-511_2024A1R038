pin=input("Enter your pin: ")
if len(pin) >= 4 and pin=='9870':
    print("Lock open")
elif len(pin)<=4:
    print("***ERROR***")
else:
    print("Try again")      
