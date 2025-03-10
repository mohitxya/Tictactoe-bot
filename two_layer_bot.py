import random
import copy


class TwoLayerBot():
    def __init__(self, player):
        self.player=player
    def select_move(self, board):
        losing_move=None
        first_candidates=board.get_legal_moves()
        for i in range(len(first_candidates)):

            row = first_candidates[i][0]
            col=first_candidates[i][1]

            newboard=copy.deepcopy(board)

            newboard.make_move(row, col, self.player)

            if (newboard.has_winner()==self.player):
                return [row, col]

            second_candidates = newboard.get_legal_moves()

            for j in range(len(second_candidates)):
                r=second_candidates[j][0]
                c=second_candidates[j][1]
                nb=copy.deepcopy(newboard)

                nb.make_move(r, c, self.player.other)

                if(nb.has_winner()==self.player.other):
                    losing_move=[r,c]

        if(losing_move!=None):
            return losing_move

        return random.choice(first_candidates)
