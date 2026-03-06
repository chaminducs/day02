def main():
    name = input("Enter student's name: ")
    
    try:
        mark1 = float(input("Enter marks for subject 1: "))
        mark2 = float(input("Enter marks for subject 2: "))
        mark3 = float(input("Enter marks for subject 3: "))
        
        average = (mark1 + mark2 + mark3) / 3
        
        print(f"\nStudent Name: {name}")
        print(f"Average Marks: {average:.2f}")
        
        if average >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")
            
    except ValueError:
        print("Invalid input. Please enter numerical values for marks.")

if __name__ == "__main__":
    main()
