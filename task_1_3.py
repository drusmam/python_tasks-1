# Дана длина ребра куба. Найти объем куба и площадь его боковой поверхности.
import math

a = int(input("Ведите любое действительное число: "))

capacity = math.pow(a,3)
square = math.pow(a,2)

print(f"Объем куба со сороной {a} равен " + str(capacity) )
print("а площадь боковой поверхности -  " + str(square))

