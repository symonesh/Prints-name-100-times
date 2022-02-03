class resturant():
    def __init__(self,resturant_name,cuisine_type,open,close):
        self.resturant_name=resturant_name
        self.cuisine_type=cuisine_type
        self.open=open
        self.close=close
    def describe_resturant(self):
        print("The resturant name is "+self.resturant_name.title())
    def food(self):
        print("The resturant offeres "+self.cuisine_type.title())
    def time_open(self):
        print("The resturant opens at "+self.open.title())
    def time_close(self):
        print("The resturant closes at "+self.close.title())
class ice_Cream(resturant):
    def __init__(self,resturant_name,cuisine_type,open,close):
        self.resturant_name=resturant_name
        self.cuisine_type=cuisine_type
        self.open=open
        self.close=close
        self.flavors={'vanilla','chocolate'}
    def ice_cream_order(self):
        for flavor in self.flavors:
            print(flavor)
ice=ice_Cream("Cuzzzz","veg","9:30","4:40")
ice.ice_cream_order()   

