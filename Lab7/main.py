from DelContext import DelContext
from PickupStr import PickupStr
from ExternalDelStr import ExternalDelStr
from InternalDelStr import InternalDelStr

def main():
    context = DelContext()

    context.set_delivery_method(PickupStr())
    print("Самовивіз:", context.calculate_delivery_cost(10, 5))

    context.set_delivery_method(ExternalDelStr())
    print("Доставка зовнішньою службою доставки:", context.calculate_delivery_cost(10, 5))

    context.set_delivery_method(InternalDelStr())
    print("Доставка власною службою доставки:", context.calculate_delivery_cost(10, 5))

if __name__ == "__main__":
    main()