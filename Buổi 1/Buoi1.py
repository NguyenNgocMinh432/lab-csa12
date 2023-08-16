class Dog:
    legs=1;
    
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs

pug = Dog('bug', 2)
print(pug.name)
print (pug.legs)

husky = Dog('husky')
print (husky.name)
print (husky.legs)