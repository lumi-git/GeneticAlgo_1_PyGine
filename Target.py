import PyGine


class Target(PyGine.GameObject) :

    def start(self):
        self.name = "Target"
        self.transform.position = PyGine.Vector3(50, 300)
        self.transform.scale = PyGine.Vector3(100, 10,0)
        self.addComponent(PyGine.DrawCircleComponent(self, (255, 0, 0), 10))