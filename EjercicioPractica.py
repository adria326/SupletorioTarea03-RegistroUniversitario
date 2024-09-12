def menu_principal():
    print("\n--- Sistema de Matriculación Universitaria ---")
    print("1. Registrar Estudiante")
    print("2. Ver Cursos Disponibles")
    print("3. Matricularse en un Curso")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion
estudiantes = []  # Lista vacía para almacenar estudiantes
cursos = ["Matemáticas", "Desarrollo", "Informatica", "Programación", "fundamentos de Hardware y Software"]  # Lista de cursos predefinidos
matriculas = {}  # Diccionario para almacenar las matrículas de estudiantes en cursos

def registrar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ").strip()
    if nombre:
        estudiantes.append(nombre)
        print(f"Estudiante '{nombre}' registrado con éxito.")
    else:
        print("El nombre no puede estar vacío.")

def ver_cursos():
    if cursos:
        print("\n--- Cursos Disponibles ---")
        for i, curso in enumerate(cursos, 1):
            print(f"{i}. {curso}")
    else:
        print("No hay cursos disponibles.")

def matricular_curso():
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    ver_cursos()
    try:
        num_curso = int(input("Seleccione el número del curso: ")) - 1
        if num_curso < 0 or num_curso >= len(cursos):
            print("Selección de curso no válida.")
            return
    except ValueError:
        print("Entrada no válida.")
        return

    nombre_estudiante = input("Ingrese el nombre del estudiante: ").strip()
    if nombre_estudiante not in estudiantes:
        print("El estudiante no está registrado.")
        return

    curso = cursos[num_curso]
    if nombre_estudiante not in matriculas:
        matriculas[nombre_estudiante] = []
    matriculas[nombre_estudiante].append(curso)
    print(f"Estudiante '{nombre_estudiante}' matriculado en el curso '{curso}'.")
    
def main():
    while True:
        opcion = menu_principal()
        if opcion == '1':
            registrar_estudiante()
        elif opcion == '2':
            ver_cursos()
        elif opcion == '3':
            matricular_curso()
        elif opcion == '4':
            print("Gracias por usar el sistema de matriculación.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()