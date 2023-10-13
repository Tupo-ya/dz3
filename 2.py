num = int(input('Введите число: '))
fact = num

for i in range(1, num):
    fact = fact * i

print(fact)