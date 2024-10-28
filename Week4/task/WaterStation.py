from agent import Agent
import utils

class WaterStation(Agent):

    def __init__(self, position):
        super().__init__(position)

    def decide(self, percept):
        for k, v in percept.items():
            if utils.is_robot(v):
                v.refill()
        return

    def act(self, environment):
        cell = self.sense(environment)
        decision = self.decide(cell)
        print(decision)

    def __str__(self):
        return '💧'