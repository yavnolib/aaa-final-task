"""
    1. Опишите рецепты классами ✅
    2. Пусть будет два размера: L и XL ✅
    3. метод dict() выводит рецепт в виде
       словаря ✅
"""
import math

from .utils import log


class Pizza:
    """
    Pizza's class

    cook() ✅

    receipt ✅
    del_from_receipt()✅
    add_to_receipt()✅

    __str__() -> print receipt and class_name ✅
    __eq__() -> if size is equal ✅
    __sub__() -> area difference  ✅
    area

    """

    radius_dict = {"XL": 35, "L": 30, "M": 25}

    def __init__(self, psize="XL"):
        self.receipt = None
        self.radius = (
            self.radius_dict[psize]
            if psize in self.radius_dict
            else self.radius_dict["XL"]
        )
        self.area = math.pi * self.radius**2

    def __str__(self):
        return self.__class__.__name__ + f" ({self.radius} cm)"

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, int):
            return self.radius == __value
        if isinstance(__value, Pizza):
            return self.radius == __value.radius
        return False

    def __sub__(self, other):
        return self.area - other.area

    @log(template="✅ Pizza cooked in {} s.")
    def cook(self):
        """
        Function to cook pizza
        """
        print("cook - (-_-) cooking")

    def add_to_receipt(self, val):
        """
        Add ingredient to receipt
        """
        if self.receipt is None:
            self.receipt = [val]
        elif val not in self.receipt:
            self.receipt.append(val)

    def del_from_receipt(self, val):
        """
        Delete ingredient from receipt
        """
        if self.receipt is None:
            return
        if val in self.receipt:
            self.receipt.remove(val)

    def dict(self):
        """
        Represent class as dictionary
        """
        return {str(self): self.receipt}


class Margherita(Pizza):
    """
    -tomato sauce
    -mozzarella
    -tomatoess
    """

    def __init__(self, psize="XL"):
        super().__init__(psize)
        self.receipt = ["tomato sauce", "mozzarella", "tomatoes"]


class Pepperoni(Pizza):
    """
    -tomato sauce
    -mozzarella
    -pepperoni
    """

    def __init__(self, psize="XL"):
        super().__init__(psize)
        self.receipt = ["tomato sauce", "mozzarella", "pepperoni"]


class Hawaiian(Pizza):
    """
    -tomato sauce
    -mozzarella
    -chicken
    -pineapples
    """

    def __init__(self, psize="XL"):
        super().__init__(psize)
        self.receipt = ["tomato sauce", "mozzarella", "chicken", "pineapples"]


pizzas = {
    "Hawaiian": Hawaiian,
    "Margherita": Margherita,
    "Pepperoni": Pepperoni,
}

__all__ = ["Pizza", "Hawaiian", "Margherita", "Pepperoni", "pizzas"]

if __name__ == "__main__":
    print(__all__)
    print(Hawaiian().cook())
