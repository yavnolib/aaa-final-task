from utils import log


class Class:
    """
    Some class for decoration
    """

    @log()
    def foo(self):
        """
        Some class method for decoration
        """
        pass


@log()
def foo():
    """
    Some func for decoration
    """
    pass


def test_class():
    assert "Delivered for" in Class().foo()


def test_foo():
    assert "Delivered for" in foo()
