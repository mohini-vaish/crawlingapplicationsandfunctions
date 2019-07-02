num=int(input('Enter a number:'))
'''flag=True
for n in range(2,int(num/2)):
    if num % n==0:
        #print("not prime")
        flag= True
    else:
        #print("prime")
        flag=False

if flag==True:
    print('Not a prime number')
else:
    print('prime number')
    '''

for n in range(2,num):
    if num % n==0:
        print("not prime")
        break
else:
    print('prime number')
