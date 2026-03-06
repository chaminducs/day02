def main():
    print("--- Monthly Budget Program ---")
    
    # Get total monthly budget
    while True:
        try:
            budget_input = input("Enter your total monthly budget: ")
            total_budget = float(budget_input)
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for the budget.")

    remaining_balance = total_budget
    expenses = []

    # Get expenses multiple times
    print("\nEnter your expenses (type 'done' to finish):")
    while True:
        entry = input("Enter expense (or 'done' to finish): ").strip()
        
        if entry.lower() == 'done':
            break
            
        try:
            amount = float(entry)
            remaining_balance -= amount
            expenses.append(amount)
            print(f"Current Balance: {remaining_balance:.2f} LKR")
        except ValueError:
            print("Invalid input. Please enter a numeric amount or 'done'.")

    # Final Display
    print("\n" + "="*30)
    print(f"Total Budget:     {total_budget:.2f} LKR")
    print(f"Total Expenses:   {sum(expenses):.2f} LKR")
    print(f"Remaining Balance: {remaining_balance:.2f} LKR")
    
    # Low funds warning
    if remaining_balance < 500:
        print("Warning: Low Funds")
    print("="*30)

if __name__ == "__main__":
    main()
