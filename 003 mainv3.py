import tkinter as tk
from tkinter import messagebox

students = []

def clear_form():
    txt_input_name.delete(first=0,last="end")
    txt_input_course.delete(first=0,last="end")

def isNumber(number):
    try:
        return int(number)
    except:
        return ""


def print_list_student():
    for student in students:
        name = student["name"]
        course = student["course"]
        print(
            f"\n\tNombre del estudiante: {name}, cantidad de cursos:{course}")


def add_student():
    name = txt_input_name.get()
    course = txt_input_course.get()

    if name == "" or course == "":
        messagebox.showinfo(
            message="no puede dejar los campos vacios", title="Error")
        return

    course = isNumber(course)
    if course == "":
        messagebox.showinfo(
            message="el valor de los cursos debe de ser un numero", title="Error")
        return

    if course < 1:
        messagebox.showinfo(
            message="el valor de los cursos debe de un entero positivo", title="Error")
        return

    students.append({"name": name, "course": course})
    clear_form()
    messagebox.showinfo(
        message="se agrego exitosamente el estudiante", title="Info")


def search_course():
    nameStudent = txt_input_name.get()
    if nameStudent == "":
        messagebox.showinfo(
            message="no puede dejar el nombre vacio", title="Error")
        return

    exist = False
    for student in students:
        name = student["name"]
        if name == nameStudent:
            course = student["course"]
            print(
                f"\n\tEl estudiante: {name}, tiene la cantidad de cursos:{course}\n")
            exist = True
            break

    if not exist:
        messagebox.showinfo(
            message="No existe ningun estudiante con ese nombre", title="Error")
    clear_form()


mw = tk.Tk()

mw.title("Sistema de ingreso de cursos")
mw.config(width=450, height=150)

btn_show_list_student = tk.Button(
    text="Listar a los estudiantes", command=print_list_student)
btn_show_list_student.place(x=5, y=5)

# name
label_input_name = tk.Label(text="Ingrese el nombre del estudiante: ")
label_input_name.place(x=20, y=40)
txt_input_name = tk.Entry()
txt_input_name.place(x=250, y=40)

# course
label_input_course = tk.Label(text="Ingrese la cantidad de cursos: ")
label_input_course.place(x=20, y=65)
txt_input_course = tk.Entry()
txt_input_course.place(x=250, y=65)

btn_show_add_student = tk.Button(
    text="Agregar Estudiante", command=add_student)
btn_show_add_student.place(x=20, y=90)

btn_search_student_course = tk.Button(
    text="Buscar Estudainte", command=search_course)
btn_search_student_course.place(x=200, y=90)
mw.mainloop()
