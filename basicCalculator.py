num1= int (input('Enter first number : '))
num2 = int (input('Enter second number : '))
op = input ('Enter operator : ')

if op == '+' :
    print('The addition of these two is', num1+num2)

elif op == '-' :
    print('The subtraction of these two is', num1-num2)

elif op == '*' :
    print('The multiplication of these two is', num1*num2)

elif op == '/' :
    print('The division of these two is', num1/num2)

elif op == '%' :
    print('The modulo of these two is', num1%num2)

else :
    print('Oops! Seems like you have entered an Invalid Operator.')