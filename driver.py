#
#
#
# 
# 
# 
# 

import numpy as np

#Define goal state
goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

#define the edges
top_row = [0,1,2]
bottom_row = [6,7,8]
right_side = [2,5,8]
left_side = [0,3,6]


class Node:
    #CONSTRUCTOR FUNCTION
    def __init__(self, state, parent, action, depth, cost, total_path_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth
        self.cost = cost
        self.total_path_cost = total_path_cost

    
    #Generate New Nodes from Actions
    def generate_children(self):
        #create empty array to store next states
        next_states = []

        #find the 0 in the current state
        zero = self.state.index(0)

        ##Only generate children nodes for states that are reachable
        ##Geneterate using [‘Up’, ‘Down’, ‘Left’, ‘Right’]  order given

        #UP
        if(zero not in top_row):
            #Swap the value above zero with zero using a new state
            new_state = self.state.copy()
            temp = new_state[zero-3]
            new_state[zero-3] = 0
            new_state[zero] = temp
            #UP as a move is now a node that self can choose
            UP = Node(new_state, self, "up", self.depth + 1, 1, self.path_cost +1)
            next_states.append(UP)

        #DOWN
        if(zero not in bottom_row):
            #Swap the value below zero with zero using a new state
            new_state = self.state.copy()
            temp = new_state[zero+3]
            new_state[zero+3] = 0
            new_state[zero] = temp
            #DOWN as a move is now a node that self can choose
            DOWN = Node(new_state, self, "down", self.depth + 1, 1, self.path_cost +1)
            next_states.append(DOWN)

        #LEFT
        if(zero not in left_side):
            #Swap the value next to zero with zero using a new state
            new_state = self.state.copy()
            temp = new_state[zero-1]
            new_state[zero-1] = 0
            new_state[zero] = temp
            #LEFT as a move is now a node that self can choose
            LEFT = Node(new_state, self, "left", self.depth + 1, 1, self.path_cost +1)
            next_states.append(LEFT)

        #RIGHT
        if(zero not in right_side):
            #Swap the value next to zero with zero using a new state
            new_state = self.state.copy()
            temp = new_state[zero+1]
            new_state[zero+1] = 0
            new_state[zero] = temp
            #RIGHT as a move is now a node that self can choose
            RIGHT = Node(new_state, self, "right", self.depth + 1, 1, self.path_cost +1)
            next_states.append(RIGHT)

    def ManhattanDistance(self):
        total = 0
        for number in self.state:
            number_index = self.state.index(number)
            goal_state_index = goal_state.index(number)

    def solver(self, method, starting_state, goal_state):
        print("In SOLVER method", method)
        visited_nodes = [starting_state]
        #__init__(self, state, parent, action, depth, cost, total_path_cost)
        queue = [Node[starting_state, None, None, 0, 0, 0]]
        nodes_popped = 0
        max_queue = 0

        while(len(queue)>0):
            #Update queue information
            max_queue = max(len(queue), max_queue)
            current_node = queue.pop()
            nodes_popped +=1

            if current_node.state == goal_state:
                return "GOAL STATE FOUND"
            next_states = current_node.generate_children()
            for node in next_states:
                if node.state not in visited_nodes:
                    visited_nodes.append(node.state)
                    if method == "bfs":
                        queue.insert(0, node )
                        #Adding to the front of a queue gives FIFO Behavior
                    else:
                        queue.append(node)
                        #Adding to the back of a queue gives LIFO Behavior
            if method == "ast":
                queue.sort(key = lambda node: node ManhattanDistance() + node.path_cost, reverse = True)

