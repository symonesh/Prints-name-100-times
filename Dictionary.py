alien_A={
'color' : 'green',
'points' : 5
}
alien_A['x position']=10
alien_A['y position']=18
alien_A['speed']='fast'
if alien_A['speed'] == 'slow':
    x_incriment=1
elif alien_A['speed'] == 'medium':
    x_incriment=2
else:
    x_incriment=3
alien_A['x position']=alien_A['x position'] + x_incriment
print("The new position of the alien is "+str(alien_A['x position'])+ " in x axis ")
