# Conway's Game of Life

## Why?

Have you evere heard about Conway's Game of Life (or 'Life')? If you want a detailed explanation about it, [click here](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).
What really draws my attenttion about this game is its simplicity and, at the same time, complexity.

Conway's Game of Life consists of basically four rules:

1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

By giving to the application an initial state (or seed), the next generation is obtained applying these rules, meaning one state is a pure function of the preceeding one.

Life is undecidable, which means that given an initial pattern and a later pattern, no algorithm exists that can tell whether the later pattern is ever going to appear. This is a corollary of the halting problem: the problem of determining whether a given program will finish running or continue to run forever from an initial input.
