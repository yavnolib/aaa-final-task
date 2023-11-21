from .utils import log


class Delivery:
    """
    Class for couriers
    """

    @log()
    def courier(self, pizza="Pizza"):
        print(f"courier - (-_-) Courier is waiting for {pizza}")
