def collect_student_data():
    students = {}
    while True:
        name = input("Enter the student name: ")
        if name.lower() == "exit":
            break
        if name in students:
            print("Student already exist.")
            continue
        try:
            marks = float(input(f"Enter the marks for {name}: "))
            students[name] = marks
        except ValueError:
            print("Invalid input. Please enter a valid number for marks.")
    return students

def display_report(students):
    if not students:
        print("No student data available.")
        return 
    marks = list(students.values())
    min_marks = min(marks)
    max_marks = max(marks)
    average_marks = sum(marks) / len(marks)

    topper = [name for name, score in students.items() if score == max_marks]
    bottom = [name for name, score in students.items() if score == min_marks]

    print('-'*40)
    print("Student Marks Report:")
    print(f"Average marks: {average_marks:.2f}")
    print(f"Highest Marks is {max_marks} by {', '.join(topper)}")
    print(f"Lowest Marks is {min_marks} by {', '.join(bottom)}")
    print('-'*40)

def main():
    students = collect_student_data()
    display_report(students)

if __name__ == "__main__":
    main()