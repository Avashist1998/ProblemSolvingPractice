from enum import Enum


class AnimalType(Enum):
    CAT = "cat"
    DOG = "dog"


class Animal:

    def __init__(self, name: str, animal_type: AnimalType):
        self.name = name
        self.animal_type = animal_type
        self.order = 0

    def get_name(self):
        return self.name

    def get_type(self):
        return self.animal_type

    def set_order(self, order):
        self.order = order


class dog(Animal):

    def __init__(self, name):
        super.__init__(self, name, AnimalType.DOG)


class cat(Animal):

    def __init__(self, name):
        super.__init__(self, name, AnimalType.CAT)


class dogCatStack():

    def __init__(self):
        self.size = 0
        self.order = 0
        self.dog_queue = list()
        self.cat_queue = list()

    def setSize(self):
        self.size = len(self.dog_queue) + len(self.dog_queue)

    def enqueue(self, newAnimal: animal):
        newAnimal.order = self.order
        if newAnimal.get_type is AnimalType.DOG:
            self.dog_queue.append(newAnimal)
        else:
            self.cat_queue.append(newAnimal)
        self.order += 1
        self.setSize()

    def dequeue(self):
        self.setSize()
        if self.size > 0:
            if len(self.dog_queue) == 0:
                return self.cat_queue.pop(0)
            elif len(self.cat_queue) == 0:
                return self.dog_queue.pop(0)
            else:
                if self.dog_queue[0].order <= self.cat_queue[0].order:
                    return self.dog_queue.pop(0)
                else:
                    return self.cat_queue.pop(0)
        else:
            return None

    def dequeue_dog(self):
        self.setSize()
        if len(self.dog_queue) != 0:
            return self.dog_queue.pop(0)
        return None

    def dequeue_cat(self):
        self.setSize()
        if len(self.cat_queue) != 0:
            return self.cat_queue.pop(0)
        return None
