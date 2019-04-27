import game,tkinter as Tk

src = "./data/pic/"

bombnearby = []
for i in range(1,9) :
    bombnearby.append(i+"_bomb_nearby.png")
flagged = "flag.png"
basic = "not_pressed.png"
pressed = "pressed.png"
bomb = "bomb_pressed.png"
all_bomb = "bomb_not_pressed.png"
fail_flag = "flag_fail.png"

class GameGrid(Tk.Frame):
    def __init__(self):
        Tk.Frame.__init__(self)
        self.game = game.MineSweeper()
        self.grid()
        self.master.title('Mine Sweeper')

        self.grid_cells = []
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()

        self.mainloop()

    def init_grid(self):
        background = Frame(self, bg=c.BACKGROUND_COLOR_GAME,
                           width=len(self.game.grid), height=len(self.game.grid[0]))
        background.grid()
        """
        for i in range(c.GRID_LEN):
            grid_row = []
            for j in range(c.GRID_LEN):
                cell = Frame(background, bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                             width=c.SIZE / c.GRID_LEN,
                             height=c.SIZE / c.GRID_LEN)
                cell.grid(row=i, column=j, padx=c.GRID_PADDING,
                          pady=c.GRID_PADDING)
                t = Label(master=cell, text="",
                          bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                          justify=CENTER, font=c.FONT, width=5, height=2)
                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)
        """

    def init_matrix(self):
        self.matrix = self.game.grid
        self.history_matrixs = list()

    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(
                        text="", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(text=str(
                        new_number), bg=c.BACKGROUND_COLOR_DICT[new_number],
                        fg=c.CELL_COLOR_DICT[new_number])
        self.update_idletasks()




gamegrid = GameGrid()


