"""Short definition of my module.

This module provides:
- add: a function to add two numbers.
"""

from myproject import __version__


def foo():
    print("hallo")


def foo4():
    menu_1 = {"1": "Start Game", "2": "Load Game", "3": "Options", "4": "Exit"}

    # fmt: off
    menu_2 = {
      "1": "Start Game",
      "2": "Load Game",
      "3": "Options",
      "4": "Exit"
  }
    # fmt: on

    return menu_1, menu_2


def foo3(a):
    b = 0  # noqa: F841
    c = a + 1
    if a > 0:  # noqa: SIM102
        if a > 10:
            return 10
    return a + c


def add(a: int, b: int) -> int:
    """Adds two positive numbers together.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        sum: The sum of the two numbers.

    Raises:
        ValueError: If either a or b is negative.
    """
    if a < 0 or b < 0:
        msg = "Both arguments must be positive"
        raise ValueError(msg)
    return a + b


def main() -> None:
    print(f"Running myproject version {__version__}")
    print(f"Result is: 1+2 = {add(1, 2)}")


if __name__ == "__main__":
    main()
