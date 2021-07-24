num = int(input('Factorial number:'))
test = 1
def fact(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num*(fact(num - 1)) 
x = fact(num)
print('hello world')
print(f'Factorial: {x}')