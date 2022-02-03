sandwichs=['Chicken Sandwich','Egg Sandwich','Seafood Sandwich','Roast Beef Sandwich']
sandwich_orders=['Egg Sandwich','Seafood Sandwich','pastrami sandwich']
finished_order=[]
unavilable_stuff='pastrami'
while sandwich_orders:
    finished_order=sandwich_orders.pop()

    if unavilable_stuff in finished_order:
        print("Your order for "+finished_order+" cannot be completed because of no "+unavilable_stuff)
    else:
        print("Your order for "+finished_order+"is done!!")

