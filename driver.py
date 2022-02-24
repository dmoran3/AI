#
#
#
# 
# 
# 
# 


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
    def generate_nodes(self):
        #create empty array to store next states
        next_states = []

        #find the 0 in the current state
        zero = self.state.index(0)

        
        #UP
        if(zero not in top_row):
            #Swap the value above zero with zero using a new state
            new_state = self.state
            temp = new_state[zero-3]
            new_state[zero-3] = 0
            new_state[zero] = temp
            #UP as a move is now a node that self can choose
            UP = Node(new_state, self, "up", self.depth + 1, 1, self.path_cost +1)
            next_states.append(UP)

        #DOWN
        if(zero not in bottom_row):
            #Swap the value below zero with zero using a new state
            new_state = self.state
            temp = new_state[zero+3]
            new_state[zero+3] = 0
            new_state[zero] = temp
            #DOWN as a move is now a node that self can choose
            DOWN = Node(new_state, self, "down", self.depth + 1, 1, self.path_cost +1)
            next_states.append(DOWN)

        #LEFT
        if(zero not in left_side):
            #Swap the value next to zero with zero using a new state
            new_state = self.state
            temp = new_state[zero-1]
            new_state[zero-1] = 0
            new_state[zero] = temp
            #LEFT as a move is now a node that self can choose
            LEFT = Node(new_state, self, "left", self.depth + 1, 1, self.path_cost +1)
            next_states.append(LEFT)

        #RIGHT
        if(zero not in right_side):
            #Swap the value next to zero with zero using a new state
            new_state = self.state
            temp = new_state[zero+1]
            new_state[zero+1] = 0
            new_state[zero] = temp
            #RIGHT as a move is now a node that self can choose
            RIGHT = Node(new_state, self, "right", self.depth + 1, 1, self.path_cost +1)
            next_states.append(RIGHT)



    def BFS(self, goal_state):
        start = time.time()


        queue = [self]
        queue_number_of_nodes_popped = [0]
        queue_max_length = 1

        depth_queue = [0]
        path_cost_queue = [0]
        visited = set([])

        #while queue:
            #update queue
