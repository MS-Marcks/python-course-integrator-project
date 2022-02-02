student = []
while True:
    print("=================== MENU ==================")
    print("1 - Ver la lista de alumno")
    print("2 - Añadir un estudiante al listado")
    print("3 - salir")
    option = input("ingrese la opcion: ")
    if option == "1":
        for studen in student:
            print(f"\tNombre del estudiante: {studen[0]}, cantidad de cursos: {studen[1]}")
    elif option == "2":
            name = ""
            course = ""
            cancel = False

            while True:
                name = input("Ingrese el nombre del estudiante (para cancelar la insercion presione:-1): ")
                if name == "-1":
                    cancel = True
                    break
                elif(name != ""):
                    break
                print("\n\t Error: no puede dejar el nombre vacio\n")

            while True and not cancel:
                try:
                    course = int(input("Ingrese la cantidad de cursos (para cancelar la insercion presione:-1): "))
                    if course == -1:
                        cancel = True
                        break
                    elif course > 0:
                        break
                    print("\n\t Error: los cursos deben de ser numero enteros positivos\n")
                except:
                    print("\n\tError: los cursos deben de ser un numero entero\n")

            if not  cancel:
                student.append([name,course])

    elif option == "3":
        break
    else:
        print("\n\tERROR: OPCION NO ENCONTRADA\n")
