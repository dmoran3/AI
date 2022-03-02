# 
# 
#Dan Moran
#AI HW1 Search
#Spring 2022
# 
#
#-*- coding: utf-8 -*-

import sys
import time
from resource import *

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

        #Only generate children nodes for states that are reachable

        #UP
        if(zero not in top_row):
            #Swap the value above zero with zero using a new state
            new_state = list(self.state[:])
            temp = zero-3
            new_state[temp] = 0
            new_state[zero] = self.state[temp]
            #UP as a move is now a node that self can choose
            UP = Node(new_state, self, "up", self.depth + 1, 1, self.total_path_cost +1)
            next_states.append(UP)

        #DOWN
        if(zero not in bottom_row):
            #Swap the value below zero with zero using a new state
            new_state = list(self.state[:])
            temp = zero+3
            new_state[temp] = 0
            new_state[zero] = self.state[temp]
            #DOWN as a move is now a node that self can choose
            DOWN = Node(new_state, self, "down", self.depth + 1, 1, self.total_path_cost +1)
            next_states.append(DOWN)

        #LEFT
        if(zero not in left_side):
            #Swap the value next to zero with zero using a new state
            new_state = list(self.state[:])
            temp = zero-1
            new_state[temp] = 0
            new_state[zero] = self.state[temp]
            #LEFT as a move is now a node that self can choose
            LEFT = Node(new_state, self, "left", self.depth + 1, 1, self.total_path_cost +1)
            next_states.append(LEFT)

        #RIGHT
        if(zero not in right_side):
            #Swap the value next to zero with zero using a new state
            new_state = list(self.state[:])
            temp = zero+1
            new_state[temp] = 0
            new_state[zero] = self.state[temp]
            #RIGHT as a move is now a node that self can choose
            RIGHT = Node(new_state, self, "right", self.depth + 1, 1, self.total_path_cost +1)
            next_states.append(RIGHT)

        return next_states

    def ManhattanDistance(self):
        total_distance = 0
        for number in self.state:
            number_index = self.state.index(number)
            goal_state_index = goal_state.index(number)

            #y position (row) found by floor division of the index
            #x position (column) found by taking mod 3 of the index
            #manhattanDistance is abs(difference in x position) + abs(difference in y position)
            distance = abs((goal_state_index % 3) - (number_index % 3)) + abs((goal_state_index \
                 // 3) - (number_index // 3))
            total_distance += distance
        return distance

def print_statistics(self, start_time, end_time, path_to_goal, cost_of_path, nodes_expanded, \
        search_depth, max_search_depth, max_ram_usage):
    print("path_to_goal: ", path_to_goal)
    print("cost_of_path: ", cost_of_path)
    print("nodes_expanded:  ", nodes_expanded)
    print("search_depth: ", search_depth)
    print("max_search_depth: ", max_search_depth)
    print("running_time: ", (end_time - start_time))
    print("max_ram_usage: ", max_ram_usage)

def solver(method, starting_state, goal_state):
    start_time = time.time()
    visited_nodes = [list(starting_state)]
    #__init__(self, state, parent, action, depth, cost, total_path_cost)
    queue = [Node(starting_state, None, None, 0, 0, 0)]
    nodes_expanded = 0
    max_queue = 0
    max_depth = 0
    while(len(queue)>0):
        #Update queue information
        max_queue = max(len(queue), max_queue)
        current_node = queue.pop()
        
        if current_node.state == goal_state:
            end_time =  time.time()
            path = []
            curr = current_node
            while curr.parent is not None:
                path.insert(0, curr.action)
                curr = curr.parent
            max_ram_usage = getrusage(RUSAGE_SELF).ru_maxrss
            print_statistics(current_node,
                    start_time, end_time,           #time
                    path,                           #path_to_goal
                    current_node.total_path_cost,   #cost_of_path
                    nodes_expanded,                 #nodes_expanded
                    current_node.depth,             #search_depth
                    max_depth,                      #max_search_depth
                    max_ram_usage            #max_ram_usage
                    )
            return "GOAL STATE FOUND"
        next_states = current_node.generate_children()
        nodes_expanded +=1

        temp_next = []
        if(method != "bfs"):
            next_states.reverse()
        for node in next_states:
            if node.state not in visited_nodes:
                max_depth = max(node.depth, max_depth)
                visited_nodes.append(node.state)
                if method == "bfs":

                    queue.insert(0, node )
                    #Adding to the front of a queue gives FIFO Behavior
                else:
                    queue.append(node)
                    #Adding to the back of a queue gives LIFO Behavior
        if method == "ast":
            queue.sort(key = lambda node: node.ManhattanDistance() + node.total_path_cost, reverse = True)
    return False
 
def main():
    method = sys.argv[1]
    start_state_arg = sys.argv[2].split(',')
    start_state = []
    for num in range(0,len(start_state_arg)):
        start_state.append(int(start_state_arg[num]))
    goal_state = [0,1,2,3,4,5,6,7,8]
    # __init__(self, state, parent, action, depth, cost, total_path_cost
    board = solver(method, start_state, goal_state)
main()