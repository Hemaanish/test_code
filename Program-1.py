from numpy import double
a=double(input('enter the a value'+' '))
b=double(input('enter the b value'+' '))
type_of_op=input('enter the type of operation required to perform'+' ')
def calculator(a,b,type_of_op):
    if type_of_op =='+':
        sum=a+b
        print(f'The addition of a and b is {sum}')
    elif type_of_op =='-':
        sub=a-b
        print(f'The subtraction of a and b is {sub}')
    elif type_of_op == '*':
         mul = a * b
         print(f'The multiplication of a and b is {mul}')
    elif type_of_op == '/':
        div = a / b
        print(f'The division of a and b is {div}')
calculator(a,b,type_of_op)



