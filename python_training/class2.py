class MGM:
    def Walk3(self):
        print("Walk- MGM")

class MGF:
    def Walk4(self):
        print("Walk- MGF")

class PGM:
    def Walk6(self):
        print("Walk- PGM")

class PGF:
    def Walk7(self):
        print("Walk- PGF")

class Mom(MGM,MGF):
    def Walk2(self):
        print("Walk-Mom")

class Dad(PGM,PGF):
    def Walk5(self):
        print("Walk-Dad")


class infant(Mom,Dad):
    def Walk1(self):
        print("Walk- infant")

Baby=infant()
Baby.Walk()




 temp.dd+=days
 if temp.dd > 30:
     mm = temp.dd // 30
     temp.dd=temp.dd-mm*30
     temp.mm+=mm
     return temp
 else: 
