import random
class dr_nim:

    def __init__(self):
        self.zogice = []
        self.indeks = 0
    
    def dodaj(self, n):
        for i in range(n):
            self.zogice.append('zoga()')
    
    def stevilo_zogic(self):
        return len(self.zogice)


    def racunalnik(self):
        if len(self.zogice) % 3 == 0:
            self.zogice = self.zogice[random.randint(1,2):]
        else:
            self.zogice = self.zogice[len(self.zogice) % 3:]

    def odstej(self,st):
        self.zogice = self.zogice[int(st):]
    
    
