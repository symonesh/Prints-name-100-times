fav_languages={
    'jen':'python',
    'josh':'c',
    'jeff':'java'
}
friends=['jen','josh','pepper']
x=0
for names in fav_languages.keys():
    if friends[x]==names:
        print("Helloo "+ str(names)+ " you fav language is "+fav_languages[names])
        x+=1
    else:
        print(friends[x].title()+ " is not in the list")