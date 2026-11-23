class ProductOfNumbers(object):
    def __init__(self):
        self.prods = [1]

    def add(self, num):
        
        if num == 0:
            self.prods = [1]
        else:
            self.prods.append(self.prods[-1] * num)

    def getProduct(self, k):
       
        curlen = len(self.prods)
        if k >= curlen:
            return 0
        return self.prods[-1] // self.prods[curlen - 1 - k]
obj = ProductOfNumbers()
obj.add(3)
obj.add(0)
obj.add(2)
obj.add(5)
obj.add(4)
print(obj.prods)

print(obj.getProduct(2))

print(obj.getProduct(3))
print(obj.getProduct(4))
obj.add(8)
print(obj.getProduct(2))