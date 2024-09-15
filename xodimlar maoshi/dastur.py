from abc import ABC, abstractmethod

class Xodim(ABC):
    def __init__(self, ism, ishlagan_soat, samaradorlik) -> None:
        self.ism = ism
        self.ishlagan_soat = ishlagan_soat
        self.samaradorlik = samaradorlik

    @abstractmethod
    def maosh(self):
        pass 

    def malumot(self):
        return f"xodim ismi: {self.ism}, ishlagan vaqti {self.ishlagan_soat}, ish samaradorligi {self.samaradorlik}"

class ToliqStavkaliXodim(Xodim):
    def __init__(self, ism, ishlagan_soat, stafka, samaradorlik) -> None:
        super().__init__(ism, ishlagan_soat, samaradorlik)
        self.stafka = stafka
        self.__maoshi = 500

    def maosh(self):
        self.__maoshi += 100 * self.samaradorlik
        return f"{self.__maoshi} USD"

    def malumot(self):
        return f"Toliq stavkali xodim ismi: {self.ism}, ishlagan vaqti {self.ishlagan_soat}, maosh {self.maosh()}"

class YarimStavkaliXodim(Xodim):
    def __init__(self, ism, ishlagan_soat, stafka, samaradorlik) -> None:
        super().__init__(ism, ishlagan_soat, samaradorlik)
        self.stafka = stafka
        self.__maoshi = 250

    def maosh(self):
        self.__maoshi += 250 * self.samaradorlik
        return f"{self.__maoshi} USD"

    def malumot(self):
        return f"Yarm stavkali xodim ismi: {self.ism}, ishlagan vaqti {self.ishlagan_soat}, maosh {self.maosh()}"
    

xodim1 = ToliqStavkaliXodim("John", 12, 75, 1.6)
xodim2 = YarimStavkaliXodim("Tom", 21, 60, 0.7)

print(xodim1.malumot())
print(xodim2.malumot())

# git status agar qizil chiqsa git add . qlnad
# git commit -m "brnch qayd" (qayt izohi)
# git status
# git remote -v  git habdan link olish
# git remote add fayl nomi + gutHub link
# git status
# git push fayl nomi
