from tkinter import Tk, BOTH, Canvas
from line import Line
from point import Point
from window import Window
from cell import Cell

def main():
    win = Window(800, 600)
    
    # Create a 2x2 grid of cells
    cell1 = Cell(win)
    cell1.draw(50, 50, 100, 100)
    
    cell2 = Cell(win)
    cell2.draw(100, 50, 150, 100)
    
    cell3 = Cell(win)
    cell3.draw(50, 100, 100, 150)
    
    cell4 = Cell(win)
    cell4.draw(100, 100, 150, 150)
    
    # Draw some moves between cells
    # Regular move from cell1 to cell2
    cell1.draw_move(cell2)
    
    # Regular move from cell2 to cell4
    cell2.draw_move(cell4)
    
    # Backtrack move from cell4 to cell3
    cell4.draw_move(cell3, undo=True)
    
    win.wait_for_close()

if __name__ == "__main__":
    main()

    