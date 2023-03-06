class Person:
    def __new__(self,*args,**kwargs):
        print("Inside dunder new")
        return super().__new__(self)
    def __str__(self) -> str:
        print("Inside str dunder")
        return "Name : {0}".format(self.name)
    def __init__(self, name):
        print("Inside init method")
        self.name = name
    

if __name__ == "__main__":
    a = Person("name")
    print(a)
