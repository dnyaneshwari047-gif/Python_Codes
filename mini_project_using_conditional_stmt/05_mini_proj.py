
# Mini Project 5: Employee Performance Bonus

# Input details
name = input("Enter employee name: ")
salary = float(input("Enter monthly salary: ₹"))
experience = int(input("Enter years of experience: "))
rating = int(input("Enter performance rating (1-5): "))

print("\n----- Employee Bonus Details -----")
print("Employee Name:", name)

# Validate performance rating
if rating < 1 or rating > 5:
    print("Invalid Rating! Please enter a rating between 1 and 5.")

else:
    # Calculate bonus percentage
    if experience >= 10 and rating >= 4:
        bonus_percentage = 20

    elif experience >= 5 and rating >= 4:
        bonus_percentage = 15

    elif experience >= 2 and rating >= 3:
        bonus_percentage = 10

    else:
        bonus_percentage = 0

    # Calculate bonus and final salary
    bonus_amount = salary * bonus_percentage / 100
    final_salary = salary + bonus_amount

    print("Bonus Percentage:", bonus_percentage, "%")
    print("Bonus Amount: ₹", bonus_amount)
    print("Final Salary: ₹", final_salary)

    # Display performance message
    if rating == 5:
        print("Performance Message: Excellent Performer")
    elif rating < 3:
        print("Performance Message: No Bonus")
    else:
        print("Performance Message: Good Performer")
