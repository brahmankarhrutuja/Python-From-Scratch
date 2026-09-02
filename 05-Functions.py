# Electricity Bill Calculator

def calculate_bill(units):
   if units <= 100:
       return units * 5
   elif units <= 200:
       return units * 7
   else:
       return units * 10

# Input
#units = int(input("Enter electricity units: "))

# Function call
print(calculate_bill(100))

# Output
#print("Total Bill Amount:", bill)