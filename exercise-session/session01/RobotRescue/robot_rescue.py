# See instructions for detailed description.
class RobotRescue:
	def __init__(self, grid, robot, wounded):
		# 0 - empty space
		# 1 - obstacle
		self.grid = grid
		self.robot = robot
		self.wounded = wounded

	# solved: return True if robot and wounded are on the same coordinates.
	def solved(self):
		return self.robot == self.wounded

	# generate_moves: generate a list of all possible moves from current robot positon and
	# their costs.
	def generate_moves(self):
		# Define empty list for storing valid moves.
		res = []
		# Notice pattern in search...
		for drow in (-1, 0, 1):
			for dcol in (-1, 0, 1):
				# If both changes are not zero:
				if not (drow == 0 and dcol == 0):
					# If move not off grid and move not into obstacle:
					if (0 <= self.robot[0] + drow < len(self.grid) and 
						0 <= self.robot[1] + dcol < len(self.grid[0]) and
						self.grid[self.robot[0] + drow][self.robot[1] + dcol] != 1):
							# Add move to list of valid moves.
							res.append(([drow, dcol], 1))
		return res

	# move: apply move (writen in format returned by generate moves).
	def move(self, move_cost):
		self.robot[0] += move_cost[0][0]
		self.robot[1] += move_cost[0][1]

	# undo_move: unapply move (writen in format returned by generate moves).
	def undo_move(self, move_cost):
		self.robot[0] -= move_cost[0][0]
		self.robot[1] -= move_cost[0][1]




# DF: perform depth first search with maximal depth depth and return the path from
# initial to end state.
def DF(pos, depth):
	# If depth is 0, return None.
	if depth < 0:
		return None
	# If system is solved, no moves needed.
	if pos.solved():
		return []
	# Go over all possible moves.
	for move in pos.generate_moves():
		# Apply move.
		pos.move(move)
		# Make recursive call for moved robot with decremented remaining depth.
		found_path = DF(pos, depth - 1)
		# Undo move.
		pos.undo_move(move)
		# If solution was found for starting move.
		if found_path != None:
			# add aplied move to rest of moves leading to final state.
			return [move] + found_path
	# If no path found, return None.
	return None

"""
from copy import deepcopy

def DF_stack(pos):
	stack = []
	stack.append(deepcopy(pos))

	while stack != []:
		state = stack.pop()
		if state.solved():
			return "solved"
		for m in state.generate_moves():
			print(m)
			new_state = deepcopy(state)
			new_state.move(m)
			# Append only if not marked
			stack.append(new_state)

	return None
"""

# Define grid from examples.
grid = [[0, 0, 0, 0, 0], 
		[1, 0, 1, 1, 1], 
		[0, 0, 0, 0, 0], 
		[0, 0, 0, 0, 0], 
		[0, 0, 0, 0, 0]]

# Initialize problem domain initial state.
rr = RobotRescue(grid, [3, 3], [0, 3])