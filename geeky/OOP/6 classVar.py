class Classname:
    clsvar = "creating class variable befor cnstractor"
   
    # cnstractor will be here


    @classmethod
    def accessible(cls, m):
        cls.n = m
        print(cls.clsvar, "\nclass variable accessing in classmethod\n", cls.n)


object1 = Classname()
p = Classname.accessible("first parametter in class method alwyes will be \'cls\'")
print(object1, p)
