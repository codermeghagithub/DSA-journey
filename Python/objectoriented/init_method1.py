class Ani:

    def __init__(self,domain,kingdom):
        self.domain=domain
        self.kingdom=kingdom
        # print("")


    def jill(self):
        print("the value of jill method is",self.domain,self.kingdom)

      

h1=Ani("combozoya","animaliya")
h2=Ani("mameliya","human")
print(type(h1))        

# Ani.jill(h1)
# Ani.jill(h2)

h1.jill()
h2.jill()




