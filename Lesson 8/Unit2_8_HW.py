# 9-13 Dice

import random

class Die():
    def __init__(self, side_numbers: int, roll):
        self.side_numbers = side_numbers
        self.roll = roll
    
    def six_sided_die(self):
        for i in range(6): 
            self.roll = random.randint(1,6)
            print(self.roll)
    
    def ten_sided_die(self):
        print(" ")
        for j in range(10): 
            self.roll = random.randint(1,10)
            print(self.roll)

    def twenty_sided_die(self):
        print(" ")
        for n in range(10): 
            self.roll = random.randint(1,20)
            print(self.roll)
        
    def user_choice(self):
        print(" ")
        self.side_numbers = int(input("How many sides does the die have: "))
        print(" ")
        for m in range(self.side_numbers):
            self.roll = random.randint(1, self.side_numbers)
            print(self.roll)

def main():
    die1 = Die("15", " ")
    die1.six_sided_die()
    die1.ten_sided_die()
    die1.twenty_sided_die()
    die1.user_choice()

if __name__ == "__main__":
    main()

# 9-14 Lottery & 9-15 Lottery Analysis

class Lottery:

    def __init__(self, lottery_list, ticket_winner, my_ticket, random_value, ticket_number):
        self.lottery_list = lottery_list
        self.lottery_list = ['a', 'b', 'z', 'h', 's', 'v', 'u', 'r', 'm', 'i', '32', '15', '48', '47', '44']
        self.ticket_winner = ticket_winner
        self.ticket_winner = ['i', 's', 'a', '47', '15', 'b', '48', '44']
        self.my_ticket = my_ticket
        self.my_ticket = []
        self.random_value = random_value
        self.ticket_number = ticket_number
        
    def winning_ticket(self):
        print(f"Anyone with this ticket {self.ticket_winner} will win a prize") 
    
    def user_ticket(self):
        while True:
            for z in range (8):
                self.random_value = random.randint(0,14)
                self.my_ticket.append(self.lottery_list[self.random_value])
            if self.my_ticket == self.ticket_winner:
                print(" ")
                print("Congrats you've won the prize!")
                print(f"You had to have {self.ticket_number} tickets")
            else:
                self.ticket_number =+ 1
            



def main1():
    lottery1 = Lottery(" ", " ", " ", " ")
    lottery1.winning_ticket()
    lottery1.user_ticket()

if __name__ == "__main__":
    main1()



