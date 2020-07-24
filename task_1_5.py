# Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь.
import math

def cal_square(ab,bc):

    if ab<0 or bc<0 :
        raise ValueError("One of the side is less or equal ZERO")

    g = math.sqrt(ab*ab+bc*bc)

    p = (ab+bc+g)/2
    s = math.sqrt(p*(p-ab)*(p-bc)*(p-g))

    print(f"Для треуголника с катетом {ab} и вторым катетом {bc} гипотенуза равна: " + str(g))
    print("а площадь S = " + str(s))


a1 = int(input('Введите целое число для первого катета: '))
b1 = int(input('Введите целое число для второго катета: '))

square = cal_square(a1,b1)
print(square)
