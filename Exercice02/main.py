students = {
    'Alice': {
         'Mathematiques': 90,
         'Francais': 80,
         'Histoire': 95
    },
    'Bob': {
         'Mathematiques': 75,
         'Francais': 85,
         'Histoire': 70
    },
    'Charlie': {
         'Mathematiques': 88,
         'Francais': 92,
         'Histoire': 78
     }
}

student_name = input("Nom de l'étudiant: ")

if student_name in students:
    student_marks = students[student_name]
    print(f"Notes de {student_name} :")

    for subject, mark in student_marks.items():
        print(f"{subject}: {mark}")
else:
    print(f"L'étudiant {student_name} n'existe pas dans la liste.")
