from class_product import Grass
from class_product import Smartphone
from class_product import Product
from class_categoy import Category

sp1 = Smartphone("iphone", "14", "grey", 100000, 5, "100", "pro", "128gb")
sp2 = Smartphone("iphone", "13", "grey", 50000, 10, "100", "pro", "128gb")
gr1 = Grass("grass", "outdoor", "green", 100, 10, "Russia", "1m")
print(sp1)
print(gr1)
total = Product.__add__(sp1, sp2)
print(total)
