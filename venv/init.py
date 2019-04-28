import grid

class Init :

    def __init__(self, choice : str = "default"):
        if choice == "easy" :
            self.grid = grid.Grid(8,11,10)
        elif choice == "medium" :
            self.grid = grid.Grid(14,20,39)
        elif choice == "hard" :
            self.grid = grid.Grid(20,29,102)
        elif choice == "insane" :
            self.grid = grid.Grid(26,38,194)
        else :
            self.grid = grid.Grid(14,20,39)
