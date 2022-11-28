"""
Mengenal fungsi __init__ 

"""

class GamePC:
    def __init__(self, nama, genre):
        self.nama = nama
        self.genre = genre

    def __str__(self):
        return f"{self.nama}"

    # method cetak nama game

    def printNama(self):
        print("Nama game nya adalah: "+self.nama+" dengan genre nya "+self.genre)
# Instansiasi dengan nama game 1

Game1 = GamePC("Far Cry 3","Action,Shooting,Survival")

#panggil method nya 

Game1.printNama()

