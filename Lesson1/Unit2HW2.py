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

    def set_number_served(self,num_served:int):
      self.number_served = num_served

    def increment_number_served(self,number:int):
      self.number_served+=number
      
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
    restaurant1.set_number_served(200)
    print(restaurant1.number_served)
    restaurant1.increment_number_served(20)
    print(restaurant1.number_served)

if __name__ == "__main__":
    main()

# self.number_served+= number_served
################################
class user:
    """an attempt to create and describe a user"""

    def __init__(self, first_name: str, last_name: str, age: int, hair_color: str, login_attempts: int) -> None:
        """creates the users first and last name, age, hair color

        Args:
            first_name (str): first name of person
            last_name (str): last name of person
            age (int): age of the person
            hair_color (str): persons hair color
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hair_color = hair_color
        self.login_attempts = login_attempts
        
    def increment_login_attempts(self)->None:
        self.login_attempts+=1
        print(f"You have attempted to login {self.login_attempts} times")
    
    def reset_login_attempts(self)->None:
        self.login_attempts = 0
        print(f"Your login attempts have been reset to {self.login_attempts}")
    
    def describe_user(self) -> None:
        """Describes the restaurant, first name, last name and description"""
        print(f"This persons name is {self.first_name} {self.last_name}")
        print(f"They are {self.age} years old and have {self.hair_color} hair")

    def greeting1(self) -> None:
        """greets the customer"""
        print(f"Welcome {self.first_name}.")
    def greeting2(self) -> None:
        """greets the customer"""
        print(f"Good evening {self.first_name}.")
    def greeting3(self) -> None:
        """greets the customer"""
        print(f"Hello {self.first_name} welcome in")

def user_main():
    user1 = user("Tom", "Brady", 47, "brown",2)
    #user2 = user("Anne","Johnson", 34, "blonde")
    #user3 = user("Dwayne", "Roberts", 28, "black")
    
    user1.describe_user()
    user1.greeting1()
    user1.increment_login_attempts()
    user1.reset_login_attempts()
    print(" ")
    user2.describe_user()
    user2.greeting2()
    print(" ")
    user3.describe_user()
    user3.greeting3()

user_main()
