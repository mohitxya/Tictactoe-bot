from player import Player
from game import Game
from random_bot import RandomBot

def main():
    xbot= RandomBot(Player.x)
    obot= RandomBot(Player.o)

    game=Game(1000)
    game.simulate(xbot, obot)

if __name__=="__main__":
    main()
