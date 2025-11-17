student_ticket = str(input("Введите номер студенческого билета -> "))
a, b, c = ([int(student_ticket[0:4][0:2]), int(student_ticket[0:4][2:4])],
           [int(student_ticket[4:8][0:2]), int(student_ticket[4:8][2:4])],
           [int(student_ticket[0:4][0:2]), int(student_ticket[4:8][2:4])]
           )

print(f"А = {a}, B = {b}, C = {c}")

dx = b[0] - a[0]
dy = b[1] - a[1]

if dx == 0:
    print(f"x = {c[0]}")

k = round(dy / dx, 3)
y = round(c[1] - k * c[0], 3)

print(f"y = {k}x + {y}")

