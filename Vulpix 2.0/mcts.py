######################################################
##                 Project Vulpix                   ##
##                Senior Project 2                  ##
##                 Andrew Siddall                   ##
##                 Chris Crisson                    ##
##               Matthew Bedillion                  ##
##               Adlene Bellaoucha                  ##
##               January 31, 2019                   ##
######################################################

import copy
import random
import math
debug = False

class Node:
    def __init__(self, move=None, parent=None, state=None, moveName=''):
        self.move = move
        self.moveName = moveName
        self.parent = parent
        self.childNodes = []
        self.wins = 0
        self.visits = 1
        #print(state.turn)

        self.untriedMoves = state.getMoves(state.turn)

    def uctSelectChild(self):
        """ Use the UCB1 formula to select a child node. Often a constant UCTK is applied so we have
            lambda c: c.wins/c.visits + UCTK * sqrt(2*log(self.visits)/c.visits to vary the amount of
            exploration versus exploitation.
        """
        s = sorted(self.childNodes, key=lambda c: c.wins / c.visits + math.sqrt(2 * math.log(self.visits) / c.visits))[-1]
        return s

    def addChild(self, m, s):
        """ Remove m from untriedMoves and add a new child node for this move.
            Return the added child node
        """

        ## Saves the move name
        name = ''
        if str(m[0]).find("playItem") != -1:
            if len(m) > 2:
                if m[1] == 'p':
                    name = s.playerHand[m[2]].Name
                elif m[1] == 'o':
                    name = s.oppHand[m[2]].Name
        elif str(m[0]).find("playSupporter") != -1:
            if len(m) > 2:
                if m[1] == 'p':
                    name = s.playerHand[m[2]].Name
                elif m[1] == 'o':
                    name = s.oppHand[m[2]].Name
        elif str(m[0]).find("playEnergy") != -1:
            if len(m) > 2:
                if m[2] == 'p':
                    name = s.playerHand[m[1]].Name
                elif m[2] == 'o':
                    name = s.oppHand[m[2]].Name
                    #print("addchild: " +name)
        n = Node(move=m, parent=self, state=s, moveName=name)
        #print("in addchild m =" + str(m))
        self.untriedMoves.remove(m)
        #print(str(self.untriedMoves))
        # self.untriedMoves = (s.getMoves(s.turn))
        # try:
        #     self.untriedMoves.remove(m)
        # except Exception as e:
        #     pass
        self.childNodes.append(n)
        return n

    def update(self, result):
        """ Update this node - one additional visit and result additional wins.
        result must be from the viewpoint of playerJustmoved.
        """
        #print("updating node result = " + str(result))
        self.visits += 1
        self.wins += result

    def __repr__(self):
        return "[M: " + str(self.move) + " W/V: " + str(self.wins) + "/" + str(self.visits) + " U: " + str(
            self.untriedMoves) + "]"

def uct(rootstate, itermax):
    """ Conduct a UCT search for itermax iterations starting from rootstate.
    Return the best move from the rootstate.
    Assumes 2 alternating players (player 1 starts), with game results in the range [0.0, 1.0]."""
    print("Creating new state...")
    #state = copy.deepcopy(rootstate)  ## Added to test if this fixes issues with mcts affecting gamestate
    #rootnode = Node(state=state)   ## Added to test if this fixes issues with mcts affecting gamestate
    rootnode = Node(state=rootstate)
##    x = copy.deepcopy(rootstate)       #Removed for test
    
    print("Starting MCTS...")
    for i in range(itermax):
        if debug:
            print("i = " + str(i))
        node = rootnode
        print("Creating new state...")
        state = copy.deepcopy(rootstate)
        
    
        #Select
        
        while node.untriedMoves == [] and node.childNodes != []:
            print("Starting Selection...")
            node = node.uctSelectChild()
            state.makeMove(node.move)       #Added for test
        print("Exiting Selection...")
        
        #Expand
        
        if node.untriedMoves != [] :      #added and node.parent == None condition
            print("Starting Expansion..")
            m = random.choice(node.untriedMoves)
            state.makeMove(m)
            #print("adding child")
            #print(node.untriedMoves)
            node = node.addChild(m, state)
            #print(node.untriedMoves)
        print("Exiting Expansion..")

        #Rollout
        
        while node.untriedMoves != [] and node.parent == None:
            print("Starting Rollout...")
            state.makeMove(random.choice(state.getMoves(state.turn)))
##        while not state.getMoves(state.turn) == []:  # while state is non-terminal
##            state.makeMove(random.choice(state.getMoves(state.turn)))
        print("Exiting Rollout...")

        #Backpropegate
        
        while node.parent is not None:
            print("Starting Backpropeagtion...")
            node.update(state.checkWinCon(state.turn))
            node = node.parent
        #print("returning move")
        print("Exiting Backpropeagtion...")

    #print("length of rootnode.childNodes " + str(len(rootnode.childNodes)))
    x = sorted(rootnode.childNodes, key=lambda c: c.visits)[-1]
    #print(x.moveName)
    print("Exiting MCTS...")
    return x.move, x.moveName
