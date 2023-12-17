# Conways-Game-Of-Life

Python implementation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life). Symulation uses matplotlib library and can be opened either with given or random data generator by numpy module.
Matplotlib animation initialized in this program is infinite. You can pause the animation by just clicking on the screen. In order to exit, just exit the matplotlib window

## Requirements

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install matplotlib module.

```bash
pip install matplotlib
```

## Usage

Depending whether you want the board to be filled randomly with given probability or manually do the following:

For random filling:

-Change given arguments x, y, prob (x, y stands for standard number of pixels in x and y axis of the board, and prob is the variable determining probability of initial random fill, it can take float number between 0 and 1)

```python
game = Game_of_Life(100, 80, prob=0.07)
```

For manual filling:

-Add argument rand=False to the set of arguments taken by the initialization of class object Game_of_Life as in the code snippet below:

```python
game = Game_of_Life(100, 80, rand=False)
```
Then follow the instructions in the input window
