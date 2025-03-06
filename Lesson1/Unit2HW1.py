'''
Name: Zachary Briggs
Date: 3/6/25
Assignment: Restaurant
'''

class restaurant:
    """A simple attempt to model a dog."""

    def __init__(self, restaurant_name: str, cuisine_type: str) -> None:
        """Creates a new dog object

        Args:
            name (str): Name of dog
            age (int): Age of dog
        """
        self.name = name
        self.age = age

    def sit(self) -> None:
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self) -> None:
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")