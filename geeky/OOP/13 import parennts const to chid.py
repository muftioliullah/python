class parent():
    def __init__(self, m):
        self.money = m
        print(self.money)
    

class child(parent):
    def __init__(self, m, n):
        super().__init__(m)  # theare are no self variable for formal argument  or  clone:
        self.price = n
        print(self.price)
    


mon = parent("parents class constrator")
pric = child("parent class cnstractor in child constrator",
             "parents constaractors positonal argument in child-super")


