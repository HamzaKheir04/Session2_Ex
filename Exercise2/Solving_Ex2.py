"""
this function to calculate the Rate of Return
 the variable used :
    Vf : Future value which I'm gonna ask the user to enter it
    Vi : Initial value which is given in the Question = 63.48$
"""
def Rate_OF_Return(Vf,Vi):
    return ( ((float(Vf) - Vi) / Vi ) * 100 )

#to take the Expectation of the user

Future_Price = input("Enter the Expectation of the Future Stock Plz : ")

Current_Price = 63.48

#Variable To store the value of Rate_of_Return

R_R = Rate_OF_Return(Future_Price, Current_Price)

#Variable to store the value of


print(f"The Current Price of the Stock : {Current_Price}",
      f"The Expectation Of The User : {Future_Price}",
      f"The Rate Of Return : {R_R} %",
      #TRUE if the Rate_Of_Return  Positive, and FALSE if Negative
      f"The Boolean value : {R_R > 0}",
      sep="\n")
