import PyGine

from Population import Population
from Target import Target
from player import player


class Scene1(PyGine.Scene):
    def __init__(self):
        super().__init__()
        self.time = 0

    def start(self):

        self.addGameObject(Target())

        self.simTime = 1000

        self.population = Population(self.simTime)

        self.population.renew()
        PyGine.PyGineGame.game.instanciate(self.population)


    def freshPop(self):

        print("fresh pop")
        self.population.finish()
        print("Best of the last : " + str(self.population.getBest().score))
        self.population.smartRenew()
        print("end renew")



    def update(self,dt):

        if self.time >= self.simTime:
            self.freshPop()
            self.time = 0

        self.population.setTime(self.time)

        self.time += 1
        PyGine.PyGineGame.game.surface.fill((0, 0, 0))
