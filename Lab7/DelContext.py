from DelStr import DelStr

class DelContext:
    def __init__(self):
        self._strategy: DelContext = None

    def set_delivery_method(self, strategy: DelStr):
        self._strategy = strategy

    def calculate_delivery_cost(self, distance: float, weight: float) -> float:
        if not self._strategy:
            raise ValueError("Ńďîńłá äîńňŕâęč íĺ âńňŕíîâëĺíî")
        return self._strategy.calculate_cost(distance, weight)