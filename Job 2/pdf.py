import csv
from fpdf import FPDF

class StudentInventory:
    def __init__(self):
        self.students = []

    def add_student(self, student_id, name, age, clas):
        self.students.append({
            'ID': student_id,
            'Name': name,
            'Age': age,
            'Class': clas
        })

    def generate_pdf_report(self, output_pdf):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Add table header
        pdf.cell(40, 10, 'ID', 1)
        pdf.cell(60, 10, 'Name', 1)
        pdf.cell(40, 10, 'Age', 1)
        pdf.cell(40, 10, 'Class', 1)
        pdf.ln()

        # Add student data
        for student in self.students:
            pdf.cell(40, 10, student['ID'], 1)
            pdf.cell(60, 10, student['Name'], 1)
            pdf.cell(40, 10, student['Age'], 1)
            pdf.cell(40, 10, student['Class'], 1)
            pdf.ln()

        pdf.output(output_pdf)
        print("PDF report generated successfully.")

        # Print student information
        self.print_students()

    def print_students(self):
        print("Student Information:")
        print("ID\tName\tAge\tClass")
        for student in self.students:
            print(f"{student['ID']}\t{student['Name']}\t{student['Age']}\t{student['Class']}")

# Example Usage
if __name__ == "__main__":
    student_inventory = StudentInventory()

    num_students = int(input("How many students to add? "))
    for i in range(num_students):
        print(f"Enter Student ({i + 1}) Information:")
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        age = input("Enter Student Age: ")
        clas= input("Enter Student Class: ")
        student_inventory.add_student(student_id, name, age, clas)

    # Generate PDF report
    student_inventory.generate_pdf_report("students_report.pdf")
