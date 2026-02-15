from config import MENU, resources

class Machine:

    def __init__(self, resources):
        self.resources = resources
        self.money = 0.0
        self.isOn = False

    def collect_coins(self, cost):
        print(f"Please insert coins. The cost of this coffee is ${cost}.")
        pennies = int(input("How many pennies: "))
        nickels = int(input("How many nickels: "))
        dimes = int(input("How many dimes: "))
        quarters = int(input("How many quarters: "))

        return pennies * 0.01 + nickels * 0.05 + dimes * 0.1 + quarters * 0.25

    def buy_coffee(self, coffee):

        demands = MENU[coffee]['ingredients']
        if demands.get('water', 0) > self.resources['water']:
            print("Sorry there is not enough water.")
            return
        elif demands.get('milk', 0) > self.resources['milk']:
            print("Sorry there is not enough milk.")
            return
        elif demands.get('coffee', 0) > self.resources['coffee']:
            print("Sorry there is not enough coffee.")
            return

        cost = MENU[coffee]['cost']
        coins = self.collect_coins(cost)

        if cost > coins:
            print("Sorry that's not enough money. Money refunded.")
            return

        self.money += cost
        self.resources['water'] -= demands.get('water', 0)
        self.resources['milk'] -= demands.get('milk', 0)
        self.resources['coffee'] -= demands.get('coffe', 0)
        print(f"Here is your {coffee}. Enjoy!!!")

        if cost < coins:
            print(f"Here is your ${coins - cost} in change.")

    def run(self):
        self.isOn = True
        print("Coffee machine started!")
        while self.isOn:

            command = input("What would you like?(espresso/latte/cappuccino)\n").lower()
            if "turn off" in command:
                self.isOn = False

            elif "report" in command:
                print(f"Current resources:\n"
                      f"Water - {self.resources['water']}ml\n"
                      f"Milk - {self.resources['milk']}ml\n"
                      f"Coffee - {self.resources['coffee']}g\n"
                      f"Money - ${self.money}")

            elif command in MENU:
                self.buy_coffee(command)

            else:
                print("Command not understood. Please try again.\n"
                      "The available commands are: report, off, and any of the following coffees:")
                print(list(MENU.keys()))



machine = Machine(resources)

machine.run()