"""
Ask The User To Enter their Name, Age and City Name
and make Sure that The Name and The City Name are Capitalized (The First letter in UpperCase)
Which i can use The Built-in Function capitalize() to do it

"""
Name=input("Enter your Name Plz :").capitalize()
Age=input("Enter your Age Plz :")
City_Name=input("Enter your City Name Plz :").capitalize()

#Using a Single Print to print the Name, Age and the City Name

print(f"\nHello {Name},",
      f"Happy birthday! You're {Age} years old now :)",
      f"Do you need to find a nice restaurant in {City_Name} to celebrate?",sep="\n")
