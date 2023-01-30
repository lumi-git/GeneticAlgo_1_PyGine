import random

import PyGine
from PyGine import DrawRectComponent, TextComponent

from player import player


class Population(PyGine.GameObject):

    def __init__(self, simTime):
        super().__init__()
        self.timeSim = simTime
        self.players = []
        self.updated = 0
        self.popSize = 100
        self.nbGenes = 100
        self.time = 0
        self.bs = None
        self.meanscore = 0
        self.highest = 0
        self.addComponent(TextComponent(self, "Best score : " + str(self.highest), (255, 255, 255)))

    def mute(self):
        for i in range(self.nbGenes):
            self.players[i].mute(self.players[i + len(self.players) // 2])

    def setTime(self, time):
        self.time = time

    def update(self, dt):
        if not self.time % (self.timeSim // self.nbGenes):
            for player in self.players:
                player.move(self.updated)
            self.updated += 1

    def getBest(self):
        best = self.players[0]

        for player in self.players:
            if player.score < best.score:
                best = player
            if player.score > self.highest:
                self.highest = player.score
            self.meanscore += player.score
            self.meanscore /= len(self.players)
        return best

    def finish(self):
        for player in self.players:
            player.setScore()

    def renew(self):
        self.updated = 0
        self.time = 0
        for player_ in self.players:
            player_.destroy = True

        newplayers = []

        for i in range(self.popSize):
            pl = player(nbGenes=self.nbGenes)
            PyGine.PyGineGame.game.instanciate(pl)
            newplayers.append(pl)

        self.players = newplayers


    def smartRenew(self):
        self.time = 0
        self.updated = 0
        self.bs = self.getBest()
        self.select()
        self.mutation()
        self.instanciateAll()
        self.getComponent("TextComponent").setText("Best score : " + str(self.bs.score) + "Mean : " + str(self.meanscore))

    def mutation(self):

        newplayers = []

        lastBest = player(adn=self.bs.adn)
        lastBest.getComponent("DrawRectComponent").color = (0, 255, 0)
        newplayers.append(lastBest)

        lastBest = player(adn=self.bs.adn)
        lastBest.getComponent("DrawRectComponent").color = (0, 255, 0)
        newplayers.append(lastBest)

        lastBest = player(adn=self.bs.adn)
        lastBest.getComponent("DrawRectComponent").color = (0, 255, 0)
        newplayers.append(lastBest)

        #take the start of the gene of a player and combine it with the end of another player
        for i in range(1, self.popSize):
            adn = random.choice(self.players).adn
            adn2 = random.choice(self.players).adn
            adn = adn[:len(adn)//2 ] + adn2[len(adn2)//2:]
            pl = player(adn=adn)
            newplayers.append(pl)

        self.players = newplayers




    def select(self):

        for player_ in self.players:
            player_.destroy = True
            player_.score /= self.highest

        newplayers = []

        for i in range(self.popSize):
            # the greatest score the player gets, the more chance he has to be selected
            if random.random() > self.players[i].score :

                adn = self.players[i ].adn
                pl = player(adn=adn)
                newplayers.append(pl)

        while len(newplayers) < self.popSize:
            pl = player(self.nbGenes)
            newplayers.append(pl)

        self.players = newplayers


    def instanciateAll(self):
        for p in self.players :
            PyGine.PyGineGame.game.instanciate(p)