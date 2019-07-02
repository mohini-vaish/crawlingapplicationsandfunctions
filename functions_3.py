#to store many values in one variable we put a star and this means we are making it as a tuple
def add(*x):
   print(x)

add(12,45,3,6,7,5)

def student(name,age,*course):
    print('name:',name)
    print('age:',age)
    print('course:',course)
student('ram',20,'python','ML','Graphics')

#*args
#**kwargs=keyword arguments
def students(**details):
    print(details)

students(name='ram',age=20,course_1='python',course_2='ML')

'''def add(*x):
    print(sum(x))
    s=0
    for i in x:
        s+=i
    print(s)

add(3,67,7)'''