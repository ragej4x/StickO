import pygame as pg
pg.init()



class run():
    def __init__(self) -> None:
        pass

        self.run1 = pg.image.load("data/player/p_move/run1.png")
        self.run2 = pg.image.load("data/player/p_move/run2.png")

        self.run1.set_colorkey((255,255,255))
        self.run2.set_colorkey((255,255,255))

        
        self.list = [

            self.run1,
            self.run2,
        ]


        self.listLeft = [

            pg.transform.flip(self.run1 , True,False),
            pg.transform.flip(self.run2 , True,False),
            
        ]

        self.listLeft[0].set_colorkey((255,255,255))
        self.listLeft[1].set_colorkey((255,255,255))

animateRun = run()


class idle():
    def __init__(self) -> None:
        pass

        self.idle1 = pg.image.load("data/player/p_move/idle1.png")
        self.idle2 = pg.image.load("data/player/p_move/idle2.png")
        self.idle3 = pg.image.load("data/player/p_move/idle3.png")
        self.idle4 = pg.image.load("data/player/p_move/idle4.png")


        self.idle1.set_colorkey((255,255,255))
        self.idle2.set_colorkey((255,255,255))
        self.idle3.set_colorkey((255,255,255))
        self.idle4.set_colorkey((255,255,255))


        self.list = [

            self.idle1,
            self.idle2,
            self.idle3,
            self.idle4,

        ]
        
        self.listLeft = [

            pg.transform.flip(self.idle1 , True , False),
            pg.transform.flip(self.idle2 , True , False),
            pg.transform.flip(self.idle3 , True , False), 
            pg.transform.flip(self.idle4 , True , False),
        ]

        self.listLeft[0].set_colorkey((255,255,255))
        self.listLeft[1].set_colorkey((255,255,255))
        self.listLeft[2].set_colorkey((255,255,255))
        self.listLeft[3].set_colorkey((255,255,255))


animateIdle = idle()



class atk_1():
    def __init__(self) -> None:
        pass
        
        self.atk1 = pg.image.load("data/player/atk/atk1.png")
        self.atk2 = pg.image.load("data/player/atk/atk2.png")
        self.atk3 = pg.image.load("data/player/atk/atk3.png")
        self.atk4 = pg.image.load("data/player/atk/atk4.png")

        self.atk1.set_colorkey((255,255,255))
        self.atk2.set_colorkey((255,255,255))
        self.atk3.set_colorkey((255,255,255))
        self.atk4.set_colorkey((255,255,255))


        self.list = [

            self.atk1,
            self.atk2,
            self.atk3,
            self.atk4,
        ]

        self.listLeft = [

            pg.transform.flip(self.atk1, True , False),
            pg.transform.flip(self.atk2, True , False),
            pg.transform.flip(self.atk3, True , False),
            pg.transform.flip(self.atk4, True , False),
        ]

        self.listLeft[0].set_colorkey((255,255,255))
        self.listLeft[1].set_colorkey((255,255,255))
        self.listLeft[2].set_colorkey((255,255,255))
        self.listLeft[3].set_colorkey((255,255,255))


animateAtk1 = atk_1()


class atk_2():
    def __init__(self) -> None:
        pass
        
        self.atk1 = pg.image.load("data/player/atk/p2_atk1.png")
        self.atk2 = pg.image.load("data/player/atk/p2_atk2.png")
        self.atk3 = pg.image.load("data/player/atk/p2_atk3.png")
        self.atk4 = pg.image.load("data/player/atk/p2_atk4.png")



        self.atk1.set_colorkey((255,255,255))
        self.atk2.set_colorkey((255,255,255))
        self.atk3.set_colorkey((255,255,255))
        self.atk4.set_colorkey((255,255,255))


        self.list = [

            self.atk1,
            self.atk2,
            self.atk3,
            self.atk4,
        ]

        self.listLeft = [

            pg.transform.flip(self.atk1, True , False),
            pg.transform.flip(self.atk2, True , False),
            pg.transform.flip(self.atk3, True , False),
            pg.transform.flip(self.atk4, True , False),
        ]

        self.listLeft[0].set_colorkey((255,255,255))
        self.listLeft[1].set_colorkey((255,255,255))
        self.listLeft[2].set_colorkey((255,255,255))
        self.listLeft[3].set_colorkey((255,255,255))

animateAtk2 = atk_2()


class down():
    def __init__(self):

        self.down1 = pg.image.load("data/player/down/down1.png")
        self.down2 = pg.image.load("data/player/down/down2.png")
        self.down3 = pg.image.load("data/player/down/down3.png")
        self.down4 = pg.image.load("data/player/down/down4.png")
        self.down5 = pg.image.load("data/player/down/down5.png")

        self.down1.set_colorkey((255,255,255))
        self.down2.set_colorkey((255,255,255))
        self.down3.set_colorkey((255,255,255))
        self.down4.set_colorkey((255,255,255))
        self.down5.set_colorkey((255,255,255))

        self.list = [

        self.down1,
        self.down2,
        self.down3,
        self.down4,
        self.down5,

        ]

        self.listLeft = [

        pg.transform.flip(self.list[0], True , False),
        pg.transform.flip(self.list[0], True , False),
        pg.transform.flip(self.list[0], True , False),
        pg.transform.flip(self.list[0], True , False),
        pg.transform.flip(self.list[0], True , False),

        ]


        self.listLeft[0].set_colorkey((255,255,255))
        self.listLeft[0].set_colorkey((255,255,255))
        self.listLeft[0].set_colorkey((255,255,255))
        self.listLeft[0].set_colorkey((255,255,255))
        self.listLeft[0].set_colorkey((255,255,255))


animateDown = down()

# GREEN ANIMATION ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class runGreen():
    def __init__(self) -> None:
        pass

        self.run1 = pg.image.load("data/player/colorG/p_move/run1.png")
        self.run2 = pg.image.load("data/player/colorG/p_move/run2.png")

        self.run1.set_colorkey((255,255,255))
        self.run2.set_colorkey((255,255,255))

        
        self.list = [

            self.run1,
            self.run2,
        ]


        self.listLeft = [

            pg.transform.flip(self.run1 , True,False),
            pg.transform.flip(self.run2 , True,False),
            
        ]

        self.listLeft[0].set_colorkey((255,255,255))
        self.listLeft[1].set_colorkey((255,255,255))

animateRunG = runGreen()



class idleGreen():
    def __init__(self) -> None:
        pass

        self.idle1 = pg.image.load("data/player/colorG/p_move/idle1.png")
        self.idle2 = pg.image.load("data/player/colorG/p_move/idle2.png")
        self.idle3 = pg.image.load("data/player/colorG/p_move/idle3.png")
        self.idle4 = pg.image.load("data/player/colorG/p_move/idle4.png")


        self.idle1.set_colorkey((255,255,255))
        self.idle2.set_colorkey((255,255,255))
        self.idle3.set_colorkey((255,255,255))
        self.idle4.set_colorkey((255,255,255))


        self.list = [

            self.idle1,
            self.idle2,
            self.idle3,
            self.idle4,

        ]
        
        self.listLeft = [

            pg.transform.flip(self.idle1 , True , False),
            pg.transform.flip(self.idle2 , True , False),
            pg.transform.flip(self.idle3 , True , False), 
            pg.transform.flip(self.idle4 , True , False),
        ]

        self.listLeft[0].set_colorkey((255,255,255))
        self.listLeft[1].set_colorkey((255,255,255))
        self.listLeft[2].set_colorkey((255,255,255))
        self.listLeft[3].set_colorkey((255,255,255))


animateIdleG = idleGreen()



class atk_1Green():
    def __init__(self) -> None:
        pass
        
        self.atk1 = pg.image.load("data/player/colorG/atk/atk1.png")
        self.atk2 = pg.image.load("data/player/colorG/atk/atk2.png")
        self.atk3 = pg.image.load("data/player/colorG/atk/atk3.png")
        self.atk4 = pg.image.load("data/player/colorG/atk/atk4.png")

        self.atk1.set_colorkey((255,255,255))
        self.atk2.set_colorkey((255,255,255))
        self.atk3.set_colorkey((255,255,255))
        self.atk4.set_colorkey((255,255,255))


        self.list = [

            self.atk1,
            self.atk2,
            self.atk3,
            self.atk4,
        ]

        self.listLeft = [

            pg.transform.flip(self.atk1, True , False),
            pg.transform.flip(self.atk2, True , False),
            pg.transform.flip(self.atk3, True , False),
            pg.transform.flip(self.atk4, True , False),
        ]

        self.listLeft[0].set_colorkey((255,255,255))
        self.listLeft[1].set_colorkey((255,255,255))
        self.listLeft[2].set_colorkey((255,255,255))
        self.listLeft[3].set_colorkey((255,255,255))


animateAtk1G = atk_1Green()


class atk_2Green():
    def __init__(self) -> None:
        pass
        
        self.atk1 = pg.image.load("data/player/colorG/atk/p2_atk1.png")
        self.atk2 = pg.image.load("data/player/colorG/atk/p2_atk2.png")
        self.atk3 = pg.image.load("data/player/colorG/atk/p2_atk3.png")
        self.atk4 = pg.image.load("data/player/colorG/atk/p2_atk4.png")



        self.atk1.set_colorkey((255,255,255))
        self.atk2.set_colorkey((255,255,255))
        self.atk3.set_colorkey((255,255,255))
        self.atk4.set_colorkey((255,255,255))


        self.list = [

            self.atk1,
            self.atk2,
            self.atk3,
            self.atk4,
        ]

        self.listLeft = [

            pg.transform.flip(self.atk1, True , False),
            pg.transform.flip(self.atk2, True , False),
            pg.transform.flip(self.atk3, True , False),
            pg.transform.flip(self.atk4, True , False),
        ]

        self.listLeft[0].set_colorkey((255,255,255))
        self.listLeft[1].set_colorkey((255,255,255))
        self.listLeft[2].set_colorkey((255,255,255))
        self.listLeft[3].set_colorkey((255,255,255))

animateAtk2G = atk_2Green()








#EXCLUDE
# ENEMY AI ANIMATION +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class enemieAnimation():
    def __init__(self):

        self.enem1 = pg.image.load("data/enemy/e_move/run1.png")
        self.enem2 = pg.image.load("data/enemy/e_move/run2.png")

        self.enem1.set_colorkey((255,255,255))
        self.enem2.set_colorkey((255,255,255))


        self.list = [

        self.enem1,
        self.enem2,

        ]

        self.listLeft = [

        pg.transform.flip(self.enem1, True,False),
        pg.transform.flip(self.enem2, True,False),


        ]

        self.listLeft[0].set_colorkey((255,255,255))
        self.listLeft[1].set_colorkey((255,255,255))


enemRun = enemieAnimation()


class enemyAtk():
    def __init__(self):

        self.enem1 = pg.image.load("data/enemy/atk/atk1.png")
        self.enem2 = pg.image.load("data/enemy/atk/atk2.png")
        self.enem3 = pg.image.load("data/enemy/atk/atk3.png")
        self.enem4 = pg.image.load("data/enemy/atk/atk4.png")

        self.enem1.set_colorkey((255,255,255))
        self.enem2.set_colorkey((255,255,255))
        self.enem3.set_colorkey((255,255,255))
        self.enem4.set_colorkey((255,255,255))

        self.list = [

        self.enem1,
        self.enem2,
        self.enem3,
        self.enem4,

        ]


        self.listLeft = [
        
        pg.transform.flip(self.list[0] , True , False),
        pg.transform.flip(self.list[1] , True , False),
        pg.transform.flip(self.list[2] , True , False),
        pg.transform.flip(self.list[3] , True , False),

        ]

        self.listLeft[0].set_colorkey((255,255,255))
        self.listLeft[1].set_colorkey((255,255,255))
        self.listLeft[2].set_colorkey((255,255,255))
        self.listLeft[3].set_colorkey((255,255,255))

enemAtk1 = enemyAtk()