from adminn import admin
class addminstrator(admin):
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
    def show_privilages(self):
        print("The admin can monitor your pc anytime they want")
    def rate_file(self):
        print("10/10")
status=addminstrator("jake","wooli","jake@wolir.com")
status.show_privilages()
status.rate_file()
