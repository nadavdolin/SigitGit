#Input the new Key and value in the cache
def InputToCache(key,value):
     cache[key]=int(value)

	
def DecoratorCache(func,data):
    key=func+data
	#check if the we have answer in the cache
    if key in cache:
        return cache[key]
	#make the fund and save the new answer
    else:
        data_split=data.split(',')
        value=adding(data_split)
        InputToCache(key,value)
        return value



def adding(data):
    return int(data[0])+int(data[1])

cache={}
DecoratorCache('adding','1,5')