from random import random as ran

class Grid :

    display = []
    mine = []
    flag = []
    numbers = []

    def __init__(self,height : int,width : int,bombs : int):
        for i in range(height) :
            line = []
            lineNumbers = []
            for j in range(width) :
                line.append(False)
                lineNumbers.append(0)
            self.display.append(line)
            self.mine.append(line)
            self.flag.append(line)
            self.numbers.append(lineNumbers)
        self.addBomb(height, width, bombs)
        self.setNumbers()

    def setNumbers(self) :
        for i in range(len(self.mine)) :
            for j in range(len(self.mine[i])) :
                count = 0
                if i > 0 :
                    if j > 0 :
                        if self.mine[i-1][j-1] :
                            count += 1
                    if self.mine[i-1][j] :
                        count += 1
                    if j < len(self.mine[i]) - 1 :
                        if self.mine[i-1][j+1] :
                            count += 1
                if j > 0 :
                    if self.mine[i][j-1] :
                        count += 1
                if j < len(self.mine[i]) - 1 :
                    if self.mine[i][j+1] :
                        count += 1
                if i < len(self.mine) - 1 :
                    if j > 0 :
                        if self.mine[i+1][j-1] :
                            count += 1
                    if self.mine[i+1][j] :
                        count += 1
                    if j < len(self.mine[i]) - 1 :
                        if self.mine[i+1][j+1] :
                            count += 1
                self.numbers[i][j] = count



    def addBomb(self,h : int,w : int,b : int):
        if b > h * w :
            exit(1)
        for i in range(b) :
            hran = round(ran() * (h - 1))
            wran = round(ran() * (w - 1))
            while self.mine[hran][wran] :
                hran = round(ran() * (h - 1))
                wran = round(ran() * (w - 1))
            self.mine[hran][wran] = True
