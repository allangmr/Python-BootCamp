#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
number_of_people = input("How many people to split the bill? ")
subtotal_with_tip = float(bill) * (int(tip) / 100) + float(bill)
bill_per_person = subtotal_with_tip  / int(number_of_people)
# other way to put 2 decimals is final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${bill_per_person:.2f}")