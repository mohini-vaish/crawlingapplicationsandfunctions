def calc(x,y):
    z=x+y
    #print(z)
    return z

#print(calc(4,5))
s=calc(4,5)

print(s)

def playerhealth():
    health=45
    return health
def enemyhealth():
    health=56
    return health

def game():
    ph=playerhealth()
    eh=enemyhealth()
    if ph<eh:
      print('health low')
    else:
      print('health high')

game()