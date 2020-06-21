class my_class:
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname
    def length(self):
        return len(self.surname)

p1=my_class("John","Doe")
print(p1.length())


