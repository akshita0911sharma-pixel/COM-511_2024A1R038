bill=int(input("Enter your bill amount: "))
if bill>=5000:
    discount=bill*0.2
    final_amount=bill-discount
    print("You are eligible for a 20% discount.")
    print("Your final bill amount after discount is:", final_amount)
    print("You saved:", discount)
elif bill>=3000:
    discount=bill*0.1
    final_amount=bill-discount
    print("You are eligible for a 10% discount.")
    print("Your final bill amount after discount is:", final_amount)
    print("You saved:", discount)
else:
    print("You are not eligible for any discount.")
    print("Your final bill amount is:", bill)    
