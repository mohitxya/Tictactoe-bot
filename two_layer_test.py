from board import Board
from player import Player
from game import Game
from random_bot import RandomBot
from two_layer_bot import TwoLayerBot

def main():
    xbot=RandomBot(Player.x)
    obot=TwoLayerBot(Player.o)

    game=Game(1000)
    print("Random (x) vs twolayerbot (o)")
    game.simulate(xbot, obot)

    xbot=TwoLayerBot(Player.x)
    obot=RandomBot(Player.o)
    game=Game(1000)
    print("Twolayer (x) vs randombot(o)")
    game.simulate(xbot, obot)


    xbot=TwoLayerBot(Player.x)
    obot=TwoLayerBot(Player.o)
    game=Game(1000)
    game.simulate(xbot, obot)

if __name__=="__main__":
    main()

