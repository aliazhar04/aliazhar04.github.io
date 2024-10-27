import tkinter as tk
from tkinter import ttk

# Grade points for each grade
GRADE_POINTS = {
    "S": 10, "A": 9, "B": 8, "C": 7, "D": 6, "E": 5, "F": 0
}

# Predefined subjects and credits for each semester
SEMESTERS = {
    1: [("Communication skills in English", 4), ("Mathematics I", 5), ("Applied Physics I", 3),
        ("Applied Chemistry", 3), ("Engineering Graphics", 1.5), ("Applied Chemistry lab", 1),
        ("Introduction to IT systems lab", 2), ("Sports and Yoga", 1)],
    2: [("Environmental Science", 0), ("Mathematics II", 4), ("Applied Physics II", 3),
        ("Applied Physics Lab", 1), ("Communication skills in English lab", 1.5),
        ("Engineering workshop practice", 1.5), ("Fundamentals of electrical and electronics", 3),
        ("Fundamentals of electrical and electronics lab", 0), ("Basic electronics", 3),
        ("Electronics tinkering workshop", 0)],
    3: [("Internship 1", 2), ("Electric circuits and networks", 3), ("Principles of electronic communication", 3),
        ("Electronic circuits", 4), ("Digital electronics", 4), ("Fundamental of C programming", 0),
        ("Principles of electronic communication lab", 1.5), ("Electronic circuits lab", 1.5),
        ("Digital electronics lab", 1.5), ("Fundamental of C programming lab", 1.5)],
    4: [("Community skills in Indian knowledge system", 0), ("Minor project", 2),
        ("Microcontroller and applications", 4), ("Electronic measurements and instrumentation", 4),
        ("Linear integrated circuits", 4), ("Microcontroller and applications lab", 1.5),
        ("Linear integrated circuits lab", 1.5), ("PCB prototyping workshop", 1.5),
        ("Python programming lab", 0)],
    5: [("Industrial Management and Safety", 0), ("Digital Communication", 4), ("Signals and Systems", 4),
        ("Industrial Automation", 4), ("Digital Communication Lab", 1.5), ("Verilog HDL and PLD Lab", 1.5),
        ("Industrial Automation Lab", 1.5), ("Seminar", 1)],
    6: [("Entrepreneurship and Startup", 4), ("Embedded Systems", 4), ("Concepts of IoT", 4),
        ("Indian Constitution", 0), ("Simulation Lab with Numerical Software", 1.5),
        ("Computer Hardware and Data Communication Lab", 2.5), ("Embedded Systems Lab", 1.5),
        ("Major Project", 4)]
}

# Function to calculate GPA and percentage
def calculate_gpa_and_percentage():
    total_credits = 0
    total_points = 0
    for subject, credit in SEMESTERS[selected_semester.get()]:
        grade = grade_vars[subject].get()
        if grade in GRADE_POINTS:
            total_credits += credit
            total_points += GRADE_POINTS[grade] * credit

    if total_credits == 0:
        gpa.set("N/A")
        percentage.set("N/A")
    else:
        gpa_value = total_points / total_credits
        gpa.set(f"{gpa_value:.2f}")
        percentage.set(f"{gpa_value * 9.5:.2f}%")

# GUI setup
root = tk.Tk()
root.title("GPA and Percentage Calculator")

# Semester selection
selected_semester = tk.IntVar(value=1)
tk.Label(root, text="Select Semester").grid(row=0, column=0, padx=10, pady=10)
semester_menu = ttk.Combobox(root, textvariable=selected_semester, values=list(SEMESTERS.keys()))
semester_menu.grid(row=0, column=1, padx=10, pady=10)

# Subject grade selection
grade_vars = {}
subject_labels = []

def update_subjects(*args):
    for label in subject_labels:
        label.destroy()

    row = 1
    for subject, credit in SEMESTERS[selected_semester.get()]:
        tk.Label(root, text=f"{subject} ({credit} credits)").grid(row=row, column=0, sticky="w", padx=10)
        grade_var = tk.StringVar(value="S")
        grade_menu = ttk.Combobox(root, textvariable=grade_var, values=list(GRADE_POINTS.keys()))
        grade_menu.grid(row=row, column=1, padx=10, pady=5)
        grade_vars[subject] = grade_var
        subject_labels.append(grade_menu)
        subject_labels.append(tk.Label(root, text=f"{subject} ({credit} credits)"))
        row += 1

    # Update row for GPA and Percentage
    global results_row
    results_row = row

selected_semester.trace("w", update_subjects)
update_subjects()

# Result labels
gpa = tk.StringVar()
percentage = tk.StringVar()

tk.Label(root, text="GPA:").grid(row=results_row, column=0, padx=10, pady=10, sticky="e")
tk.Label(root, textvariable=gpa).grid(row=results_row, column=1, padx=10, pady=10, sticky="w")

tk.Label(root, text="Percentage:").grid(row=results_row + 1, column=0, padx=10, pady=10, sticky="e")
tk.Label(root, textvariable=percentage).grid(row=results_row + 1, column=1, padx=10, pady=10, sticky="w")

# Calculate Button
calculate_button = tk.Button(root, text="Calculate", command=calculate_gpa_and_percentage)
calculate_button.grid(row=results_row + 2, column=0, columnspan=2, pady=20)

# Start the application
root.mainloop()
