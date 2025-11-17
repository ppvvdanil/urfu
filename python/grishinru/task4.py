def get_line(d1: [int, int], d2: [int, int]):
    x1, y1 = d1
    x2, y2 = d2

    if x1 - x2 == 0 and  y1 - y2 == 0:
        return None

    dx = round(b[1] - a[1], 3)
    dy = round(a[0] - b[0], 3)
    dc = round(-(dx * c[0] + dy * c[1]), 3)

    return (dx, dy, dc)

def determinant(a, b, c, d):
    return a * d - b * c

def determine_line(d1: [int, int], d2: [int, int], d3: [int, int], d4: [int, int]):
    line1 = get_line(d1, d2)
    line2 = get_line(d3, d4)

    if line1 is None and line2 is None:
        return "Пары точек вырождены"
    if line1 is None:
        return "Пара A, B - вырожденная"
    if line2 is None:
        return "Пара C, D - вырожденная"

    dx1, dy1, dc1 = line1
    dx2, dy2, dc2 = line2

    det = determinant(dx1, dy1, dx2, dy2)

    if det != 0:
        x = determinant(-dc1, dy1, -dc2, dy2) / det
        y = determinant(dx1, -dc1, dx2, -dc2) / det

        return f"Пересекаются в точке [{x}, {y}]"
    else:
        on_same = abs(dx1 * d3[0] + dy1 * d3[1] + dc1) == 0
        if on_same:
            return "Прямые коллинеарны"
        else:
            return "Прямые параллельны"

student_ticket = str(input("Введите номер студенческого билета -> "))
a, b, c, d = ([int(student_ticket[0:4][0:2]), int(student_ticket[0:4][2:4])],
              [int(student_ticket[4:8][0:2]), int(student_ticket[4:8][2:4])],
              [int(student_ticket[0:4][0:2]), int(student_ticket[4:8][2:4])],
              [int(student_ticket[0:4][2:4]), int(student_ticket[4:8][0:2])]
           )

print(f"А = {a}, B = {b}, C = {c}, D = {d}")
print(determine_line(a, b, c, d))