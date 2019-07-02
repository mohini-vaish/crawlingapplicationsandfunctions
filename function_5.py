def calc(x,y):
    z1=x+y
    z2=x-y
    z3=x*y
    z4=x/y
    return z1,z2,z3,z4
a=calc(4,5)
print(a)

#packing,unpacking (here we are returning so many values in only one tuple)

a,b,c,d=calc(2,4)
print('a:',a,'b:',b,c,d)#unpacking

#print(a,b,*c) and this will make c as a list not a tuple