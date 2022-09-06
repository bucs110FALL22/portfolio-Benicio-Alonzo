print(10*5)
print(10**2)
print(15/10)
print(15//10)
print(-15//10)
print(15%10)
print(10%15)
print(10%10)
print(0%10)
print(10/15) # it is a repeating decimal


rate = float(input( "What is the current exchange rate for the Euro to Dollar? "))


amount = float(input("What is the amount of currency that needs to be exchanged? "))

total= rate*amount

result = total-3 # the 3 is for a service fee

print("Your amount that has been exchanged is $",result)