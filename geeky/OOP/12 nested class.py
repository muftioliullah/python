class dipartment():
    def first(self):
        self.right = self.second()
    
    
    class second():
        def  left(self):
            self.front= "nested calss"
    m = second()
    m.left()

nest = dipartment()
nest.first()
nn = nest.m.front

print(nn)

