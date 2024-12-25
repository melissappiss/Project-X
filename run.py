'''import turtle, random
from time_manager import TimeStep
from bodies.planet import *
from bodies.star import *
from physics_manager import PhysicsManager

win = turtle.Screen()
win.title("Gravity Simulator X")
win.setup(1200, 800)
win.bgcolor("black")
win.tracer(0)

#body
#setRadius: cambia le dimensioni del corpo
#setColor: cambia il corpo della sfera

#time
#setTempo: cambia la velocità
#eachTime: fai un azione ogni tot secondi

#Body(massa, posx, posy, vx, vy)

#timeStep = TimeStep()
#timeStep.setTempo("0.1x")

#bodies = [Planet(random.randint(3, 15), random.randint(-300, 300), random.randint(-300, 300), random.randint(-300, 300),  random.randint(-300, 300)) for _ in range(0, 5)]
#bodies = [Planet(1, -400, 0, 0, -2000), Planet(1, 400, 0, 0, 2000), Planet(1, 0, -400, 2000, 0), Planet(1, -0, 400, -2000, 0), Star(0.5, 0, 0, 0, 0)]


physicsManager = PhysicsManager(bodies)
def main():
	while True:
		win.update()
		timeStep.nextStep()
		physicsManager.applyAllForces()
		for body in bodies:
			timeStep.eachTime(3, body.clear)
			body.updateAll(timeStep.getStepTime(), timeStep.getTempo())
			#timeStep.eachTime(0.1, body.drawTrail)
			body.draw()
'''
import turtle
from time_manager import TimeStep
from physics_manager import PhysicsManager

def run_simulation(bodies):
    win = turtle.Screen()
    win.title("Celestial Simulator X")
    win.setup(1200, 800)
    win.bgcolor("black")
    win.tracer(0)

    timeStep = TimeStep()
    physicsManager = PhysicsManager(bodies)

    while True:
        win.update()
        timeStep.nextStep()
        physicsManager.applyAllForces()

        '''# Applica le forze solo ai corpi con velocità non nulla
        for body in bodies:
            if body.speed_x != 0 or body.speed_y != 0:
                physicsManager.applyAllForces()'''

        for body in bodies:
            body.updateAll(timeStep.getStepTime(), timeStep.getTempo())
            body.draw()

