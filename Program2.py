print("Fahrenheit Celsius Convator---")
value=float(input("Enter your value :"))
FC=input("Enter your C or F choise here:")
if FC=="C":
    F=value*(9/5)+32
    print("Temperature in Fahrenheit:",F,"F")
else:
    C=(value-32)*(5/9)
    print("Temperature in Celsius:",C,"C")