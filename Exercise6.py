def Mapfunc(func,f):
    new_array=list()
    for i in f:
        x=func(i)
        new_array.append(str(x))

    return new_array


def multi(x):
    return x*2


ff=(1,2,3)
new_ar=str(Mapfunc(multi,ff))
print(new_ar)