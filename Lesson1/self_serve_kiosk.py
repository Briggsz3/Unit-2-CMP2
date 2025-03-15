class Kiosk:

    def __init__(self) -> None:
        """defines some of the variables in use

        Args:
            number_items (int): _description_
            total_price (float): _description_
            purchase_list (dict): _description_
        """
        self.number_items = 0
        self.total_price = 0
        self.purchase_list = {}

    def add_item(self):
        """takes input of item and item price and plugs it into a dictionary

        Args:
            item_name (str): name of item
            item_price (float): price of item
            purchase_list (dict): dictionary list containing the item names and item prices
        """
        while True:
            item_name = input("Please enter your item, if you do not have any more items to scan enter '1': ")
            if item_name == '1':
                break
            else:
                item_price = float(input("What is the price of your item: "))
                self.purchase_list[item_name] = item_price
                print(self.purchase_list)
                # maybe try creating a dictionary with the items and prices and then printing them out.
        pass
    
    def get_total(self):
        """ gets the total value of all items purchased

        Args:
            purchase_list (dict): dictionary containing the users purchases and their costs
            total_price (int): adds together all the values on the dictionary
        """
        self.total_price = sum(self.purchase_list.values())
        print(f"You owe {self.total_price}")
        self.total_price = round(self.total_price,2)
        
        
    def take_payment(self, total_price):
        """asks the user how much they are paying, subtracts it from the total price
        then runs it through a function to check that they payed enough
        """
        while True:
            pay= float(input("How much do you want to pay: "))
            self.total_price = self.total_price - pay
            self.total_price = round(self.total_price,2)
            print(self.total_price)
            if self.total_price > 0:
                print(" ")
                print(f"You still owe {self.total_price}")
                continue
            else:
                break
        pass
        
        # if the getTotal - takePayemnt > 0 then say you have to pay more
        # Could use a while loops
        
    def give_change(self):
        """takes the amount that you paid and the amount you owed and checks
        to see how much to give back
        """
        if self.total_price == 0:
            print("Have a great day")
        else:
            self.total_price = self.total_price*-1
            self.total_price = round(self.total_price,2)
            print(f"You're change is ${self.total_price}")
            print("Have a great day")
        pass
    def finalize_transaction(self):
        """prints out the change and pay function
        """
        while True: 
            finalize = int(input("Would you like to finalize the transaction 1) yes, 2) no: "))
            if finalize == 1:
                dictionary_len = len(self.purchase_list)
                print(f"You bought {dictionary_len} items today")
                self.get_total()
                self.take_payment(self.total_price)
                self.give_change()
                break
            else: 
                self.add_item()
                continue
        pass
def main():
    Kiosk1=Kiosk()
    Kiosk1.add_item()
    Kiosk1.finalize_transaction()
        
    

if __name__ == "__main__":
    main()
# How do you get to print out the main for testing and finality purposes.
# create a dictionary when the person adds the price and item
# sum of dictionary for the total price
