import shapefile
w = shapefile.Writer("soal8", shapeType=shapefile.POLYGON)
w.shapeType


w.field("kolom1", "C")
w.field("kolom2", "C")

w.record("ngek", "satu")

w.poly([[[1, 3], [5, 3], [1, 2], [5, 2], [1, 3]]])

w.close()
