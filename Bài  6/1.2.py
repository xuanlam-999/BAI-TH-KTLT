class Hinhchunhat(object):
    def __init__(self,chieudai, chieurong):
        self.chieudai = chieudai
        self.chieurong = chieurong
    def area(self):
        return self.chieudai*self.chieurong

aHinhchunhat = Hinhchunhat(2,3)
print(aHinhchunhat.area())
