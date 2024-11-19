from Agent import Agent

class TimePick:
    def __init__(self, Agent: Agent):
        self.Agent = Agent
        self.available_time = []

    def update_time_slots(self, date):
        self.Agent.notify(self, "Часові інтервали оновлені")