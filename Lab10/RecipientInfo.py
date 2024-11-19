from Agent import Agent

class RecipientInfo:
    def __init__(self, Agent: Agent):
        self.Agent = Agent
        self.is_different_person = False
        self.recipient_name = ""
        self.recipient_phone = ""

    def set_different_person(self, is_different):
        self.is_different_person = is_different
        self.Agent.notify(self, "Набір іншої людини")

    def update_required_fields(self):
        pass