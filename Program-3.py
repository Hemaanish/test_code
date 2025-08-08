a=int(input('enter a value to generate series of numbers'+' '))
s=0
if a%2==0:
    a-=-1
    for i in range(1, a + 1):
        s += i
        print(s, end='' if i == a else ',')
        s = i
else:
    for i in range(1, a + 1):
        s += i
        print(s, end='' if i == a else ',')
        s = i
