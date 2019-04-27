import grid

class Init :

    def __init__(self, choice : str = "default"):
        if choice == "easy" :
            self.grid = grid.Grid(11,8,10)
        elif choice == "medium" :
            self.grid = grid.Grid(20,14,39)
        elif choice == "hard" :
            self.grid = grid.Grid(29,20,102)
        elif choice == "insane" :
            self.grid = grid.Grid(38,26,194)
        else :
            self.grid = grid.Grid(20,14,39)
