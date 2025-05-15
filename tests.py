import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_create_cells_small(self):
        # Test with a small 2x2 maze
        num_cols = 2
        num_rows = 2
        m2 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m2._cells),
            num_cols,
        )
        self.assertEqual(
            len(m2._cells[0]),
            num_rows,
        )
    
    def test_maze_create_cells_large(self):
        # Test with a larger 20x30 maze
        num_cols = 30
        num_rows = 20
        m3 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m3._cells),
            num_cols,
        )
        self.assertEqual(
            len(m3._cells[0]),
            num_rows,
        )
    
    def test_maze_cells_initialized(self):
        # Test that all cells are properly initialized
        num_cols = 3
        num_rows = 3
        m4 = Maze(0, 0, num_rows, num_cols, 10, 10)
        
        # Check that all cells exist and have walls
        for i in range(num_cols):
            for j in range(num_rows):
                self.assertIsNotNone(m4._cells[i][j])
                self.assertTrue(m4._cells[i][j].has_left_wall)
                self.assertTrue(m4._cells[i][j].has_right_wall)
                self.assertTrue(m4._cells[i][j].has_top_wall)
                self.assertTrue(m4._cells[i][j].has_bottom_wall)
    
    def test_entrance_and_exit(self):
        # Test entrance and exit are properly created
        num_cols = 5
        num_rows = 5
        m5 = Maze(0, 0, num_rows, num_cols, 10, 10)
        
        # Check entrance (top wall of first cell)
        self.assertFalse(m5._cells[0][0].has_top_wall)
        
        # Check exit (bottom wall of last cell)
        self.assertFalse(m5._cells[num_cols-1][num_rows-1].has_bottom_wall)
        
        # Check that other walls of entrance and exit cells are intact
        entrance_cell = m5._cells[0][0]
        self.assertTrue(entrance_cell.has_left_wall)
        self.assertTrue(entrance_cell.has_right_wall)
        self.assertTrue(entrance_cell.has_bottom_wall)
        
        exit_cell = m5._cells[num_cols-1][num_rows-1]
        self.assertTrue(exit_cell.has_left_wall)
        self.assertTrue(exit_cell.has_right_wall)
        self.assertTrue(exit_cell.has_top_wall)

if __name__ == "__main__":
    unittest.main() 