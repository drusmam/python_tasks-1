import math

a = int(input("Ведите любое действительное число: "))
b = int(input("Введите ещё одно действительное число: "))

sum_num = a+b
dif_num = a-b
mult_num = a*b

print("Сумма ваших чисел = " + str(sum_num))
print("Разность ваших чисел = " + str(dif_num))
print("А произведение ваших чисел = " + str(mult_num))

x = a
y = b

mdl = (math.fabs(x) - math.fabs(y))/(1 + math.fabs(x*y))
print("Если ваше первое чило присвоить Х")
print("а второе чило присвоить Y")
print("то результат выражения (|x|-|y|/1+|xy|) равен " + str(mdl))


aver_num = math.sqrt(x*y)
print("Вот среднее геометрическое ваших чисел: " + str(aver_num))

print("Теперь прикинем чему равны гипотенуза прямоугольного треугольника и его площадь)))")

a1 = int(input('Введите целое число для катета AC: '))
b1 = int(input('Введите целое число для катета BC: '))

def cal_square(ab,bc):

    if ab<0 or bc<0 :
        raise ValueError("One of the side is less or equal ZERO")

    g = math.sqrt(ab*ab+bc*bc)

    p = (ab+bc+g)/2
    s = math.sqrt(p*(p-ab)*(p-bc)*(p-g))

    print(f"Для ваших сторон AB = {ab} и BC = {bc} гипотенуза равна: " + str(g))
    print("а полщадь S = " + str(s))


square = cal_square(a1,b1)
print(square)

