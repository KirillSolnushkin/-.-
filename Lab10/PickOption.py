from Agent import Agent

class PickOption:
    def __init__(self, Agent: Agent):
        self.Agent = Agent
        self.is_pick = False

    def set_pick(self, is_pick):
        self.is_pick = is_pick
        self.Agent.notify(self, "Підібрати комплект")