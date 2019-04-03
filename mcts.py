from gameboard import *

class Node:
	def __init__(self, move=None, parent=None, state=None):
		self.move = move
		self.parent = parent
		self.childNodes = []
		self.wins = 0
		self.visits = 0
		self.untriedMoves = getMoves()

	def uct_select_child(self):
        """ Use the UCB1 formula to select a child node. Often a constant UCTK is applied so we have
            lambda c: c.wins/c.visits + UCTK * sqrt(2*log(self.visits)/c.visits to vary the amount of
            exploration versus exploitation.
        """
        s = sorted(self.child_nodes, key=lambda c: c.wins / c.visits + np.sqrt(2 * np.log(self.visits) / c.visits))[-1]
        return s

    def add_child(self, m, s):
        """ Remove m from untriedMoves and add a new child node for this move.
            Return the added child node
        """
        n = Node(move=m, parent=self, state=s)
        self.untried_moves.remove(m)
        self.child_nodes.append(n)
        return n

    def update(self, result):
        """ Update this node - one additional visit and result additional wins.
        result must be from the viewpoint of playerJustmoved.
        """
        self.visits += 1
        self.wins += result

    def __repr__(self):
        return "[M:" + str(self.move) + " W/V:" + str(self.wins) + "/" + str(self.visits) + " U:" + str(
            self.untried_moves) + "]"