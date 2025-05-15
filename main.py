from tkinter import Tk, BOTH, Canvas
from line import Line
from point import Point
from window import Window
from cell import Cell

def main():
    win = Window(800, 600)
    
    # Create cells with different wall configurations
    
    # Cell 1: All walls (default)
    cell1 = Cell(win)
    cell1.draw(50, 50, 100, 100)
    
    # Cell 2: No right wall
    cell2 = Cell(win)
    cell2.has_right_wall = False
    cell2.draw(100, 50, 150, 100)
    
    # Cell 3: No left wall (connects to cell 2)
    cell3 = Cell(win)
    cell3.has_left_wall = False
    cell3.draw(150, 50, 200, 100)
    
    # Cell 4: Only top and bottom walls
    cell4 = Cell(win)
    cell4.has_left_wall = False
    cell4.has_right_wall = False
    cell4.draw(50, 150, 200, 200)
    
    # Cell 5: Only side walls
    cell5 = Cell(win)
    cell5.has_top_wall = False
    cell5.has_bottom_wall = False
    cell5.draw(250, 50, 300, 200)
    
    win.wait_for_close()

if __name__ == "__main__":
    main()

    