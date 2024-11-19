from Agent import Agent

class DelAgent(Agent):
    def __init__(self, date_pick, time_pick, recipient_info, pick_option):
        self.date_pick = date_pick
        self.time_pick = time_pick
        self.recipient_info = recipient_info
        self.pick_option = pick_option

    def notify(self, sender, event):
        if event == "Вибрані дані":
            self.time_pick.update_time_slots(self.date_pick.selected_date)
        elif event == "Налаштування іншої людини":
            self.recipient_info.update_required_fields()
        elif event == "Підібрати налаштування":
            if self.pick_option.is_pick:
                self.disable_del_options()
            else:
                self.enable_del_options()

    def disable_del_options(self):
        pass

    def enable_del_options(self):
        pass