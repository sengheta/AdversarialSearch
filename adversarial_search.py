############################################################
# CIS 521: adversarial_search
############################################################

student_name = "Sarah Engheta"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.

import collections
import copy
import itertools
import random
import math


############################################################
# Section 1: Dominoes Game
############################################################

def create_dominoes_game(rows, cols):
    res = [[False for i in range(cols)] for x in range(rows)]
    return DominoesGame(res)


class DominoesGame(object):

    # Required
    def __init__(self, board):
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])

    def get_board(self):
        return self.board

    def reset(self):
        self.board = [[False for i in range(self.cols)] for x in range(self.rows)]

    def is_legal_move(self, row, col, vertical):
        if vertical:
            if row + 1 <= self.rows - 1 and col >= 0 and row >= 0 and col <= self.cols - 1 and not self.board[row][
                col] and not self.board[row + 1][col]:
                return True
            else:
                return False
        else:
            if col + 1 <= self.cols - 1 and col >= 0 and row >= 0 and row <= self.rows - 1 and not self.board[row][
                col] and not self.board[row][col + 1]:
                return True
            else:
                return False

    def legal_moves(self, vertical):
        for x in range(self.rows):
            for y in range(self.cols):
                if self.is_legal_move(x, y, vertical):
                    yield x, y

    def perform_move(self, row, col, vertical):
        if not self.is_legal_move(row, col, vertical):
            return
        else:
            if vertical:
                self.board[row][col] = True
                self.board[row + 1][col] = True
            else:
                self.board[row][col] = True
                self.board[row][col + 1] = True

    def game_over(self, vertical):
        if any(self.legal_moves(vertical)):
            return False
        else:
            return True

    def copy(self):
        res = copy.deepcopy(self.board)
        return DominoesGame(res)

    def successors(self, vertical):
        for x in range(self.rows):
            for y in range(self.cols):
                if (x, y) in self.legal_moves(vertical):
                    res = self.copy()
                    res.perform_move(x, y, vertical)
                    yield (x, y), res

    def get_random_move(self, vertical):
        pass

    def get_board_value(self, vertical):
        player_moves_count = len(list(self.legal_moves(vertical)))
        opponent_moves_count = len(list(self.legal_moves(not vertical)))
        return player_moves_count - opponent_moves_count

    # Required
    def get_best_move(self, vertical, limit):
        return self.max_value(vertical, vertical, limit, float("-inf"), float("inf"))

    def max_value(self, max_is_vertical, move_is_vertical, limit, alpha, beta):
        if self.game_over(move_is_vertical) or limit == 0:
            return None, self.get_board_value(max_is_vertical), 1
        best_move = 0, 0
        best_value = float("-inf")
        total_leaves = 0
        for move, res in self.successors(move_is_vertical):
            new_move, new_value, new_leaves = res.min_value(max_is_vertical, not move_is_vertical, limit - 1, alpha,
                                                            beta)
            total_leaves += new_leaves

            if new_value > best_value:
                best_value = new_value
                best_move = move

            if best_value >= beta:
                break

            alpha = max(alpha, best_value)
        return best_move, best_value, total_leaves

    def min_value(self, max_is_vertical, move_is_not_vertical, limit, alpha, beta):
        if self.game_over(move_is_not_vertical) or limit == 0:
            return None, self.get_board_value(max_is_vertical), 1
        best_move = 0, 0
        best_value = float("inf")
        total_leaves = 0
        for move, res in self.successors(move_is_not_vertical):
            new_move, new_value, new_leaves = res.max_value(max_is_vertical, not move_is_not_vertical, limit-1, alpha,
                                                            beta)
            total_leaves += new_leaves

            if new_value < best_value:
                best_value = new_value
                best_move = move

            if best_value <= alpha:
                break

            beta = min(beta, best_value)
        return best_move, best_value, total_leaves


def main():
    b = [[False] * 3 for i in range(4)]
    g = DominoesGame(b)
    print(g.get_best_move(True, 3))



if __name__ == "__main__":
    main()
############################################################
# Section 2: Feedback
############################################################

feedback_question_1 = 9


feedback_question_2 = """
I found it challenging to trace through the recursive nature of the functions - I was struggling a bit with the logic
"""

feedback_question_3 = """
Honestly the aspect that I liked most was how helpful the TAs were during the homework recitation. Sherry walked through 
the logic so clearly and concisely. I would love to see more examples and walk throughs like this before all homeworks!
"""
