from DelStr import DelStr

class InternalDelStr(DelStr):
    def calculate_cost(self, distance: float, weight: float) -> float:
        return distance * 1.29 + weight * 0.4