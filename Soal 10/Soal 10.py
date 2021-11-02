import shapefile
print(1194025 % 8)
# Karena angka kedua terakhir npm saya adalah 2 jadi saya membuat 2 segitiga sama sisi

w = shapefile.Writer("soal10", shapeType=shapefile.POLYGON)
w.shapeType


w.field("kolom1", "C")
w.field("kolom2", "C")

w.record("Muhammad", "Nazhim")
w.record("One", "Piece")


w.poly([[[2, 1], [8, 1], [5, 5], [2, 1]]])

w.poly([[[9, 1], [15, 1], [12, 5], [9, 1]]])


w.close()
