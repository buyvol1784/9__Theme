with open('результаты_контрольной.txt', 'r') as file:
    for line in file:
        student_data = line.split()

        if int(student_data[2]) < 3:
            print(f"{student_data[0]} {student_data[1]} получил(а) оценку {student_data[2]} идёт на пересдачу.")