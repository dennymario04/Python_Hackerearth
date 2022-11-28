# buat class mobile legend

class GameMobile :
#Atribut
    Name = "Mobile Legend Bang Bang"
    Genre = "Moba"
#Method
    def change_name(self,new_name):
        self.Name = new_name
    def change_genre(self,new_genre):
        self.Genre = new_genre
#instansiasi
game = GameMobile()
"""
Instansiasi berguna untuk akses atribut didalam sebuah class

"""
print(game.Name)
print(game.Genre)

game.change_name("Clash Of Clans")
game.change_genre("Strategy")

print(game.Name)
print(game.Genre)

"""
Self berfungsi sebagai penunjuk objek / method itu sendiri
"""

