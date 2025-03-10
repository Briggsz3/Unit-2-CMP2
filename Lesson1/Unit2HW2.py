class restaurant:
    """an attempt to create a restaurant"""

    def __init__(self, restaurant_name: str, cuisine_type: str, number_served: int) -> None:
        """creates a restaurant name and describes the cuisine type

        Args:
            restaurant_name (str): Name of restaurant
            cuisine_type (str): Style of cuisine
            number_served (int): number of customers served in a day
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def set_number_served(self):
      print(f"We have served {self.number_served} people today")

    #def increment_number_served(self):
      #self.number_served+=number_served
      
    def describe_restaurant(self) -> None:
        """Describes the restaurant, name and cuisine type"""
        print(f"The restaurants name is {self.restaurant_name} ")
        print(f"The restaurants cuisine is {self.cuisine_type}.")

    def open_restaurant(self) -> None:
        """Defines when the restaurant is open"""
        print(f"{self.restaurant_name} is open.")

def main():
    restaurant1 = restaurant("Velucci's","Italian", 50)
    
    restaurant1.describe_restaurant()
    restaurant1.open_restaurant()
    print(" ")

# self.number_served+= number_served
