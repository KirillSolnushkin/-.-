from DatePick import DatePick
from TimePick import TimePick
from RecipientInfo import RecipientInfo
from PickOption import PickOption
from DelAgent import DelAgent

def main():
    Agent = DelAgent(
        date_pick=DatePick(None),
        time_pick=TimePick(None),
        recipient_info=RecipientInfo(None),
        pick_option=PickOption(None)
    )

    date_pick = Agent.date_pick
    time_pick = Agent.time_pick
    recipient_info = Agent.recipient_info
    pick_option = Agent.pick_option

    date_pick.Agent = Agent
    time_pick.Agent = Agent
    recipient_info.Agent = Agent
    pick_option.Agent = Agent

    date_pick.select_date("2002-11-25")
    recipient_info.set_different_person(True)
    pick_option.set_pick(True)

if __name__ == "__main__":
    main()
