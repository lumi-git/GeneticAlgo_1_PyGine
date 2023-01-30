import random

import PyGine
import pygame
from PyGine import Vector3


class player(PyGine.GameObject) :

    def __init__(self,nbGenes = 0,adn=None):
        super().__init__()
        self.nbGenes = nbGenes
        self.speed = 1
        if adn == None:
            self.adn = [ Vector3(( random.random() -0.5 )*0.1*2*self.speed,( random.random() -0.5 )*0.1*2*self.speed) for i in range(nbGenes)]

        else :
            self.adn = adn
            self.nbGenes = len(adn)
        self.velocity = Vector3(0,0,0)
        self.score = 0
        self.addComponent(PyGine.DrawRectComponent(self, (255, 0, 0)))
        self.arrived = False
        self.distParcourue = 0
    def start(self):
        self.transform.position = Vector3(400, 300)
        self.transform.scale = Vector3(10, 10,0)


    def move(self,time):

        if time < self.nbGenes:
            self.velocity += self.adn[time]



    def update(self,dt):
        super().update(dt)
        self.transform.position += self.velocity

        dist = (PyGine.PyGineGame.game.getCurrentScene().getGameobject("Target").transform.position - self.transform.position)
        disteucl = (dist.x**2 + dist.y**2)
        if disteucl < 200 :
            self.score = 1

        else :
            self.score = disteucl

        if self.transform.position.x < 0 or self.transform.position.x > 800 or self.transform.position.y < 0 or self.transform.position.y > 600 :
            self.score = 1000000000

    def setScore(self ):
        #le score c'la dif entre la cible et le truc
        pass

