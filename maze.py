from cell import Cell
import time

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
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        
        self._create_cells()
    
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