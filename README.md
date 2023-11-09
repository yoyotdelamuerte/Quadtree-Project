# QuadTree Project using Tkinter

This project demonstrates the visualization of a QuadTree data structure using Tkinter interface library in Python.

## :computer: Overview

A QuadTree is a tree data structure in which each internal node has exactly four children, corresponding to the four quadrants of a Cartesian coordinate system. This project provides a simple implementation of a QuadTree and a Tkinter-based graphical representation of the tree.

## :gift: Features

- **QuadTree Class:** Defines the QuadTree data structure with the ability to create a QuadTree from a file or a nested list.
- **TkQuadTree Class:** Inherits from the QuadTree class and utilizes Tkinter to create a graphical representation of the QuadTree.

## :bust_in_silhouette: Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/yoyotdelamuerte/Quadtree-Project.git
   ```

3. :rocket: Run the main script:

   ```bash
   python quadtree.py
   ```

   This will read the QuadTree data from the specified file (`quadtree.txt` by default) and display the graphical representation using Tkinter.
   
   It will make you smile :smiley:.
   
## :file_folder: File Format

The QuadTree data is stored in a text file (`quadtree.txt` by default) in Python list format. The QuadTree structure is represented as nested lists, with leaves containing boolean values (0 or 1).

Example:

```python
[[0, 1], [1, 0]]
```

## :bookmark: Requirements

- Python 3.12 
- Tkinter library (usually included with Python installations)

## :white_check_mark: License
Feel free to explore, modify, and use the code in your projects! If you encounter any issues or have suggestions, please create an issue or pull request.
