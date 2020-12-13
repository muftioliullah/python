class Classname:
    def __init__(self ):
        self.variable2 ="instace variable must be with instance method, its call \"cnstractor\" and \'self\' variable"
    def meth(self):
        self.variable1_2 ="variable with self & can you call it inside & outsite off class"
        variable2_2 = "variable without self & can't call it outsite off class"
        print(variable2_2)
#


object1 = Classname()
b = object1.variable2
object1.meth()
d = object1.variable1_2
print(b,"\n", d)
