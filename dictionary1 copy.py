poll={
    'john':'python',
    'jeff':'c',
    'anne':'python',
    'josh':'java'
}
x=0
peoples=['josh','jeff','anne','josh','felix','ash']
for names   in  poll.keys():
    print("thank you "+names+ " for taking the poll")
for people in peoples: 
    if people not in poll.keys():
        print(people+" please take the pooll")
        x+=1

    
    