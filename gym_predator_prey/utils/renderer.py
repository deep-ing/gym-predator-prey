
import numpy as np 
import curses
class TerminalRenderer:
    def __init__(self, width, height, n_predators):

        self.stdscr = curses.initscr()
        self.right_window = curses.newwin(n_predators+10, width+80, 1, width+8)
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)
        self.width = width 
        self.height = height
        self.pad = curses.newpad(self.height+4 , self.width+5 )

    def render(self, predator_poses, prey_poses, eaten_positions):
        # self.stdscr.clear()
        self.right_window.clear()
        self.pad.clear()
        bx = 1
        by = 1 
        for x in range(1, self.height+2):
            self.pad.addch(x,0, '|')
            self.pad.addch(x, self.width+bx+3,  '|')

        for y in range(1, self.width+4):
            self.pad.addch(0,y, '-')
            self.pad.addch(self.height+by+1, y, '-')

        self.right_window.addstr("[Predator Prey Information]\n")
        self.right_window.addstr("----------------\n")
        self.right_window.addstr("🦁 eats 🐔 [count] : Recent 3 ")
        self.right_window.addstr("Predator", curses.color_pair(1))
        self.right_window.addstr(" and ")
        self.right_window.addstr("Prey", curses.color_pair(2))
        self.right_window.addstr(" Positions \n")

        for predator, eaten_info  in enumerate(eaten_positions):
            self.right_window.addstr(" {0} [{1}]: ".format(predator, len(eaten_info)))
            for predator_pos, prey_pos in eaten_info[::-1][:3]:
                self.right_window.addstr("({0:.1f},{1:.1f})".format(float(predator_pos[0]), float(predator_pos[1])), curses.color_pair(1))
                self.right_window.addstr(" ")
                self.right_window.addstr("({0:.1f},{1:.1f})".format(float(prey_pos[0]), float(prey_pos[1])), curses.color_pair(2))
                self.right_window.addstr(" | ")
            self.right_window.addstr("\n")
            
        self.right_window.addstr("----------------\n")


        self.right_window.addstr("[🐔] Alive Positions\n")
        for x,y in sorted(prey_poses):
            self.pad.addch(y+by,x+bx, '🐔')
            self.right_window.addstr("({0},{1}) ".format(x,y))

        self.right_window.addstr("\n\n[🦁] Alive Positions\n")
        for x,y in sorted(predator_poses):
            self.right_window.addstr("({0},{1}) ".format(x,y))
            self.pad.addch(y+by,x+bx, '🦁')

        self.right_window.move(0,0)
        self.pad.move(0,0)
        self.right_window.refresh()
        self.pad.refresh(0,0, 1,1, self.height+4, self.width+5)

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

