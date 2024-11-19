
print("hello")
expenses = []

def menu():
    print("Welcome to the Expense Tracker!")
    while True:  # Keeps the program running in a loop
        print("\nPlease choose an option:")
        print("1. Add an expense")        
        print("2. View all expenses")      
        print("3. Calculate total expenses") 
        print("4. Exit")  
    
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_expense()   # Calls a function to add a new expense
        elif choice == "2":
            view_expenses()  # Calls a function to display all expenses
        elif choice == "3":
            calculate_total()  # Calls a function to calculate and show the total spent
        elif choice == "4":
            print("Exiting the Expense Tracker. Goodbye!")
            break  # Exit the loop, ending the program
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


def add_expense():
    """Allow the user to add an expense by asking for three details"""
    description = input("Enter a description for the expense: ")
    amount = float(input("Enter the amount spent: "))
    date = input("Enter the date(e.g., YYYY-MM-DD): ")
    
    #create a dictionary for the expense
    expense = {
        "description": description,
        "amount": amount,
        "date" : date
        }
    
    # add the expense to the list of expenses
    expenses.append(expense)
    print((f"Expense '{description}' of ${amount}' on '{date}' added."))


def view_expenses():
    print("\nYour expenses:")
    if not expenses:
        print("No expenses recorded yet.")
    else:
        for expense in expenses:
            #For each expense, retrieve detail and print them
            print(f"{expense['date']} - {expense['description']}: ${expense['amount']:.2f }")


def calculate_total():
    total = 0
    for expense in expenses:
        total += expense["amout"] #Adds the amount to the total
    print(f"\nTotal expenses: ${total:.2f}")
menu()