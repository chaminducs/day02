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

    # 1. Asks for 3 initial expenses
    print("\nPlease enter your first 3 expenses:")
    for i in range(1, 4):
        while True:
            try:
                amount = float(input(f"Expense {i}: "))
                remaining_balance -= amount
                expenses.append(amount)
                
                # Immediate warning check
                if remaining_balance < 500:
                    print("Warning: Low Funds")
                
                print(f"Remaining Balance: {remaining_balance:.2f} LKR")
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

    # 2. Enter expenses multiple times until "done"
    print("\nEnter additional expenses (type 'done' to finish):")
    while True:
        entry = input("Enter expense (or 'done'): ").strip()
        
        if entry.lower() == 'done':
            break
            
        try:
            amount = float(entry)
            remaining_balance -= amount
            expenses.append(amount)
            
            # Immediate warning check
            if remaining_balance < 500:
                print("Warning: Low Funds")
                
            print(f"Remaining Balance: {remaining_balance:.2f} LKR")
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")

    # Final Display
    print("\n" + "="*30)
    print(f"Total Budget:      {total_budget:.2f} LKR")
    print(f"Total Expenses:    {sum(expenses):.2f} LKR")
    print(f"Remaining Balance: {remaining_balance:.2f} LKR")
    
    if remaining_balance < 500:
        print("Warning: Low Funds")
    print("="*30)

if __name__ == "__main__":
    main()
