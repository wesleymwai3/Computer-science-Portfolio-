
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


def main():
    try:
        mark = float(input("Enter student mark (0-100): "))

        if not 0 <= mark <= 100:
            print("Please enter a mark between 0 and 100.")
        else:
            grade = calculate_grade(mark)
            print("Your grade is:", grade)

    except ValueError:
        print("Error: Please enter a valid number.")


if __name__ == "__main__":
    main()
