import math

a = int(input('Введите А'))
b = int(input('Введите B'))
c = int(input('Введите C'))

# A = Bx + Cy
# Представление существует, только если А делится на НОД(|B|,|C|)
# Находим НОД(b,c) с помощью функции gcd

if a % math.gcd(abs(b),abs(c)) == 0:
    print('Число ',a,' можно представить в виде линейной целочисленной комбинации чисел',b, 'и',c)
else:
    print('Число ',a,' можно представить в виде линейной целочисленной комбинации чисел',b, 'и',c)


