places={}
status=True
while status:
    user=input("enter your name\n")
    place=input("Where would you like to go for vaccation?\n")
    places[user]=place
    repeat=input("would you let another person responce?(yes/no)\n")
    if repeat=='no':
        status=False
print("+-------POll result------+")
for user,place in places.items():
    print(user+" wants to visit "+place)