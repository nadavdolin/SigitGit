#Conver a word like:aaaaabbbccddtt to a5b3c2d2t2
def convert(string):
    count=1
    new_word=''
    index=0
    for index in range(len(string)-1):
        if string[index]==string[index+1]:
            count+=1
        else:
            new_word=new_word + string[index] + str(count)
            count=1
    new_word = new_word + string[index] + str(count)
    return str(new_word)


s='aaaaabbbccddtt'
new=convert(s)
print(str(new))
