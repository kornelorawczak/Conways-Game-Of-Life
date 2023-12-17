import matplotlib.pyplot as plt
import matplotlib.animation as ani
import numpy as np

class Game_of_Life:
    def __init__(self, x, y, rand=True, prob=0, given_tab=[]):
        self.x = x
        self.y = y
        fig, ax = plt.subplots()
        self.board_size=(x, y)
        self.board_colors = np.random.randint(1, 256, (self.board_size[0], self.board_size[1]), dtype=np.uint8)
        #self.board_on_off = np.random.randint(0, 2, (self.board_size[0], self.board_size[1]), dtype=np.uint8) #0 is off, 1 is on
        if rand:
            self.board_on_off = np.random.rand(self.board_size[0], self.board_size[1]) < prob
        else:
            self.board_on_off = self.fill_list()

        self.board = [[self.board_colors[i][j]*self.board_on_off[i][j] for j in range(self.board_size[1])] for i in range(self.board_size[0])]
        self.screen = ax.imshow(np.rot90(self.board), cmap='inferno')
        self.animation = ani.FuncAnimation(fig, self.update, cache_frame_data=False, interval=20)
        self.paused=False
        fig.canvas.mpl_connect('button_press_event', self.toggle_pause)

    def fill_list(self):
        tab = [[0 for _ in range(self.y)] for _ in range(self.x)]
        n = input("Type in how many spaces you want to fill: ")
        for _ in range(int(n)):
            str_input=input(f"Type coordinates (range: {self.x}, {self.y}) with space in between: ")
            x0 = int(str_input.split(" ")[0])
            y0 = int(str_input.split(" ")[1])
            tab[x0][y0] = 1
        return tab
    def toggle_pause(self, *args, **kwargs):
        if self.paused:
            self.animation.resume()
        else:
            self.animation.pause()
        self.paused = not self.paused

    def update(self, *args, **kwargs):
        for x in range(self.board_size[0]):
            for y in range(self.board_size[1]):
                sum_surroundings = sum([self.board_on_off[cords[0]][cords[1]] for cords in self.get_surroundings(x,y)])
                if self.board_on_off[x][y]==0 and sum_surroundings==3:
                    self.board_on_off[x][y]=1
                elif self.board_on_off[x][y]==1 and not (sum_surroundings==2 or sum_surroundings==3):
                    self.board_on_off[x][y]=0
        self.board_update = [[self.board_colors[i][j] * self.board_on_off[i][j] for j in range(self.board_size[1])] for i in range(self.board_size[0])]
        self.screen.set_data(np.rot90(self.board_update))
        return (self.board,)

    def get_surroundings(self, x, y):
        if x==0 and y==0:
            return [(1,0), (1,1), (0,1)]
        elif x==0 and y==self.board_size[1]-1:
            return [(0,y-1), (1, y-1), (1, y)]
        elif x==self.board_size[0]-1 and y==0:
            return [(x-1,0), (x-1,1), (x,1)]
        elif x==self.board_size[0]-1 and y==self.board_size[1]-1:
            return [(x-1, y), (x-1,y-1), (x,y-1)]
        elif x==0:
            return [(0,y+1), (0,y-1), (1,y+1), (1,y), (1,y-1)]
        elif y==0:
            return [(x-1,0), (x+1,0), (x-1,1), (x,1), (x+1,1)]
        elif x==self.board_size[0]-1:
            return [(x,y-1), (x,y+1), (x-1,y-1), (x-1,y), (x-1,y+1)]
        elif y==self.board_size[1]-1:
            return [(x-1,y), (x+1,y), (x-1,y-1), (x,y-1), (x+1,y-1)]
        return [(x-1,y-1), (x-1,y), (x-1,y+1), (x+1,y-1), (x+1,y), (x+1,y+1), (x,y+1), (x,y-1)]



#game = Game_of_Life(100, 80, prob=0.07)
game = Game_of_Life(100, 80, rand=False)
plt.show()
