from collections import namedtuple

Koordinat = namedtuple("Koordinat", ["x", "y"])

titik1 = Koordinat(2, 4)

# menggunakan indeks elemen
print("x = ", titik1[0])
print("y = ", titik1[1])

# menggunakan field name
print("\nx = ", titik1.x)
print("y = ", titik1.y)

# menggunakan getattr()
print("\nx = ", getattr(titik1, "x"))
print("y = ", getattr(titik1, "y"))
