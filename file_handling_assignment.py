def print_welcome_message():
    print("Welcome to the Personal Finance Tracker!")
    print("You can manage your income, expenses, and savings.")
    print("Select an option from the menu below:")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Generate Report")
    print("4. Exit")

print_welcome_message()

income = 0.0
expenses = 0.0
savings = 0.0
transactions = []  # List to store transactions
def get_input(prompt):
    return input(prompt)

def add_income(amount):
    global income
    income += amount
    transactions.append({'type': 'Income', 'amount': amount})

def add_expense(amount):
    global expenses
    expenses += amount
    transactions.append({'type': 'Expense', 'amount': amount})

def calculate_savings():
    global savings
    savings = income - expenses
def menu():
    while True:
        print_welcome_message()
        choice = int(get_input("Enter your choice: "))
        if choice == 1:
            amount = float(get_input("Enter income amount: "))
            add_income(amount)
        elif choice == 2:
            amount = float(get_input("Enter expense amount: "))
            add_expense(amount)
        elif choice == 3:
            calculate_savings()
            print(f"Total Income: ${income:.2f}")
            print(f"Total Expenses: ${expenses:.2f}")
            print(f"Total Savings: ${savings:.2f}")
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

menu()
import json

def save_transactions():
    with open('transactions.json', 'w') as file:
        json.dump(transactions, file)

def load_transactions():
    global transactions
    try:
        with open('transactions.json', 'r') as file:
            transactions = json.load(file)
    except FileNotFoundError:
        transactions = []
def generate_report():
    categories = {}
    for transaction in transactions:
        category = transaction['type']
        if category not in categories:
            categories[category] = 0
        categories[category] += transaction['amount']
    
    for category, total in categories.items():
        print(f"Total {category}: ${total:.2f}")
import matplotlib.pyplot as plt

def plot_report():
    categories = {'Income': 0, 'Expense': 0}
    for transaction in transactions:
        category = transaction['type']
        categories[category] += transaction['amount']

    labels = categories.keys()
    sizes = categories.values()
    
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Income vs Expense')
    plt.show()
def get_valid_float(prompt):
    while True:
        try:
            return float(get_input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def menu():
    load_transactions()
    while True:
        print_welcome_message()
        choice = int(get_input("Enter your choice: "))
        if choice == 1:
            amount = get_valid_float("Enter income amount: ")
            add_income(amount)
        elif choice == 2:
            amount = get_valid_float("Enter expense amount: ")
            add_expense(amount)
        elif choice == 3:
            calculate_savings()
            print(f"Total Income: ${income:.2f}")
            print(f"Total Expenses: ${expenses:.2f}")
            print(f"Total Savings: ${savings:.2f}")
            generate_report()
        elif choice == 4:
            save_transactions()
            break
        else:
            print("Invalid choice. Please try again.")
def print_closing_message():
    print("Thank you for using the Personal Finance Tracker!")
    print("Goodbye!")

print_closing_message()
