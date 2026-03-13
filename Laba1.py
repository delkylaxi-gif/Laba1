def Nod(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = Nod(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

a, b, c = map(int, input().split())
gcd, x0, y0 = Nod(a, b)
if c % gcd != 0:
    print("Impossible")
else:
    # Умножаем найденные коэффициенты на (c / gcd), чтобы получить решение уравнения ax + by = c
    x1 = x0 * (c // gcd)
    y1 = y0 * (c // gcd)    
    step = b // gcd   
    # Находим наименьшее неотрицательное x
    # Для этого берём остаток от деления x1 на step
    # В Python остаток от деления отрицательного числа даёт положительное число
    x_min = x1 % step
    y_min = (c - a * x_min) // b
    
    # Выводим результат
    print(x_min, y_min)
print('Лысенко Владимир Александрович группа 090301-Пова-о25')