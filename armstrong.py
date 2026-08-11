num=int(input("Enter a number: "))

temp=num
sum = 0
while num > 0:

    digit = num % 10
    cube = digit ** 3
    sum = sum + cube 
    num = num // 10

if temp == sum:
    print('Armstrong Number')
else:
    print('Not Armstrong Number ')