from tkinter import *
from tkinter import messagebox

class Student:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
    
    def calcGrade(self):
        avg = (self.mark1 + self.mark2 + self.mark3) / 3
        return avg
    
    def display(self):
        avg = self.calcGrade()
        return f"Hello {self.name}! Your average grade is {avg}. Congratulations!"

class StudentGUI(Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Student Information")
        self.geometry("300x200")
        
        self.input_values()
    
    def input_values(self):
        name = input("Enter the student's name:")
        mark1 = int(input("Enter Mark 1: "))
        mark2 = int(input("Enter Mark 2: "))
        mark3 = int(input("Enter Mark 3: "))
        
        student = Student(name, mark1, mark2, mark3)
        
        result_label = messagebox.showinfo(self, message=student.display())
        result_label.pack(pady=10)
        
if __name__ == "__main__":
    app = StudentGUI()
    app.mainloop()