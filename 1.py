num = int(input('Введите число: '))
nums_sum = 0

counter = 1
while True:
    if ((num//counter)%10)!=0:
        nums_sum += ((num//counter)%10)
    else:
        break
    counter *= 10

print(nums_sum)