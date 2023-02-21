import csv 

# Dimport csv

# Define an empty dictionary to store the user's expenses by category
expenses = {}

# Prompt the user to enter their monthly income
monthly_income = float(input("What is your monthly income? "))

# Load existing expenses from a file if available
try:
    with open('expenses.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            category, amount = row
            expenses[category] = float(amount)
    print("Existing expenses loaded.")
except FileNotFoundError:
    print("No existing expenses found.")

# Define a function to add a new expense to the expenses dictionary
def add_expense():
    while True:
        category = input("Enter a category for the expense (or 'done' to finish): ")
        if category == "done":
            break
        else:
            amount = float(input("Enter the monthly expense amount: "))
            if category in expenses:
                expenses[category] += amount
            else:
                expenses[category] = amount

# Define a function to edit an existing expense in the expenses dictionary
def edit_expense():
    category = input("Enter the category of the expense you want to edit: ")
    if category in expenses:
        new_amount = float(input("Enter the new monthly expense amount: "))
        expenses[category] = new_amount
    else:
        print("Expense not found.")

# Define a function to delete an existing expense from the expenses dictionary
def delete_expense():
    category = input("Enter the category of the expense you want to delete: ")
    if category in expenses:
        del expenses[category]
    else:
        print("Expense not found.")

# Define a function to edit an existing expense in the expenses dictionary   
def save_expenses():
    with open('expenses.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for category, amount in expenses.items():
            writer.writerow([category, amount])
    print("Expenses saved.")

# Allow the user to add, edit, or delete expenses
while True:
    action = input("Enter an action (add, edit, delete, summary, save, or quit): ")
    if action == "add":
        add_expense()
    elif action == "edit":
        edit_expense()
    elif action == "delete":
        delete_expense()
    elif action == "save":
        save_expenses()
    elif action == "quit":
        break
    elif action == "summary":
        # Calculate the user's total monthly expenses and savings
        total_expenses = sum(expenses.values())
        monthly_savings = monthly_income - total_expenses

        # Print a summary of the user's finances
        print("\nMonthly Income: ${:.2f}".format(monthly_income))
        print("Monthly Expenses:")
        for category, amount in expenses.items():
            print("- {}: ${:.2f}".format(category, amount))
        print("Total Expenses: ${:.2f}".format(total_expenses))
        print("Monthly Savings: ${:.2f}".format(monthly_savings))
 
