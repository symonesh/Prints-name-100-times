while True:
    try:
        x=int(input(("ENater a number:")))
        y=int(input("Anorher number:"))
        sum=x+y
        print(sum)
    except ValueError:
        print("FUck you")
    else:
        status=input("Enter 'q' to quir")
        if status=='q':
            quit