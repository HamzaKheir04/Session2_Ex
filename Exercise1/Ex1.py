#Function to Calculate The  Total Profit
def Calculate_Profit(Rev,Exp):
    return int(Rev) - int(Exp)

#Declare variables And Ask the User To Enter The Revenue & Expenses

Revenue = input("Enter The Total Revenue plz :")
Expenses = input("Enter The Total Expenses plz :")

#Declare a variable and assign the value that return from the function after calling it
Profit=Calculate_Profit(Revenue,Expenses)

#Print the vairables in tidy manner
print(f"The Total Revenue : {Revenue} JOD", f"The Total Expenses :{Expenses} JOD","After Doing Some Calculations (TotalProfit = TotalRevenue - TotalExpenses)",
      f"The Total Profit :{Profit} JOD", sep="\n")
