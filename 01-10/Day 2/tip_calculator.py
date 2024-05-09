print("welcome toa doller tip calculator\n")
total = float(input("What was the total bill?\n$"))
percentage = int(input("What percentage would you like to give?\n"))
splitNum = int(input("How many people are we splitting with?\n"))
tipAmount = float(total * (percentage/100)) 
plusTip = float(total + tipAmount)
perPerson = "{:.2f}".format(plusTip/splitNum)


print(f"Each person should pay: ${perPerson}")