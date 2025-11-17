student_ticket = str(input("Введите номер студенческого билета -> "))
a, b, c = ([int(student_ticket[0:4][0:2]), int(student_ticket[0:4][2:4])],
           [int(student_ticket[4:8][0:2]), int(student_ticket[4:8][2:4])],
           [int(student_ticket[0:4][0:2]), int(student_ticket[4:8][2:4])]
           )

print(f"А = {a}, B = {b}, C = {c}")

dx = round(b[1] - a[1], 3)
dy = round(a[0] - b[0], 3)
dc = round(-(dx * c[0] + dy * c[1]), 3)

print(f"{dx}x + {dy}y + {dc} = 0")
