from numpy import ones,vstack
from numpy.linalg import lstsq

student_ticket = str(input("Введите номер студенческого билета -> "))
a, b = ([int(student_ticket[0:4][0:2]), int(student_ticket[0:4][2:4])],
        [int(student_ticket[4:8][0:2]), int(student_ticket[4:8][2:4])])

x_coords, y_coords = zip(a, b)
print(f"А = {a}, B = {b}")

A = vstack([x_coords,ones(len(x_coords))]).T
m, c = round(float(lstsq(A, y_coords)[0][0]), 3), round(float(lstsq(A, y_coords)[0][1]), 3)

print(f"Уравнение прямой y = {m}x + {c}")
