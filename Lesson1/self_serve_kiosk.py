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

    def add_item(self,item_name,item_price, purchase_list):
        """_summary_

        Args:
            item_name (_type_): _description_
            item_price (_type_): _description_
            purchase_list (_type_): _description_
        """
        purchase_list = {}
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
        """_summary_

        Args:
            purchase_list (_type_): _description_
            total_price (int): _description_
        """
        total_price = sum(purchase_list.values())
        total_price = round(total_price,2)
        self.add_item()
    def take_payment(self,pay, total_price):
        """_summary_
        """
        print(f"You owe {total_price}")
        pay= float(input("How much do you want to pay"))
        total_price = total_price - pay
        total_price = round(total_price,2)
        
        # if the getTotal - takePayemnt > 0 then say you have to pay more
        # Could use a while loops
        pass
    def give_change():
        """_summary_
        """
        pass
    def finalize_transaction():
        """_summary_
        """
        pass
    

# How do you get to print out the main for testing and finality purposes.
# create a dictionary when the person adds the price and item
# sum of dictionary for the total price
