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
            
            grade = ""
            if average >= 75:
                grade = "A"
            elif average >= 60:
                grade = "B"
            elif average >= 40:
                grade = "C"
            else:
                grade = "Fail"

            print("\n" + "-" * 30)
            print(f"Name    : {name}")
            print(f"Average : {average:.1f}")
            print(f"Grade   : {grade}")
            print("-" * 30 + "\n")
                
        except ValueError:
            print("Invalid input. Please enter numerical values for marks.")

if __name__ == "__main__":
    main()
