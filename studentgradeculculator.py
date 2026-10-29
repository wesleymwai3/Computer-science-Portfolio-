#TODO: Write your program
def calculate_grade(mark):
    if mark < 0 or mark > 100:
        return "Invalid mark"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "E"

mark = float(input("Enter student mark (0-100): "))

if 0 <= mark <= 100:
    print("Your grade is:", calculate_grade(mark))
else:
    print("Please enter a mark between 0 and 100.")
    