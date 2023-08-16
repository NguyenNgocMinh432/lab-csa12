class Sieunhan:
    sucmanh = 50
    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac
class Sieunhangao(Sieunhan):
    def __init__(self, para_ten, para_vu_khi, para_mau_sac, para_su_thu):
        super().__init__(para_ten, para_vu_khi, para_mau_sac)
        self.su_thu = para_su_thu
        

sieunhangaohong = Sieunhangao("hong", "kiem", "hong", "dsdsds")
print(sieunhangaohong.su_thu)
# print(sieunhangaohong.color)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}, {self.age} years old"

person = Person("Alice", 30)
print(person)  # Kết quả: Alice, 30 years old