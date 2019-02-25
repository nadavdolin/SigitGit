def Ex2A():
    sum=0
    number=input('Please enter a number \n')
    while number!='stop':
        sum+=int(number)
        number = input('Please enter a number \n')
    print('the sum of the number is: ' +str(sum))

def Ex2B():
    sum=0
    number=' 1 , 2 , 3 , 4 '
    splitnum=number.split(' , ')
    for i in splitnum:
        sum=sum+int(i)
    print('the sum of the number is: ' + str(sum))

Ex2B()