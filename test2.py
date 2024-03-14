import os
mypath = 'metadata'
print('hello')
abspath = os.path.abspath(mypath)
print(abspath)

for i in os.listdir(abspath):
    path = os.path.join(abspath, i)
    #print(path)

print('End')


mystr = '123 asdre 5432 dfret'

pos = 0

def Myrev(mystr2, pos=0):
    res = ''
    for i in range(pos, len(mystr2)):
        if mystr2[i:i+1] != ' ':
            dd = mystr2[i+1:]
            res = Myrev(dd, i+1) + mystr2[i:i+1]
            i = len(res)+1
        else:
            res = res + ' '
        print(i)

    return res


#print('---')
#print(mystr[5:1:-1])
print('---')

#print(Myrev(mystr))

def f(sum, l=[]):
    l.append(sum)
    print(l)

l=[1]
f(10)
f(10)
f(10, l)
f(1
f(10)

l1 = [1,2,3]
l2 = [2,3,4]
l3 = l1.extend()
print(l3)