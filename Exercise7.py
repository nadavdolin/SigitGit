
def InputToCache(key,value):
     cache[key]=int(value)

def DecoratorCache(func,data):
    key=func+data
    if key in cache:
        return cache[key]
    else:
        data_split=data.split(',')
        value=adding(data_split)
        InputToCache(key,value)
        return value



def adding(data):
    return int(data[0])+int(data[1])

cache={}
DecoratorCache('adding','1,5')