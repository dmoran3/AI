import random
from BaseAI_3 import BaseAI
import Grid_3
import math
import numpy as np
import time

clock = 0
rewardGrid = np.array([
		[2**1, 2**2, 2**3, 2**4],
		[2**8, 2**7, 2**6, 2**5],
		[2**9, 2**10, 2**11, 2**12],
		[2**16, 2**15, 2**14, 2**13]
	])
# Expectimax Pseudocode:
# def value(state):
# 	if the state is a terminal state: return the state's utility
# 	if the next agent is MAX: return max-value(state)
# 	if the next agent is EXP: return min-value(state)
class PlayerAI(BaseAI):

	#Using one function for both Max-Val and Min-Val from the lectures
	#switches between the two based on depth parameter
 
	#
	def expectiminimax(self, grid, depth, dir = None):
		#print(time.time())
		if(depth < 0):
		#if(time.time() >= clock + 0.2):
			#print(time.time())
			return ((self.getHeuristicTileLayout(grid) * .5)+(self.getHeuristicSummation(grid) * .5))
		if depth == int(depth):
			#if player's turn
			V = -math.inf
			for dir in grid.getAvailableMoves():
				new_board = grid.clone()
				new_board.move(dir)
				f = self.expectiminimax(new_board, depth - 0.5, dir)
				if f > V: V = f
		elif depth != int(depth):
			#if adversary's turn
			V = 0
			available_cells = grid.getAvailableCells()
			for cell in available_cells:
				grid.insertTile(cell,2)
				f = self.expectiminimax(grid, depth - 0.5, dir)
				if f < V: V = f
				# V += 1.0/len(available_cells) * self.expectiminimax(grid, depth - 0.5, dir)
				# V += 1.0/len(available_cells) * 0.9 * self.expectiminimax(grid, depth - 0.5, dir)
				# grid.insertTile(cell, 4)
				# V += 1.0/len(available_cells) * 0.1 * self.expectiminimax(grid, depth - 0.5, dir)
				grid.insertTile(cell, 0)

		return V
 				
	def alphaBetaExpectiminimax(self, grid, depth, dir = None, alpha, beta):
    		#print(time.time())
		if(depth < 0):
		#if(time.time() >= clock + 0.2):
			#print(time.time())
			return ((self.getHeuristicTileLayout(grid) * .5)+(self.getHeuristicSummation(grid) * .5))
		if depth == int(depth):
			#if player's turn
			V = -math.inf
			for dir in grid.getAvailableMoves():
				new_board = grid.clone()
				new_board.move(dir)
				f = self.expectiminimax(new_board, depth - 0.5, dir, alpha, beta)
				if f >= beta: V = f
				alpha = max(alpha, V)
		elif depth != int(depth):
			#if adversary's turn
			V = 0
			available_cells = grid.getAvailableCells()
			for cell in available_cells:
				grid.insertTile(cell,2)
				f = self.expectiminimax(grid, depth - 0.5, dir, alpha, beta)
				if f < V: V = f
				#V += 1.0/len(available_cells) * self.expectiminimax(grid, depth - 0.5, dir, alpha, beta)
				# V += 1.0/len(available_cells) * 0.9 * self.expectiminimax(grid, depth - 0.5, dir)
				# grid.insertTile(cell, 4)
				# V += 1.0/len(available_cells) * 0.1 * self.expectiminimax(grid, depth - 0.5, dir)
				grid.insertTile(cell, 0)

		return V	

# def expectiminimax(self, grid, depth, dir = None):
#     		#print(time.time())
# 		if(depth < 0):
# 		#if(time.time() >= clock + 0.2):
# 			#print(time.time())
# 			return ((self.getHeuristicTileLayout(grid) * .5)+(self.getHeuristicSummation(grid) * .5))
# 		if depth == int(depth):
# 			#if player's turn
# 			V = -math.inf
# 			for dir in grid.getAvailableMoves():
# 				new_board = grid.clone()
# 				new_board.move(dir)
# 				f = self.expectiminimax(new_board, depth - 0.5, dir)
# 				if f > V: V = f
# 		elif depth != int(depth):
# 			#if adversary's turn
# 			V = 0
# 			available_cells = grid.getAvailableCells()
# 			for cell in available_cells:
# 				grid.insertTile(cell,2)
# 				f = self.expectiminimax(grid, depth - 0.5, dir)
# 				if f < V: V = f
# 				# V += 1.0/len(available_cells) * self.expectiminimax(grid, depth - 0.5, dir)
# 				# V += 1.0/len(available_cells) * 0.9 * self.expectiminimax(grid, depth - 0.5, dir)
# 				# grid.insertTile(cell, 4)
# 				# V += 1.0/len(available_cells) * 0.1 * self.expectiminimax(grid, depth - 0.5, dir)
# 				grid.insertTile(cell, 0)

# 		return V
 				
#      def alphaBetaExpectiminimax(self, grid, depth, dir = None, alpha, beta):
#     		#print(time.time())
# 		if(depth < 0):
# 		#if(time.time() >= clock + 0.2):
# 			#print(time.time())
# 			return ((self.getHeuristicTileLayout(grid) * .5)+(self.getHeuristicSummation(grid) * .5))
# 		if depth == int(depth):
# 			#if player's turn
# 			V = -math.inf
# 			for dir in grid.getAvailableMoves():
# 				new_board = grid.clone()
# 				new_board.move(dir)
# 				f = self.expectiminimax(new_board, depth - 0.5, dir, alpha, beta)
# 				if f >= beta: V = f
# 				alpha = max(alpha, V)
# 		elif depth != int(depth):
# 			#if adversary's turn
# 			V = 0
# 			available_cells = grid.getAvailableCells()
# 			for cell in available_cells:
# 				grid.insertTile(cell,2)
# 				f = self.expectiminimax(grid, depth - 0.5, dir, alpha, beta)
# 				if f < V: V = f
# 				#V += 1.0/len(available_cells) * self.expectiminimax(grid, depth - 0.5, dir, alpha, beta)
# 				# V += 1.0/len(available_cells) * 0.9 * self.expectiminimax(grid, depth - 0.5, dir)
# 				# grid.insertTile(cell, 4)
# 				# V += 1.0/len(available_cells) * 0.1 * self.expectiminimax(grid, depth - 0.5, dir)
# 				grid.insertTile(cell, 0)

# 		return V	

	# based on : Minimax and Expectimax Algorithm to Solve 2048 Ahmad Zaky
	def alphabeta(self, state, depth, alpha, beta, turn):
		#if(depth == 0):
  
		print(time.time())
		if(time.time() >= clock + 2):
			return state.getV
		if(turn == player):
			for successor in state.getSuccessors:
				alpha = max(alpha, alphabeta(successor, depth-1, alpha, beta, pc))
				if(beta <= alpha):
					break
			return alpha
		else:
			for successor in state.getSuccessors:
				beta = min(beta, alphaBeta(successor, depth-1, alpha, beta, player))
				if(beta <= alpha):
					break
			return beta

	#based on https://tseng.ch/2048-ai-best-heuristics/
	def getHeuristicTileLayout(self, grid):
		h=0
		for i in range(4):
			for j in range(4):
				h += (rewardGrid[i][j] * grid.getCellValue((i,j)))
		return h

	def getHeuristicSummation(self, grid):
		h=0
		for i in range(4):
			for j in range(4):
				h += grid.getCellValue((i,j))
		return h	

	def getNextBestMoveExpectiminimax(self, grid):
    	# Initialize to a random move and returns it
		best_move = random.choice(grid.getAvailableMoves())[0]

		depth = 2
		best_score = -math.inf
		new_board = grid.clone()
		for move in new_board.getAvailableMoves():
			new_board = move[1]
			# for i in range(4):
			# 	print(new_board.getCellValue((i,0))," ",new_board.getCellValue((i,1))," ",new_board.getCellValue((i,2))," ",new_board.getCellValue((i,3)))
			score = self.expectiminimax(new_board, depth, move[0])
			# print(score)
			if score > best_score:
				best_score = score
				best_move = move[0]

		return best_move

	def getMove(self, grid):
		clock = time.time()
		print(time.time())
		print(clock)
		if(grid.getMaxTile() == 2048): return NULL
		else: return self.getNextBestMoveExpectiminimax(grid)