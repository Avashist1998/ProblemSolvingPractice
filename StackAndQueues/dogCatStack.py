


class animal:
    def __init__(self, name, Type):
        self.name = name
        self.Type = Type
        self.order = 0
    def getName(self):
        return self.name
    
    def getType(self):
        return self.Type

    def setOrder(self, order):
        self.order = order


class dog(animal):
    def __init__(self, name):
        animal.__init__(self, name, 'dog')
    
class cat(animal):
    def __init__(self, name):
        animal.__init__(self, name, 'cat')


class dogCatStack():
    def __init__(self):
        self.size = 0
        self.order = 0
        self.dogQueue = list()
        self.catQueue = list()

    def setSize(self):
        self.size = len(dogQueue) + len(catQueue)

    def enqueue(self, newAnimal:animal):
        newAnimal.order = self.order
        if (newAnimal.getType == 'dog'):
            self.dogQueue.append(newAnimal)
        else:
            self.catQueue.append(newAnimal)
        self.order += 1
        self.setSize()
    

    def dequeue(self):
        self.setSize()
        if (self.size>0):
            if (len(self.dogQueue) == 0):
                return self.catQueue.pop(0)
            elif (len(self.catQueue) == 0):
                return self.dogQueue.pop(0)
            else:
                if (self.dogQueue[0].order <= self.catQueue[0].order):
                    return self.dogQueue.pop(0)
                else:
                    return self.catQueue.pop(0)
        else:
            return None

    def dequeueDog(self):
        self.setSize()
        if (len(self.dogQueue) != 0):
            return self.dogQueue.pop(0)
        return None

    def dequeueCat(self):
        self.setSize()
        if (len(self.catQueue) != 0):
            return self.catQueue.pop(0)
        return None
        

