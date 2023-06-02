#
#
#
#                                THIS IS A TIP CALCULATOR 
#
#          
#
print("Welcome to the Tip Calculator")                                   # Print statement for initial greeting to the user

# Taking input from the user
bill = float(input("What is the total bill? $"))                         # Taking the total bill amount as input from the user
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))  # Taking the desired tip percentage as input
people = int(input("How many people to split the bill?"))                # Taking the number of people to split the bill among

tip_as_percent = tip / 100                                               # Converting the tip percentage to decimal form
total_tip_amount = bill * tip_as_percent                                 # Calculating the total tip amount
total_bill = bill + total_tip_amount                                     # Calculating the total bill amount (bill + tip)
bill_per_person = total_bill / people                                    # Calculating the amount each person should pay
final_amount = "{:.2f}".format(bill_per_person)                          # Formatting the bill per person to two decimal places

print(f"Each person should pay: ${final_amount}")                        # Printing the amount each person should pay
#
#
#
#                               
#
#          
#