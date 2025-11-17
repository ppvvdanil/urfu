a = [int(num.strip()) for num in str(input("Введите координаты точки А (пример 3,4,5) -> ")).split(",")]
b = [int(num.strip()) for num in str(input("Введите координаты точки B (пример 3,4,5) -> ")).split(",")]
c = [int(num.strip()) for num in str(input("Введите координаты точки C (пример 3,4,5) -> ")).split(",")]
d = [int(num.strip()) for num in str(input("Введите координаты точки D (пример 3,4,5) -> ")).split(",")]

print(f"А = {a}, B = {b}, C = {c}, D = {d}")

x1, y1, *z1 = a if len(a) == 3 else (*A, 0)
x2, y2, *z2 = b if len(b) == 3 else (*B, 0)
x3, y3, *z3 = c if len(c) == 3 else (*C, 0)

z1 = z1[0]
z2 = z2[0]
z3 = z3[0]

ba = (x1 - x2, y1 - y2, z1 - z2)
bc = (x3 - x2, y3 - y2, z3 - z2)

dot = ba[0] * bc[0] + ba[1] * bc[1] + ba[2] * bc[2]

if dot == 0:
    print("Угол прямой")
elif dot > 0:
    print("Угол острый")
else:
    print("Угол тупой")