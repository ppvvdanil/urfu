a = [int(num.strip()) for num in str(input("Введите координаты точки А (пример 3,4,5) -> ")).split(",")]
b = [int(num.strip()) for num in str(input("Введите координаты точки B (пример 3,4,5) -> ")).split(",")]
c = [int(num.strip()) for num in str(input("Введите координаты точки C (пример 3,4,5) -> ")).split(",")]
d = [int(num.strip()) for num in str(input("Введите координаты точки D (пример 3,4,5) -> ")).split(",")]

print(f"А = {a}, B = {b}, C = {c}, D = {d}")

x1,y1,z1 = a
x2,y2,z2 = b
x3,y3,z3 = c
x4,y4,z4 = d

ux, uy, uz = x2-x1, y2-y1, z2-z1
vx, vy, vz = x3-x1, y3-y1, z3-z1

nx = uy * vz - uz * vy
ny = uz * vx - ux * vz
nz = ux * vy - uy * vx

# Проверка вырождения (нормаль почти нулевая)
if nx == 0 and ny == 0 and nz == 0:
    print("Точки A,B,C коллинеарны")
    exit()

d0 = -(nx * x4 + ny * y4 + nz * z4)

print(f"Уравнение плоскости {nx}*x + {ny}*y + {nz}*z + ({d0}) = 0")