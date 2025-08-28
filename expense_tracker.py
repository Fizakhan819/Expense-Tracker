from expense import Expense
import calendar
import datetime

def main():
    print(f" 💸 Expense Tracker")
    expense_file_path = "expenses.csv"
    budget = 2000

    # get user input for expense
    expense = get_user_expense()

    # write their expense to a file
    save_expense_to_file(expense, expense_file_path)

    #read file and summarise expenses
    summarise_expenses(expense_file_path,budget)
    pass

def get_user_expense():
    print(f"Getting user expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    expense_categories =[
        '🍕Food',
        '🏠Home' ,
        '💻Work' ,
        '🍿Fun' ,
        '🏝️Extra'
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f" {i + 1}. {category_name}")  #to start at 1

        value_range = f"[1-{len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}:")) -1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        else:
            print("Invalid Category. Please try again")


def save_expense_to_file(expense: Expense, expenses_file_path):  #:Expense for typehint
    print(f"Saving user expense: {expense} to {expenses_file_path}")
    with open(expenses_file_path, "a", encoding="utf-8") as f:
        f.write(f"{expense.name}, {expense.amount}, {expense.category}\n")



def summarise_expenses(expenses_file_path, budget):
    print(f"Summarising user expense 📌")
    expenses = []
    with open(expenses_file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            line_expense = Expense(
                name=expense_name,
                amount=float(expense_amount),
                category=expense_category
            )
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount  

    print("Expenses by Category 🏷️:")
    for key, amount in amount_by_category.items():
        print(f"  {key}: €{amount:.2f}")

    total_spent = sum([x.amount for x in expenses])
    print(f"💰Total Spent: €{total_spent:.2f} ")

    remaining_budget = budget - total_spent
    print(f"✅Budget remaining: €{remaining_budget:.2f}")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day
    daily_budget = remaining_budget / remaining_days
    print(f"\033[92m📅Budget per Day: €{daily_budget:.2f}\033[0m")




if __name__ == "__main__":

    main()
