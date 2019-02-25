secretcode =123456
CurrentMoney=2000
number=0
while number!=4:
    PersonSecretCode = int(input('Please enter your Id : \n'))
    if secretcode == PersonSecretCode:
        print('1-Print balance \n'
              '2-Attracting money \n'
              '3-Change secret code \n'
              '4-Exit \n')
        number=int(input())
        if number==2:
            print('How much money you want to attracth:'
                  '20,50 or another? \n')
            money=int(input())
            CurrentMoney-=money
        elif number==1:
            print('You have:' + str(CurrentMoney) + 'Shekels \n')
        elif number==3:
            code=int(input('Please enter your new secret code \n'))
            secretcode=code