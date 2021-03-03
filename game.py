import random
import copy
import time


class Game:
    def __init__(self, seed, size=5):
        self.seed = seed
        self.generation = 0
        self.grid = [[0]] * (size + 2)
        random.seed(seed)
        pattern = list(map(int, bin(random.randint(0, int("".join(['1'] * (size ** 2)), 2)))[2:]))
        if len(pattern) != size ** 2:
            pattern.extend([0] * (size ** 2 - len(pattern)))
        self.grid[0] = [0] * (size + 2)
        self.grid[-1] = [0] * (size + 2)
        for x in range(0, size):
            self.grid[x + 1] = [0, *pattern[x * size: (x + 1) * size], 0]
        self.print()

    def print(self):
        print(f"Generation: {self.generation}")
        for x in self.grid:
            for y in x:
                if y == 1:
                    print("■", end="")
                else:
                    print("▢", end="")
            print()
        print()

    def count_neighbors(self):
        pass

    def generate(self):
        # logic is if there are 3 live cells around it becomes alive no matter what
        # if there are 2 live cells it remains how it was
        # if there are neither of those it is dead

        self.generation += 1
        new = copy.deepcopy(self.grid)
        # check top left corner
        if self.grid[0][1] + self.grid[1][1] + self.grid[1][0] == 3:
            new[0][0] = 1
        elif self.grid[0][1] + self.grid[1][1] + self.grid[1][0] != 2:
            new[0][0] = 0

        # check top row
        for x in range(1, len(self.grid[0]) - 1):
            if self.grid[0][x - 1] + self.grid[0][x + 1] + self.grid[1][x] + self.grid[1][x - 1] + \
                    self.grid[1][x + 1] == 3:
                new[0][x] = 1
            elif self.grid[0][x - 1] + self.grid[0][x + 1] + self.grid[1][x] + self.grid[1][x - 1] + \
                    self.grid[1][x + 1] != 2:
                new[0][x] = 0

        # check top right corner
        if self.grid[0][-2] + self.grid[1][-2] + self.grid[1][-1] == 3:
            new[0][-1] = 1
        elif self.grid[0][-2] + self.grid[1][-2] + self.grid[1][-1] != 2:
            new[0][-1] = 0

        # left column
        for x in range(1, len(self.grid) - 1):
            if self.grid[x - 1][0] + self.grid[x + 1][0] + self.grid[x][1] + self.grid[x - 1][1] + \
                    self.grid[x + 1][1] == 3:
                new[x][0] = 1
            elif self.grid[x - 1][0] + self.grid[x + 1][0] + self.grid[x][1] + self.grid[x - 1][1] + \
                    self.grid[x + 1][1] != 2:
                new[x][0] = 0

        # check middle size * size area
        for x in range(1, len(self.grid) - 1):
            for y in range(1, len(self.grid) - 1):
                if self.grid[x + 1][y] + self.grid[x - 1][y] + self.grid[x][y + 1] + self.grid[x][y - 1] +\
                        self.grid[x + 1][y + 1] + self.grid[x + 1][y - 1] + self.grid[x - 1][y + 1] + \
                        self.grid[x - 1][y - 1] == 3:
                    new[x][y] = 1
                elif self.grid[x + 1][y] + self.grid[x - 1][y] + self.grid[x][y + 1] + self.grid[x][y - 1] + \
                        self.grid[x + 1][y + 1] + self.grid[x + 1][y - 1] + self.grid[x - 1][y + 1] + \
                        self.grid[x - 1][y - 1] != 2:
                    new[x][y] = 0

        # right column
        for x in range(1, len(self.grid) - 1):
            if self.grid[x - 1][-1] + self.grid[x + 1][-1] + self.grid[x][-2] + self.grid[x - 1][-2] + \
                    self.grid[x + 1][-2] == 3:
                new[x][-1] = 1
            elif self.grid[x - 1][-1] + self.grid[x + 1][-1] + self.grid[x][-2] + self.grid[x - 1][-2] + \
                    self.grid[x + 1][-2] != 2:
                new[x][-1] = 0

        # bottom left corner
        if self.grid[-1][1] + self.grid[-2][1] + self.grid[-2][0] == 3:
            new[-1][0] = 1
        elif self.grid[-1][1] + self.grid[-2][1] + self.grid[-2][0] != 2:
            new[-1][0] = 0

        # bottom row
        for x in range(1, len(self.grid[0]) - 1):
            if self.grid[-1][x - 1] + self.grid[-1][x + 1] + self.grid[-2][x] + self.grid[-2][x - 1] + \
                    self.grid[-2][x + 1] == 3:
                new[-1][x] = 1
            elif self.grid[-1][x - 1] + self.grid[-1][x + 1] + self.grid[-2][x] + self.grid[-2][x - 1] + \
                    self.grid[-2][x + 1] != 2:
                new[-1][x] = 0

        # bottom right corner
        if self.grid[-1][-2] + self.grid[-2][-2] + self.grid[-2][-1] == 3:
            new[-1][-1] = 1
        elif self.grid[-1][-2] + self.grid[-2][-2] + self.grid[-2][-1] != 2:
            new[-1][-1] = 0

        self.grid = new

hey = Game(1, 20)
hey.print()
for i in range(100):
    hey.generate()
    hey.print()
    time.sleep(0.5)

