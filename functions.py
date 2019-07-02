#function declaration/definition
#global variables
x=10
y=16
def add():
    #local scope
    global x
    x=12
    y=13
    z=x+y
    print(z)

#function calling
# print(add())#none is here because we are expecting a value which function returns  but here is no such value is present so returning a none value.
add()

#z=x-y
#will not run as x and y are locally defined #print(z)

z=x+y
print(z)


