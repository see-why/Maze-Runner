from cell import Cell
import time
import random

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        create_entrance_exit=True,
        seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        
        if seed is not None:
            random.seed(seed)
        
        self._create_cells()
        self._break_walls_r(0, 0)  # Start breaking walls from the top-left cell
        self._reset_cells_visited()  # Reset visited flags after generating maze
        if create_entrance_exit:
            self._break_entrance_and_exit()
    
    def _create_cells(self):
        # Initialize the grid with empty lists for each column
        self._cells = [[None for _ in range(self._num_rows)] for _ in range(self._num_cols)]
        
        # Create each cell and store it in the grid
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j] = Cell(self._win)
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        # Calculate the pixel positions for this cell
        x1 = self._x1 + (i * self._cell_size_x)
        y1 = self._y1 + (j * self._cell_size_y)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        
        # Draw the cell at the calculated position
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        # Break the top wall of the first cell (entrance)
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        
        # Break the bottom wall of the last cell (exit)
        self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1, self._num_rows-1)
    
    def _break_walls_r(self, i, j):
        # Mark current cell as visited
        self._cells[i][j].visited = True
        
        while True:
            # Get possible directions (unvisited adjacent cells)
            possible_directions = []
            
            # Check left
            if i > 0 and not self._cells[i-1][j].visited:
                possible_directions.append(("left", i-1, j))
            
            # Check right
            if i < self._num_cols-1 and not self._cells[i+1][j].visited:
                possible_directions.append(("right", i+1, j))
            
            # Check up
            if j > 0 and not self._cells[i][j-1].visited:
                possible_directions.append(("up", i, j-1))
            
            # Check down
            if j < self._num_rows-1 and not self._cells[i][j+1].visited:
                possible_directions.append(("down", i, j+1))
            
            # If no possible directions, we're done with this cell
            if len(possible_directions) == 0:
                self._draw_cell(i, j)
                return
            
            # Choose a random direction
            direction, next_i, next_j = random.choice(possible_directions)
            
            # Break walls between current cell and chosen cell
            if direction == "left":
                self._cells[i][j].has_left_wall = False
                self._cells[next_i][next_j].has_right_wall = False
            elif direction == "right":
                self._cells[i][j].has_right_wall = False
                self._cells[next_i][next_j].has_left_wall = False
            elif direction == "up":
                self._cells[i][j].has_top_wall = False
                self._cells[next_i][next_j].has_bottom_wall = False
            else:  # down
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_i][next_j].has_top_wall = False
            
            # Recursively visit the chosen cell
            self._break_walls_r(next_i, next_j)
    
    def _reset_cells_visited(self):
        """Reset the visited flag of all cells to False."""
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False
    
    def solve(self):
        """Start solving the maze from the entrance (top-left cell)."""
        self._reset_cells_visited()  # Reset visited flags before solving
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        """
        Recursively solve the maze using depth-first search.
        Returns True if this cell is or leads to the end cell, False otherwise.
        """
        self._animate()
        self._cells[i][j].visited = True
        
        # If we're at the end cell (bottom-right), we've solved it!
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        
        # Try each possible direction
        # Check right
        if (i < self._num_cols-1 and 
            not self._cells[i][j].has_right_wall and 
            not self._cells[i+1][j].visited):
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1, j):
                return True
            self._cells[i][j].draw_move(self._cells[i+1][j], undo=True)
        
        # Check down
        if (j < self._num_rows-1 and 
            not self._cells[i][j].has_bottom_wall and 
            not self._cells[i][j+1].visited):
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i, j+1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j+1], undo=True)
        
        # Check left
        if (i > 0 and 
            not self._cells[i][j].has_left_wall and 
            not self._cells[i-1][j].visited):
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1, j):
                return True
            self._cells[i][j].draw_move(self._cells[i-1][j], undo=True)
        
        # Check up
        if (j > 0 and 
            not self._cells[i][j].has_top_wall and 
            not self._cells[i][j-1].visited):
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i, j-1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j-1], undo=True)
        
        # If we get here, this cell doesn't lead to the end
        return False 