grid = []

for i in range(0,6):
	pos = input()
	x = pos.split()
	grid.append(x)

print("\n")

y = []
x = []

def boomber_man(grid):

	#rec 6x7
	for i in range(0,6):
		for j in range(0,7):
			if grid[i][j] == "O":
				y.append(i)
				x.append(j)
	
	
	for i in range(0,6):
		for j in range(0,7):
			if grid[i][j] == ".":
				grid[i][j] = "O" #bombebis dawkoba kvelgan
		
	for i in range(len(y)):
		#angle
		if y[i] == 0 and x[i] == 0:
			grid[y[i]][x[i]] = "."
			grid[y[i]][x[i]+1] = "."
			grid[y[i]+1][x[i]] = "."
		#angle
		if y[i] == 5 and x[i] == 6:
			grid[y[i]][x[i]] = "."
			grid[y[i]][x[i]-1] = "."
			grid[y[i]-1][x[i]] = "."
		#angle
		if y[i] == 0 and x[i] == 6:
			grid[y[i]][x[i]] = "."
			grid[y[i]+1][x[i]] = "."
			grid[y[i]][x[i]-1] = "."
		#angle
		if y[i] == 5 and x[i] == 0:
			grid[y[i]][x[i]] = "."
			grid[y[i]-1][x[i]] = "."
			grid[y[i]][x[i]+1] = "."
		
		if y[i] > 0 and x[i] > 0 and y[i] < 5:
			grid[y[i]][x[i]] = "."
			grid[y[i]+1][x[i]] = "."
		
		#uwall
		if y[i] == 0 and x[i] > 0 and x[i] < 6:
			grid[y[i]][x[i]] = "."
			grid[y[i]][x[i]+1] = "."
			grid[y[i]][x[i]-1] = "."
			grid[y[i]+1][x[i]] = "."
		#lwall
		if y[i] > 0 and x[i] == 0 and y[i] < 5:
			grid[y[i]][x[i]] = "."
			grid[y[i]][x[i]+1] = "."
			grid[y[i]-1][x[i]] = "."
			grid[y[i]+1][x[i]] = "."
			grid[y[i]+1][x[i]] = "."

		if y[i] > 0 and x[i] > 0 and x[i] < 6:
			grid[y[i]][x[i]] = "."
			grid[y[i]][x[i]-1] = "."
			grid[y[i]][x[i]+1] = "."
			grid[y[i]-1][x[i]] = "."
			grid[y[i]][x[i]+1] = "."
		if y[i] > 0 and x[i] == 6:
			grid[y[i]][x[i]] = "."
			grid[y[i]][x[i]-1] = "."
			grid[y[i]+1][x[i]] = "."
			grid[y[i]-1][x[i]] = "."

	for i in grid:
		print(*i,sep=' ')
	print("\n\n")

		




boomber_man(grid)
