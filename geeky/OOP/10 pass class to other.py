class main():
    def __init__(self, i):
     self.m1 = i
    def paramain(self):
        print("this is", self.m1)

class stsmeth:
    @staticmethod
    def func(n):
        print(callmain.m1, " passed in other class" )
        n.paramain()


callmain = main("main class")
stsmeth.func(callmain)
