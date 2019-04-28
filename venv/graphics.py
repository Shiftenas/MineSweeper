import game,tkinter as Tk

src = "./data/pic/"

bombnearby = []
for i in range(1,9) :
    bombnearby.append(str(i)+"_bomb_nearby.png")
flagged = "flag.png"
basic = "not_pressed.png"
pressed = "pressed.png"
bomb = "bomb_pressed.png"
all_bomb = "bomb_not_pressed.png"
fail_flag = "flag_fail.png"

class GameGrid(Tk.Frame):
    def __init__(self,difficulty : str = "default"):
        Tk.Frame.__init__(self)
        self.game = game.MineSweeper(difficulty)
        self.grid()
        self.master.title('Mine Sweeper')
        self.grid_cells = []
        self.GRID_WIDTH = len(self.game.grid.numbers) * 30
        self.GRID_HEIGHT = len(self.game.grid.numbers[0]) * 30
        self.GRID_WIDTH_N = len(self.game.grid.numbers)
        self.GRID_HEIGHT_N = len(self.game.grid.numbers[0])
        self.init_grid()
        self.init_matrix()
        #self.update_grid_cells()

        self.mainloop()

    def init_grid(self):
        background = Tk.Frame(self, width=self.GRID_WIDTH, height=self.GRID_HEIGHT, bg="#000000")
        background.grid()


        for i in range(self.GRID_WIDTH_N):
            grid_row = []
            for j in range(self.GRID_HEIGHT_N):
                basic_image = Tk.PhotoImage(src+basic)
                cell = Tk.Frame(background, bg="#888888",
                             width=30,
                             height=30)
                cell.grid(row=i, column=j, padx=0,pady=0)
                t = Tk.Label(master=cell)
                t.grid()
                grid_row.append(t)
                print(str(i) + " " + str(j))

            self.grid_cells.append(grid_row)



    def init_matrix(self):
        self.matrix = self.game.grid
        self.history_matrixs = list()

    def update_grid_cells(self):
        for i in range(self.GRID_WIDTH_N):
            for j in range(self.GRID_HEIGHT_N):
                new_state = self.game.grid.display[i][j]
                if new_state:
                    self.grid_cells[i][j].configure(image=bombnearby[self.game.grid.numbers[i][j]])
        self.update_idletasks()


