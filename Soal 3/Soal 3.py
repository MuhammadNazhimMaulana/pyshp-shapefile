import shapefile
w = shapefile.Writer("soal3", shapeType=1)
w.shapeType
w.shapeType = 3
w.shapeType

w.field("kolom1", "C")
w.field("kolom2", "C")

w.record("ngek", "satu")

w.line([[[1, 1], [2, 2]]])

w.close()
