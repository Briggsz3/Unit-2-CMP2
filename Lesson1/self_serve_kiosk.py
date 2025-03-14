class Kiosk:

    def __init__(self, number_items: int, total_price: float, purchase_list: dict) -> None:
        """_summary_

        Args:
            number_items (int): _description_
            total_price (float): _description_
            purchase_list (dict): _description_
        """
        self.number_items = number_items
        self.total_price = total_price
        self.purchase_list = purchase_list
`   purchase_list = {}
    def add_item(self,item_name,item_price, purchase_list):
        """_summary_

        Args:
            item_name (str): name of item
            item_price (float): price of item
            purchase_list (dict): dictionary list containing the item names and item prices
        """
        while True:
            item_name = input("Please enter your item, if you do not have any more items to scan enter 'none':")
            if item_name != "none":
                item_price = float(input("What is the price of your item: "))
                self.purchase_list[item_name] = item_price
                print(purchase_list)
                # maybe try creating a dictionary with the items and prices and then printing them out.
            else:
                break
    def get_total(self,purchase_list, total_price: int):
        """ gets the total value of all items purchased

        Args:
            purchase_list (dict): dictionary containing the users purchases and their costs
            total_price (int): adds together all the values on the dictionary
        """
        total_price = sum(purchase_list.values())
        total_price = round(total_price,2)
        self.add_item()
    def take_payment(self,pay, total_price, remaining):
        """asks the user how much they are paying, subtracts it from the total price
        then runs it through a function to check that they payed enough
        """
        print(f"You owe ${total_price}")
        while True:
            pay= float(input("How much do you want to pay"))
            remaining = total_price - pay
            remaining = round(total_price,2)
            if remaining > 0:
                print(f"You still owe {remaining}")
                continue
            else:
                break
        
        # if the getTotal - takePayemnt > 0 then say you have to pay more
        # Could use a while loops
    def give_change(self, remaining):
        """takes the amount that you paid and the amount you owed and checks
        to see how much to give back.n
        """
        if remaining == 0:
            print("Have a great day")
        else:
            remaining = remaining*-1
            remaining = round(remaining,2)
            print(f"You're change is ${remaining}")
            print("Have a great day")
    def finalize_transaction(self, finalize, dictionary_len):
        """prints out the change and pay function
        """
        finalize = int(input("Would you like to finalize the transaction 1) yes, 2) no"))
        if finalize == 1:
            dictionary_len = len(purchase_list)
            print(f"You bought {dictionary_len} items today")
            get_total(self,purchase_list, total_price: int)
            take_payment(self,pay, total_price, remaining)
            give_change(self, remaining)
        else: 
            add_item(self,item_name,item_price, purchase_list)
    

# How do you get to print out the main for testing and finality purposes.
# create a dictionary when the person adds the price and item
# sum of dictionary for the total price
