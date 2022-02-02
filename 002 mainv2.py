students = []

def print_list_student(students):
    for student in students:
        name = student["name"]
        course = student["course"]
        print(f"\n\tNombre del estudiante: {name}, cantidad de cursos:{course}")

def add_student():
    name=""
    course=""
    cancel=False

    while name=="":
        name = input("Ingrese el nombre del estudiante (para cancelar la insercion presione:-1): ")
        if name=="-1":
            cancel=True
            break
        if name == "":
            print("\n\tError: no puede dejar el nombre vacio\n")

    while course=="" and not cancel:
        course=input("Ingrese la cantidad de cursos (para cancelar la insercion presione: 0 ): ")
        if not course.isdecimal(): 
            print("\n\tError: el valor ingresado debe de ser un numero\n")   
            course = ""   
            continue
        elif course=="0":
            cancel=True
            break
        course = int(course)

    if not cancel:
        return {"name":name,"course":course}

def search_course(students):
    nameStudent = ""
    while nameStudent=="":
        nameStudent = input("Ingrese el nombre del estudiante (para cancelar la insercion presione:-1): ")
        if nameStudent == "":
            print("\n\tError: no puede dejar el nombre vacio\n")
    
    if nameStudent == "-1":
        return

    for student in students:
        name = student["name"]
        if name == nameStudent:
            course = student["course"]
            print(f"\n\tEl estudiante: {name}, tiene la  cantidad de cursos:{course}\n")
            return 

while True:
    print("=================== MENU ==================")
    print("1 - Ver la lista de alumno")
    print("2 - Añadir un estudiante al listado")
    print("3 - Ver cantidad de cursos de un estudiante")
    print("4 - salir")
    option = input("ingrese la opcion: ")
    if option == "1":
        print_list_student(students)
    elif option == "2":
        students.append(add_student())
    elif option == "3":
        search_course(students)
    elif option == "4":
        break
    else:
        print("\n\tERROR: OPCION NO ENCONTRADA\n")
