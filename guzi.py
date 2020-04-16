import sys
import getopt
import numpy
import math

def quotient_from_earn(earn):
    #return 65 * numpy.log((earn + 1200000)/1200000) + 60
    return math.pow(earn, 1/3)

def usage():
    return """
    guzi.py -b <base_earned> -d <days> [-s <spend_percent>]
    guzi.py --play
    """

class Player:

    def __init__(self, name, Q=1.0):
        self.name = name
        self.Q = Q
        self.A = 0
        self.G = int(pow(self.Q, 1/3))
        self.GA = int(pow(self.Q, 1/3))

    def spend_guzi(self, amount):
        print("{} spends {} Guzis".format(self.name, amount))
        if self.G < amount:
            raise ValueError('Amount is greater than Guzi counter.')
        self.G -= amount

    def receive_guzi(self, amount):
        print("{} receives {} Guzis".format(self.name, amount))
        self.Q += amount

    def spend_guza(self, amount):
        print("{} spends {} Guzas".format(self.name, amount))
        if self.GA < amount:
            raise ValueError('Amount is greater than Guza counter.')
        self.A -= amount
        self.GA -= amount

    def receive_guza(self, amount):
        print("{} receives {} Guzas".format(self.name, amount))
        self.A += amount

    def new_day(self):
        if self.A > 0:
            self.Q += self.A
            self.A = 0
        self.G += int(pow(self.Q, 1/3))
        self.GA += int(pow(self.Q, 1/3))

    def to_string(self):
        return "{} (Q={}, A={}, G={}, GA={})".format(self.name, self.Q, self.A, self.G, self.GA)


def play():
    players = {}
    user_input = input("Player, quotient (E1, 1):")
    while user_input.lower() != "e" and user_input.lower() != "end":
        if len(user_input) == 0:
            player = Player("E" + str(len(players) + 1))
        else:
            p, q = user_input.split(",")
            player = Player(p.strip(), float(q.strip()))
        players[player.name] = player
        user_input = input("Player, quotient (E{}, 1):".format(len(players) + 1))
    print_states(players)

    #ACTIONS
    name_list = [p.name for p in players.values()]
    user_input = input("Action <{}> <{}> <amount> <g|ga>".format(name_list, name_list))
    while user_input.lower() != "e" and user_input.lower() != "end":
        if user_input == "newday" or user_input == "n":
            for p in players.values():
                p.new_day()
            print_states(players)
        else:
            try:
                source, target, amount, unit = user_input.split(" ")
            except ValueError:
                print("invalid input")
            else:
                print(source, target, amount, unit)
                amount = int(amount)
                if unit.lower() == "g":
                    players[source].spend_guzi(amount)
                    players[target].receive_guzi(amount)
                elif unit.lower() == "ga":
                    players[source].spend_guza(amount)
                    players[target].receive_guza(amount)
                print_states(players)
        user_input = input("Action <{}> <{}> <amount> <g|ga>".format(name_list, name_list))


def print_states(players):
    for p in players.values():
        print(p.to_string())

if __name__ == "__main__":

    try:
        opts, args = getopt.getopt(sys.argv[1:],"hpb:d:s:",["play", "base_earned=","days=","spend_percent="])
    except getopt.GetoptError:
        print(usage())
        sys.exit(2)

    base_earned = 0
    days = 0
    spend_percent = 0

    for opt, arg in opts:
        if opt == '-h':
            print(usage())
            sys.exit()
        elif opt in ("-b", "--base_earned"):
            base_earned = int(arg)
        elif opt in ("-d", "--days"):
            days = int(arg)
        elif opt in ("-s", "--spend_percent"):
            spend_percent = float(arg)
        elif opt in ("-p", "--play"):
            play()
            sys.exit()

    quotient = quotient_from_earn(base_earned)
    total_earned = base_earned

    for d in range(days):
        total_earned += quotient - quotient * spend_percent
        quotient = quotient_from_earn(total_earned)
    print("total earned = {:.2f}, quotient = {:.2f}".format(total_earned, quotient))
