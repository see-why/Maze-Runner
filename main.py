from tkinter import Tk, BOTH, Canvas
from maze import Maze
from window import Window

def main():
    win = Window(800, 600)
    
    # Create a maze with a 4x4 grid of cells
    # Starting at (50,50)
    # Each cell 50x50 pixels
    maze = Maze(50, 50, 4, 4, 50, 50, win)
    
    win.wait_for_close()

if __name__ == "__main__":
    main()

    