employee_name = input("Enter the employee's name? ")
hourly_wage = input(f"What is {employee_name.strip().title()}'s hourly rate? ")
hours_worked = input(f"How many hours did {employee_name.strip().title()} work this week? ")
total_earned = float(hourly_wage) * float(hours_worked)

print(f"{employee_name.strip().title()} earned ${str(total_earned)} this week")
