#Ce fichier a pour but de d'avoir la classe de base pour tout les items

class Item:
    def __init__(self, name):
        self.name=name

    def getName(self):
        return self.name