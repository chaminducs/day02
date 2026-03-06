def main():
    while True:
        name = input("Enter student's name (or type 'Exit' to quit): ")
        
        if name.lower() == 'exit':
            break
            
        try:
            mark1 = float(input("Enter marks for subject 1: "))
            mark2 = float(input("Enter marks for subject 2: "))
            mark3 = float(input("Enter marks for subject 3: "))
            
            average = (mark1 + mark2 + mark3) / 3
            
            print(f"\nStudent Name: {name}")
            print(f"Average Marks: {average:.2f}")
            
            if average >= 75:
                print("Result: Grade A")
            elif average >= 60:
                print("Result: Grade B")
            elif average >= 40:
                print("Result: Grade C")
            else:
                print("Result: Fail")
            print("-" * 20)
                
        except ValueError:
            print("Invalid input. Please enter numerical values for marks.")

if __name__ == "__main__":
    main()
