from Agent import Agent

class OrderPage:
    def __init__(self, Agent: Agent):
        self.Agent = Agent
        self.date_pick = None
        self.time_pick = None
        self.recipient_info = None
        self.pick_option = None

    def set_date_pick(self, date_pick):
        self.date_pick = date_pick

    def set_time_pick(self, time_pick):
        self.time_pick = time_pick

    def set_recipient_info(self, recipient_info):
        self.recipient_info = recipient_info

    def set_pick_option(self, pick_option):
        self.pick_option = pick_option

    def update_del_options(self):
        self.Agent.notify(self, "Оновити параметри доставки")