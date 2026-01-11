# Student Grade Calculator
# Week 2 Project

def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent work! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good effort! You can do even better 😊"
    elif marks >= 60:
        return "D", "You passed. Keep practicing 💪"
    else:
        return "F", "Don't give up! Try again 🔄"


print("🎓 Student Grade Calculator 🎓\n")

name = input("Enter student name: ")

while True:
    try:
        marks = int(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            break
        else:
            print("⚠️ Marks must be between 0 and 100. Try again.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

grade, message = calculate_grade(marks)

print("\n📊 RESULT FOR", name.upper())
print(f"Marks: {marks}/100")
print(f"Grade: {grade}")
print(f"Message: {message}")
