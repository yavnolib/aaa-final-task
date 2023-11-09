"""
    Examples of usage:
    $ python cli.py order pepperoni --delivery
    $ python cli.py menu
"""

import click

from .delivery import Delivery
from .receipts import pizzas


@click.group()
def cli():
    pass


@cli.command()
@click.option("--delivery", default=False, is_flag=True)
@click.argument("pizza", nargs=1)
def order(pizza: str, delivery: bool):
    """
    Cook and delivery (if necessary) pizza
    """
    if pizza.lower() in map(str.lower, pizzas):
        pizzas[pizza.capitalize()]().cook()

    if delivery:
        Delivery().courier(pizza=pizza)


@cli.command()
def menu():
    """
    Print menu
    """
    for ind, (key, value) in enumerate(pizzas.items()):
        click.echo(
            click.style(
                f"{ind + 1}.) Pizza {key}: {', '.join(value().receipt)}",
                bg="blue",
            )
        )


__all__ = ["cli"]

if __name__ == "__main__":
    cli()
