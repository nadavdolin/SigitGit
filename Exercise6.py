#Make the func of each one
def Mapfunc(func,f):
    Answer=list()
    for i in f:
        x=func(i)
        Answer.append(str(x))

    #return the answers
    return Answer


def multi(x):
    return x*2


ff=(1,2,3)
new_ar=str(Mapfunc(multi,ff))
print(new_ar)