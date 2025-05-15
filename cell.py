from point import Point
from line import Line

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = 0
        self._x2 = 0
        self._y1 = 0
        self._y2 = 0
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        
        if self._win is None:
            return
        
        # Draw all walls, using background color for removed walls
        # Left wall
        line = Line(Point(x1, y1), Point(x1, y2))
        self._win.draw_line(line, "black" if self.has_left_wall else "#d9d9d9")
        
        # Top wall
        line = Line(Point(x1, y1), Point(x2, y1))
        self._win.draw_line(line, "black" if self.has_top_wall else "#d9d9d9")
        
        # Right wall
        line = Line(Point(x2, y1), Point(x2, y2))
        self._win.draw_line(line, "black" if self.has_right_wall else "#d9d9d9")
        
        # Bottom wall
        line = Line(Point(x1, y2), Point(x2, y2))
        self._win.draw_line(line, "black" if self.has_bottom_wall else "#d9d9d9")
    
    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
            
        # Calculate center points of both cells
        from_center_x = (self._x1 + self._x2) / 2
        from_center_y = (self._y1 + self._y2) / 2
        
        to_center_x = (to_cell._x1 + to_cell._x2) / 2
        to_center_y = (to_cell._y1 + to_cell._y2) / 2
        
        # Create and draw the line with appropriate color
        line = Line(
            Point(from_center_x, from_center_y),
            Point(to_center_x, to_center_y)
        )
        self._win.draw_line(line, "gray" if undo else "red") 