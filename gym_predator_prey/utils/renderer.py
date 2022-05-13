
import numpy as np 
class TerminalRenderer:
    def __init__(self, width, height):
        import curses
        self.stdscr = curses.initscr()
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        # win = curses.newwin(height*2, width*2, 0, 0)
        self.width = width 
        self.height = height
        self.pad = curses.newpad(self.height+3 , self.width+3 )

    def render(self, predator_poses, prey_poses):
        # self.stdscr.clear()
        self.pad.clear()
        bx = 1
        by = 1 
        for x in range(1, self.height+2):
            self.pad.addch(x,0, '|')
            self.pad.addch(x, self.width+bx+1,  '|')

        for y in range(1, self.width+2):
            self.pad.addch(0,y, '-')
            self.pad.addch(self.height+by+1, y, '-')

        for x,y in predator_poses:
            self.pad.addch(y+by,x+bx, '🐺')
        for x,y in prey_poses:
            self.pad.addch(y+by,x+bx, '🐑')
        self.pad.move(0,0)
        self.pad.refresh(0,0, 1,1, self.height+3, self.width+3)
        # self.stdscr.refresh()
        
    

if __name__ == "__main__":

    import time 
    width= 20
    height = 10
    tr = TerminalRenderer(width=width,height=height)

    while True:
        pdp = [(np.random.randint(width),2), (np.random.randint(width),6), (2,np.random.randint(height))]
        prp = [(np.random.randint(width),4), (np.random.randint(width),7)]
        tr.render(pdp, prp)
        time.sleep(1)
        print("Done")

