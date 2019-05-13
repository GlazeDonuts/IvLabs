hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate : "))
if (hrs<=40):
    pay=hrs*rate
else:
    pay = 40*rate + (hrs-40)*1.5*rate
print(pay)
