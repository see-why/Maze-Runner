from tkinter import Tk, BOTH, Canvas
from maze import Maze
from window import Window

def main():
    win = Window(800, 600)
    
    # Create a maze with a 12x12 grid of cells
    # Starting at (50,50)
    # Each cell 40x40 pixels
    # Use seed=0 for reproducible testing
    maze = Maze(50, 50, 12, 12, 40, 40, win, seed=0)
    
    win.wait_for_close()

if __name__ == "__main__":
    main()

    