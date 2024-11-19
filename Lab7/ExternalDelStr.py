from DelStr import DelStr

class ExternalDelStr(DelStr):
    def calculate_cost(self, distance: float, weight: float) -> float:
        return distance * 1.67 + weight * 0.5