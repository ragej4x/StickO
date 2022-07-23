import pygame as pg
pg.init()



class playSound():
    def __init__(self):


        self.cut = pg.mixer.Sound("data/sfx/hit-sword3.data")
        self.swing = pg.mixer.Sound("data/sfx/wsh-sword.data")
        
        


sfx = playSound()


