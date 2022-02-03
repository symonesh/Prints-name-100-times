def roll_dice():
    from random import randint
    x=randint(1,6)
    print(x)
x=0
while x<10:
    roll_dice()      
    x+=1