#from gameboard import *
#import GameLoop
import copy
import random

class Node:
    def __init__(self, move=None, parent=None, state=None):
        self.move = move
        self.parent = parent
        self.childNodes = []
        self.wins = 0
        self.visits = 0
        #print(state.turn)

        self.untriedMoves = state.getMoves(state.turn)

    def uctSelectChild(self):
        """ Use the UCB1 formula to select a child node. Often a constant UCTK is applied so we have
            lambda c: c.wins/c.visits + UCTK * sqrt(2*log(self.visits)/c.visits to vary the amount of
            exploration versus exploitation.
        """
        s = sorted(self.childNodes, key=lambda c: c.wins / c.visits + np.sqrt(2 * np.log(self.visits) / c.visits))[-1]
        return s

    def addChild(self, m, s):
        """ Remove m from untriedMoves and add a new child node for this move.
            Return the added child node
        """
        n = Node(move=m, parent=self, state=s)
        self.untriedMoves = (s.getMoves(s.turn))
        try:
            self.untriedMoves.remove(m)
        except Exception as e:
            pass
        
        
        self.childNodes.append(n)
        return n

    def update(self, result):
        """ Update this node - one additional visit and result additional wins.
        result must be from the viewpoint of playerJustmoved.
        """
        print("updating node result = " + str(result))
        self.visits += 1
        self.wins += result

    def __repr__(self):
        return "[M:" + str(self.move) + " W/V:" + str(self.wins) + "/" + str(self.visits) + " U:" + str(
            self.untried_moves) + "]"

def uct(rootstate, itermax):
    rootnode = Node(state=rootstate)

    for i in range(itermax):
        node = rootnode
        state = copy.deepcopy(rootstate)
        #print(str(node.untriedMoves))
    
        #Select
        while node.untriedMoves == [] and node.childNodes != []:
            node = node.uctSelectChild()
            node.move[0](node.move[1:])
        
        #Expand
        if node.untriedMoves != [] and node.parent == None:
            m = random.choice(node.untriedMoves)
            state.makeMove(m)
            print("adding child")
            node = node.addChild(m, state)
            print(node.untriedMoves)

        #Rollout
        while not state.getMoves(state.turn) == []:
            state.makeMove(random.choice(state.getMoves(state.turn)))

        #Backpropegate
        while node is not None:
            node.update(state.checkWinCon(state.turn))
            node = node.parent
        print("returning move")
        print("length of rootnode.childNodes " + str(len(rootnode.childNodes)))
        return sorted(rootnode.childNodes, key=lambda c: c.visits)[-1].move