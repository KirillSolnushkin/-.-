from Agent import Agent

class DatePick:
    def __init__(self, Agent: Agent):
        self.Agent = Agent
        self.selected_date = None

    def select_date(self, date):
        self.selected_date = date
        self.Agent.notify(self, "Вибрані дані")