class Cat:
    species = 'cat'
    stt = 1
    name = "tom",
    color="vang"
    #init method
    def __init__(self, cat_name, cat_color):
        self.name = cat_name
        self.color = cat_color
        self.stt = Cat.stt
        Cat.stt +=1
    def catchMouse(self, name_mouse):
        print(self.name, "Catch", name_mouse)

tom = Cat("tom", 'vang') # tự động gọi đến hàm init => tom.name tom.color
meo = Cat("meo", 'nau')
print(tom.stt)
print(meo.stt)
