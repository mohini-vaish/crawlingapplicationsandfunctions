def add(x,y):
     z=x+y
     print('sum is:',z)
def sub(x,y):
     z=x-y if x>y else y-x
     print('Diff is:',z)
def div(x,y):
     if y==0:
       pass#to skip particular function run skip krna code ko iss vale
     else:
       z=x/y
       print('division is:',z)
def mult(x,y):
     z=x*y
     print('multiplication is:',z)
def errorhandler(*args):
    print('invalid choice')

'''add(4,5)
div(10,3)
mult(100,5)
sub(2,7)
'''

print("""
1.ADD
2.SUBTRACT
3.DIVISION
4. MULTIPLICATION""")


ch=input("Enter your choice:")
num_1=int(input("enter first number:"))
num_2=int(input("enter second  number:"))
operations =   {"1":add,
                "2":sub,
                "3":div,
                "4":mult}
#operations[ch](num_1,num_2)
operations.get(ch,errorhandler)(num_1,num_2)#we can also use get(ch).(num_1,num_2)