'''
Name: Zachary Briggs
Date: 3/6/25
Assignment: Restaurant
'''

class user:
    """an attempt to create and describe a user"""

    def __init__(self, first_name: str, last_name: str, age: int, hair_color) -> None:
        """creates the users first and last name, age, hair color

        Args:
            first_name (str): first name of person
            last_name (str): last name of person
            age (int)
        """
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self) -> None:
        """Describes the restaurant, first name, last name and description"""
        print(f"This persons name is {self.first_name} {self.last_name}")

    def open_restaurant(self) -> None:
        """Defines when the restaurant is open"""
        print(f"{self.restaurant_name} is open.")

def main():
    restaurant1 = restaurant("Velucci's","Italian")
    restaurant2 = restaurant("Pine Hill","Brewery")
    restaurant3 = restaurant("The Soup Bar", "Soup")
    
    restaurant1.describe_restaurant()
    restaurant1.open_restaurant()
    print(" ")
    restaurant2.describe_restaurant()
    restaurant2.open_restaurant()
    print(" ")
    restaurant3.describe_restaurant()
    restaurant3.open_restaurant()
    
if __name__ == "__main__":
    main()

class restaurant:
    """an attempt to create a restaurant"""

    def __init__(self, restaurant_name: str, cuisine_type: str) -> None:
        """creates a restaurant name and describes the cuisine type

        Args:
            restaurant_name (str): Name of restaurant
            cuisine_type (int): Style of cuisine
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self) -> None:
        """Describes the restaurant, name and cuisine type"""
        print(f"The restaurants name is {self.restaurant_name} ")
        print(f"The restaurants cuisine is {self.cuisine_type}.")

    def open_restaurant(self) -> None:
        """Defines when the restaurant is open"""
        print(f"{self.restaurant_name} is open.")

def main():
    restaurant1 = restaurant("Velucci's","Italian")
    restaurant2 = restaurant("Pine Hill","Brewery")
    restaurant3 = restaurant("The Soup Bar", "Soup")
    
    restaurant1.describe_restaurant()
    restaurant1.open_restaurant()
    print(" ")
    restaurant2.describe_restaurant()
    restaurant2.open_restaurant()
    print(" ")
    restaurant3.describe_restaurant()
    restaurant3.open_restaurant()
