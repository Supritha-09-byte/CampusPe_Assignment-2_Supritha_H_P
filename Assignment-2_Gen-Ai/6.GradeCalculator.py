"""
Question 6: Grade Calculator
Description: Calculates total, percentage, grade and pass/fail result.
"""

def grade_calculator():
    print("===== GRADE CALCULATOR =====\n")

    try:
        marks = []

        # Taking marks for 5 subjects
        for i in range(1, 6):
            subject_mark = float(input(f"Enter marks for Subject {i} (0-100): "))

            if subject_mark < 0 or subject_mark > 100:
                raise ValueError("Marks must be between 0 and 100.")

            marks.append(subject_mark)

        # Calculations
        total_marks = sum(marks)
        percentage = total_marks / 5

        # Grade calculation
        if percentage >= 90:
            grade = "A+ (Outstanding)"
        elif percentage >= 80:
            grade = "A (Excellent)"
        elif percentage >= 70:
            grade = "B (Good)"
        elif percentage >= 60:
            grade = "C (Average)"
        elif percentage >= 50:
            grade = "D (Pass)"
        else:
            grade = "F (Fail)"

        # Pass/Fail condition (all subjects >= 40)
        if all(mark >= 40 for mark in marks):
            result = "Pass"
        else:
            result = "Fail"

        # Display results
        print("\n===== RESULT =====")
        for i in range(5):
            print(f"Subject {i+1}: {marks[i]}")

        print(f"\nTotal Marks: {total_marks} / 500")
        print(f"Percentage: {percentage:.2f}%")
        print(f"Grade: {grade}")
        print(f"Result: {result}")

    except ValueError as error:
        print("\n Error:", error)
    except Exception:
        print("\n Invalid input! Please enter valid numbers.")


# Main execution
if __name__ == "__main__":
    grade_calculator()