import init as grid_maker

class MineSweeper :

    def __init__(self,choose="default"):
        self.end = False
        self.mining = True
        init = grid_maker.Init(choose)
        self.grid = init.grid

    def switch(self) :
        self.mining = not self.mining

    def checkVictory(self):
        for i in len(self.grid.mine) :
            for j in len(self.grid.mine[i]) :
                if not self.grid.mine[i][j] and not self.grid.display[i][j] :
                    return False
        return True

    def select(self,h,w):
        if not self.mining :
            self.grid.flag[h][w] = not self.grid.flag[h][w]
        elif not self.grid.flag[h][w] :
            self.activate(h,w)

    def activate(self,h,w):
        if self.grid.mine[h][w] :
            displayBomb()
            self.end = True
        else :
            display(h,w)

    def displayBomb(self):
        for i in range(len(self.grid.mine)) :
            for j in range(len(self.grid.mine[i])) :
                if self.grid.mine[i][j] :
                    self.grid.display[i][j] = True

    def display(self,h,w):
        self.grid.display[h][w] = True
        if self.grid.numbers[h][w] == 0 :
            if h > 0 :
                self.display(h-1,w)
            if w > 0 :
                self.display(h,w-1)
            if h < len(self.grid.numbers) - 1 :
                self.display(h+1,w)
            if w < len(self.grid.numbers[h]) - 1 :
                self.display(h,w+1)
