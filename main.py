from tkinter import Tk, BOTH, Canvas
from line import Line
from point import Point

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Runner")
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    
    def close(self):
        self.running = False
    
    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

def main():
    win = Window(800, 600)
    
    # Create some test points
    p1 = Point(100, 100)
    p2 = Point(200, 200)
    p3 = Point(300, 100)
    
    # Create and draw some lines
    line1 = Line(p1, p2)
    line2 = Line(p2, p3)
    
    # Draw the lines with different colors
    win.draw_line(line1, "red")
    win.draw_line(line2, "blue")
    
    win.wait_for_close()

if __name__ == "__main__":
    main()

    