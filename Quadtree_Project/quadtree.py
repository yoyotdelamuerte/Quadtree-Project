# Import necessary libraries
from __future__ import annotations
import tkinter as tk


class QuadTree:
    """
    Represents a QuadTree data structure.

    Attributes:
        NB_NODES (int): Number of nodes in the QuadTree.
    """

    NB_NODES: int = 4

    def __init__(self, hg: bool | QuadTree, hd: bool | QuadTree, bd: bool | QuadTree, bg: bool | QuadTree):
        """
        Initializes a QuadTree node with four subtrees.

        Args:
            hg (bool | QuadTree): Northwest subtree.
            hd (bool | QuadTree): Northeast subtree.
            bd (bool | QuadTree): Southwest subtree.
            bg (bool | QuadTree): Southeast subtree.
        """

    @property
    def depth(self) -> int:
        """
        Returns the depth of the QuadTree recursion.

        Returns:
            int: The depth of the recursion.
        """
        return 1

    @staticmethod
    def fromFile(filename):
        """
        Creates a QuadTree from file.

        Args:
            filename (str): The name of the file containing QuadTree data.

        Returns:
            QuadTree: The QuadTree created from file.
        """
        with open(filename, 'r') as file:
            data = eval(file.read())
        return QuadTree.fromList(data)

    @staticmethod
    def fromList(data):
        """
        Creates a QuadTree from data in the form of list.

        Args:
            data (list): The data to create QuadTree.

        Returns:
            QuadTree: QuadTree created from the data.
        """
        if isinstance(data, list):
            if isinstance(data[0], list):
                hg, hd, bg, bd = (QuadTree.fromList(sublist) for sublist in data)
                return QuadTree(hg, hd, bg, bd)
            else:
                return QuadTree(*data)


class TkQuadTree(QuadTree):
    """
    Represents a graphical interface for visualizing QuadTree using Tkinter.
    Inherits from the QuadTree class.
    """

    def __init__(self, data):
        """
        Initializes the Tkinter graphical interface to represent a QuadTree.

        Args:
            data: QuadTree data in the form of a list.
        """
        # Call the parent class constructor with arbitrary values, as they will be replaced in the draw method
        super().__init__(None, None, None, None)
        self.data = data
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()
        self.draw(0, 0, 400, self.data)

    def draw(self, x, y, size, node):
        """
        Draws the QuadTree recursively.

        Args:
            x (int): X-coordinate of the drawing area.
            y (int): Y-coordinate of the drawing area.
            size (int): Size of the drawing area.
            node: The current node of the QuadTree.
        """
        if isinstance(node, list):
            half_size = size // 2
            self.draw(x, y, half_size, node[0])
            self.draw(x + half_size, y, half_size, node[1])
            self.draw(x, y + half_size, half_size, node[2])
            self.draw(x + half_size, y + half_size, half_size, node[3])
        elif isinstance(node, int):
            fill_color = 'white' if node == 0 else 'black'
            self.canvas.create_rectangle(x, y, x + size, y + size, fill=fill_color, outline='black')

    def paint(self):
        """
        Starts the main loop of the Tkinter graphical interface to display the QuadTree.
        """
        self.root.mainloop()


# Main block to execute the program
if __name__ == '__main__':
    # Read data from file and create a TkQuadTree
    filename = 'quadtree.txt'
    with open(filename, 'r') as file:
        data = eval(file.read())
    tk_quadtree = TkQuadTree(data)
    tk_quadtree.paint()
