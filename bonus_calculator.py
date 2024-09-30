# Display the purpose of the program
print("Thank you for working at our company to make the world a better place!\n" +
     "To reward you, we want to give you an end-of-the-year bonus. Please " +
     "complete the survey to determine the amount of bonus you will receive.")

# Get weekly pay, bonus code, and years with company from user
weekly_pay = float(input("What is your weekly pay? (Do not use $). "))
bonus_code = input("What is your base bonus code? (It is either 1, 2, or 3). ")
years_experience = float(input("How many years have you worked with the company? "))

# TODO: Write your code here



  
# Display bonus information and bonus amount
print(f"The bonus for an employee with bonus code {bonus_code} and {years_experience} " +
     f"years of experience is ${bonus_pay:.2f}.")
