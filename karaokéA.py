class Player :
    def __init__ (self, name, bestScore, score) :
        self.pseudo = name
        self.meilleurScore = bestScore
        self.score = score
        self.chanson = [0, 1, 2, 3, 4]
    def getPseudo (self) :
        return self.pseudo
    def getBestScore (self) :
        return self.bestScore

player1 = Player ("Joueur1", 0, 50)
player2 = Player ("Joueur2", 0, 50)
player3 = Player ("Joueur3", 0, 50)
player4 = Player ("Joueur4", 0, 50)

pseudo1 = player1.getName()
pseudo2 = player2.getName()
pseudo3 = player3.getName()
pseudo4 = player4.getName()

print ("Bienvenue ", player1, player2, player3, player4, "!")
print ("Le jeu va commencer !")


    