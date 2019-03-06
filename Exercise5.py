import math
#Round up a number
def roundup(x):
    return int(math.ceil(x / 10.0)) * 10

#check if the ID is ok
def check_id():
    ID=input('Please enter your ID\n')
    right=int(ID[-1:])
    ID=int(ID)/10
    ID=round(ID-0.5)
    #Split the ID
    temp_ID=list(str(ID))
    temp=0
    sum1=0
    num=1

    for i in temp_ID:
        temp=int(i)*num
        if temp>=10:
            minisum=list(str(temp))
            for j in minisum:
                sum1+=int(j)
        elif temp<10:
         sum1+=temp
        if num==1:
            num+=1
        else:
            num-=1
    roundnum = roundup(sum1)
    #check the number
    if roundnum-sum1==right:
        return 1
    else:
        return 0

answer=check_id()
if answer==1:
    print('the ID is ok')
else:
    print('the ID is not ok')
