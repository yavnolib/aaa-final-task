"""
    There are tests for receipts.py
"""

from src.receipts import Hawaiian, Margherita, Pepperoni, Pizza


def test_pizza():
    """
    Test Pizza class
    """
    p = Pizza()
    assert str(p) == "Pizza (35 cm)"
    assert p.dict() == {"Pizza (35 cm)": None}


def test_margherita():
    """
    Test Margherita class
    """
    assert str(Margherita("L")) == "Margherita (30 cm)"
    assert list(Margherita("L").dict().keys()) == ["Margherita (30 cm)"]
    assert len(list(Margherita().dict().values())[0]) == 3


def test_cooktime():
    """
    Test cooking time
    """
    assert isinstance(Hawaiian().cook(), str)


def test_eq_pizza():
    """
    Test equal operation between Pizza's classes
    """
    assert Pepperoni("M") == Hawaiian("M")
    assert Hawaiian("M") == 25
