print("TIP CALCULATOR\n\n")

total_bill = float(input("How much is the total bill ? \n"))
tip_percentage = int(input("How much tip would you like to give in percentage ? 10, 12 or 15 ?\n"))
num_of_persons = int(input("How many people to split the bill ? \n"))
res=round((total_bill * (1 + (tip_percentage/100)) / num_of_persons), 2)

print(".\n")
print(".\n")
print(".\n")
print(".\n")
print(".\n")
print(f"Each person should pay {res}")