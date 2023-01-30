import PyGine

from Scene1 import Scene1


class Game(PyGine.PyGineGame):
    def __init__(self):
        super().__init__( 800, 600,self)
        self.addScene(Scene1())
        self.setScene(0)





Game().run()