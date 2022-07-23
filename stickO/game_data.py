import random
import pygame as pg
import game_engine as engine
import os
import game_fx as effect
pg.init()

width,height = 600,400
display = pg.display.set_mode((width,height))
pg.display.set_caption("Stick O          RAGEJAXINDEV Alpha V0.1.1")
developer = pg.image.load("ragejax.data")
pg.display.set_icon(developer)
window = pg.Surface((width/2 , height/2))
clock = pg.time.Clock()
font = pg.font.Font("data/pix.ttf" , 18)

info = open("ragejax.data")

logs = open("logs.txt","a")


class mainClass():
    def __init__(self) -> None:
        pass
        global globalVelx
        global globalVely

        self.moveX = False
        self.moveY = False
        self.x = random.randint(200,350)
        self.y = 150
        self.cd = 0
        self.cdBool = False
        self.velX = 10
        self.velY = 10

        self.runLoop = 0

        self.left = True
        self.right = False 

        self.idleLeft = False
        self.idleRight = False

        self.jump = False


        self.s1Loop = 0
        self.s2Loop = 0
        self.s3Loop = 0

        self.s1 = False
        self.s2 = False
        self.s3 = False


        self.enemRight = False
        self.enemLeft = False

        self.enemAtkCount = 0

        self.enemRun = 0

        self.atk1 = False

        self.enemList = [

        0,0,
        0,0,
        0,0,

        ]

        #+++++++++++++++

        globalVelx = self.x
        globalVely = self.y


    def alpha():

        engine.animateIdle.list[0].set_alpha(0)
        engine.animateIdle.list[1].set_alpha(0)     
        engine.animateIdle.list[2].set_alpha(0)
        engine.animateIdle.list[3].set_alpha(0)
    
    def un_alpha():

        engine.animateIdle.list[0].set_alpha()
        engine.animateIdle.list[1].set_alpha()     
        engine.animateIdle.list[2].set_alpha()
        engine.animateIdle.list[3].set_alpha()

    def alphaLeft():

        engine.animateIdle.listLeft[0].set_alpha(0)
        engine.animateIdle.listLeft[1].set_alpha(0)
        engine.animateIdle.listLeft[2].set_alpha(0)
        engine.animateIdle.listLeft[3].set_alpha(0)


    def un_alphaLeft():

        engine.animateIdle.listLeft[0].set_alpha()
        engine.animateIdle.listLeft[1].set_alpha()
        engine.animateIdle.listLeft[2].set_alpha()
        engine.animateIdle.listLeft[3].set_alpha()     



    def playerRects(self):
        global playerRect
        playerRect = pg.draw.rect(window ,(255,0,0) , (self.x + 8, self.y + 8 , 15 ,24 ),1)

        #self.enemRect = pg.draw.rect(window ,(255,0,0) , (self.x + 8, self.y + 8 , 15 ,24 ))
        

 


    def player(self):

        
        if self.s1Loop == 0 and self.right is True and keyinput[pg.K_RIGHT]:
            window.blit(engine.animateRun.list[int(self.runLoop)] , (self.x , self.y))
            self.idleRight = False
            self.idleLeft = False

        else:
            self.idleRight = True


        if self.s1Loop == 0 and self.left is True and keyinput[pg.K_LEFT]:
            window.blit(engine.animateRun.listLeft[int(self.runLoop)] , (self.x , self.y))
            self.idleRight = False
            self.idleLeft = False
        else:
            self.idleLeft = True




        
        if self.right is True and self.idleRight is True:
            window.blit(engine.animateIdle.list[int(self.runLoop)] , (self.x , self.y))


        if self.left is True and self.idleLeft is True:
            window.blit(engine.animateIdle.listLeft[int(self.runLoop)] , (self.x , self.y))






        if self.left is True and self.right is False and self.s1 is True:
            window.blit(engine.animateAtk1.listLeft[int(self.s1Loop)] , (self.x , self.y))


        if self.right is True and self.left is False and self.s1 is True:
            window.blit(engine.animateAtk1.list[int(self.s1Loop)] , (self.x , self.y))



        if self.left is True and self.right is False and self.s2 is True:
            window.blit(engine.animateAtk2.listLeft[int(self.s2Loop)] , (self.x , self.y))


        if self.right is True and self.left is False and self.s2 is True:
            window.blit(engine.animateAtk2.list[int(self.s2Loop)] , (self.x , self.y))



    def input(self):
        global keyinput
        keyinput = pg.key.get_pressed()

        if keyinput[pg.K_RIGHT]:
           self.moveX = True

           self.right = True
           self.left = False
           self.idleRight = True
           self.idleLeft = False
        else:
            self.moveX = False

        if keyinput[pg.K_LEFT]:
            self.moveY = True

            self.left = True
            self.right = False
            self.idleLeft = True
            self.idleRight = False
        else:
            self.moveY = False
        

        if self.s1Loop == 0 and self.moveX is True:
            self.x += 3
        if self.s1Loop == 0 and self.moveY is True:
            self.x -= 3


        if keyinput[pg.K_UP]:
            self.jump = True

        if self.jump is True:
            self.y -= self.velY
            self.velY -= 1

            if self.velY < -10:
                self.velY = 10
                self.jump = False

 
    def count(self):

        self.cd += 0.3
        if self.cd >= 10:
            self.cd = 10
            self.cdBool = True

        self.runLoop += 0.2
        if self.runLoop >= 2:
            self.runLoop = 0
        
        
        if self.cd == 10 and keyinput[pg.K_RCTRL]:
            self.s1 = True
            mainClass.alphaLeft()
            mainClass.alpha()
            if self.left is True:
                self.x -= 1

            if self.right is True:
                self.x += 1

        if self.s1Loop == 3:
            self.s1 = False
            self.s2 = True

            if self.left is True:
                self.x -= 1.5

            if self.right is True:
                self.x += 1.5

        if self.s2Loop == 3:
            self.s2 = False
            self.s1Loop = 0
            self.s2Loop = 0
            self.cd = 0
            mainClass.un_alpha()
            mainClass.un_alphaLeft()

    

        if self.s1 is True:
            self.s1Loop += 0.2
            if self.s1Loop >= 3:
                self.s1Loop = 3
                #self.s1 = False
        
        if self.s2 is True:
            self.s2Loop += 0.2
            if self.s2Loop >= 3:
                self.s2Loop = 3
                #self.s2 = False
        

        print(self.cd , self.cdBool)




#ENEMY AI +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


    def enemie(self):

        self.enemieRect1 = pg.draw.rect(window,(255,0,0) , (self.enemList[0],self.enemList[1] , 15,25))
        
        self.enemList[1] = playerRect.y


        if playerRect.x > self.enemieRect1.x + 10:
            self.enemList[0] += 1.5
            self.enemRight = True


        if playerRect.x < self.enemieRect1.x - 10:
            self.enemList[0] -= 1.5
            self.enemLeft = True

        if self.enemieRect1.colliderect(playerRect):
            self.enemLeft = False
            self.enemRight = False
            self.atk1 = True

        if self.atk1 is True and playerRect.x > self.enemieRect1.x:

            window.blit(engine.enemAtk1.list[int(self.enemAtkCount)], (self.enemList[0] -8 , self.enemList[1] -8))

            self.enemzsAtkCount += 0.2
    
            if self.enemAtkCount >= 4:
                self.enemAtkCount = 0
        

        if self.atk1 is True and playerRect.x < self.enemieRect1.x:

            window.blit(engine.enemAtk1.listLeft[int(self.enemAtkCount)], (self.enemList[0] -8 , self.enemList[1] -8))

            self.enemAtkCount += 0.2
    
            if self.enemAtkCount >= 4:
                self.enemAtkCount = 0


        if self.enemLeft is True:
            window.blit(engine.enemRun.listLeft[int(self.enemRun)],(self.enemList[0] -8 , self.enemList[1] -8))
            self.enemRight = False


        if self.enemRight is True:
            window.blit(engine.enemRun.list[int(self.enemRun)],(self.enemList[0] -8 , self.enemList[1] -8))
            self.enemLeft = False

        self.enemRun += 0.2
        if self.enemRun >= 2:
            self.enemRun = 0

        if self.enemLeft is True:
            self.atk1 = False
        if self.enemRight is True:
            self.atk1 = False



# PLAYER 2 CFLASS +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



class player2Mainclass():
    def __init__(self):

        self.x = random.randint(0,100)
        self.y = 150
        self.velY = 10
        self.velX = 10

        self.left = False
        self.right = True
        self.idleLeft = False
        self.idleRight = False
        self.jump = False



        self.runLoop = random.randint(0,1)
        self.s1Loop = 0
        self.s2Loop = 0
        self.s3Loop = 0

        self.s1 = False
        self.s2 = False
        self.s3 = False


        self.cd = 0
        self.cdBool = False




    def alpha2():

        engine.animateIdleG.list[0].set_alpha(0)
        engine.animateIdleG.list[1].set_alpha(0)     
        engine.animateIdleG.list[2].set_alpha(0)
        engine.animateIdleG.list[3].set_alpha(0)
    
    def un_alpha2():

        engine.animateIdleG.list[0].set_alpha()
        engine.animateIdleG.list[1].set_alpha()     
        engine.animateIdleG.list[2].set_alpha()
        engine.animateIdleG.list[3].set_alpha()

    def alphaLeft2():

        engine.animateIdleG.listLeft[0].set_alpha(0)
        engine.animateIdleG.listLeft[1].set_alpha(0)
        engine.animateIdleG.listLeft[2].set_alpha(0)
        engine.animateIdleG.listLeft[3].set_alpha(0)


    def un_alphaLeft2():

        engine.animateIdleG.listLeft[0].set_alpha()
        engine.animateIdleG.listLeft[1].set_alpha()
        engine.animateIdleG.listLeft[2].set_alpha()
        engine.animateIdleG.listLeft[3].set_alpha()     


    def playerRects(self):
        global playerRect2
        playerRect2 = pg.draw.rect(window ,(255,0,0) , (self.x + 8, self.y + 8 , 15 ,24 ),1)
        #self.enemRect = pg.draw.rect(window ,(255,0,0) , (self.x + 8, self.y + 8 , 15 ,24 ))


    def player(self):

        if self.s1Loop == 0 and self.right is True and keyinput[pg.K_d]:
            window.blit(engine.animateRunG.list[int(self.runLoop)] , (self.x , self.y))
            self.idleRight = False
            self.idleLeft = False

        else:
            self.idleRight = True


        if self.s1Loop == 0 and self.left is True and keyinput[pg.K_a]:
            window.blit(engine.animateRunG.listLeft[int(self.runLoop)] , (self.x , self.y))
            self.idleRight = False
            self.idleLeft = False
        else:
            self.idleLeft = True

  


        if self.right is True and self.idleRight is True:
            window.blit(engine.animateIdleG.list[int(self.runLoop)] , (self.x , self.y))


        if self.left is True and self.idleLeft is True:
            window.blit(engine.animateIdleG.listLeft[int(self.runLoop)] , (self.x , self.y))


        if self.left is True and self.right is False and self.s1 is True:
            window.blit(engine.animateAtk1G.listLeft[int(self.s1Loop)] , (self.x , self.y))


        if self.right is True and self.left is False and self.s1 is True:
            window.blit(engine.animateAtk1G.list[int(self.s1Loop)] , (self.x , self.y))



        if self.left is True and self.right is False and self.s2 is True:
            window.blit(engine.animateAtk2G.listLeft[int(self.s2Loop)] , (self.x , self.y))


        if self.right is True and self.left is False and self.s2 is True:
            window.blit(engine.animateAtk2G.list[int(self.s2Loop)] , (self.x , self.y))



    def input(self):

        if keyinput[pg.K_d]:
           self.moveX = True

           self.right = True
           self.left = False
           self.idleRight = True
           self.idleLeft = False
        else:
            self.moveX = False

        if keyinput[pg.K_a]:
            self.moveY = True

            self.left = True
            self.right = False
            self.idleLeft = True
            self.idleRight = False
        else:
            self.moveY = False
        

        if self.s1Loop == 0 and self.moveX is True:
            self.x += 3
        if self.s1Loop == 0 and self.moveY is True:
            self.x -= 3


        if keyinput[pg.K_w]:
            self.jump = True

        if self.jump is True:
            self.y -= self.velY
            self.velY -= 1

            if self.velY < -10:
                self.velY = 10
                self.jump = False





    def count(self):

        self.cd += 0.3
        if self.cd >= 10:
            self.cd = 10
            self.cdBool = True

        self.runLoop += 0.2
        if self.runLoop >= 2:
            self.runLoop = 0
        
        
        if self.cd == 10 and keyinput[pg.K_LCTRL]:
            self.s1 = True
            player2Mainclass.alphaLeft2()
            player2Mainclass.alpha2()
            if self.left is True:
                self.x -= 1

            if self.right is True:
                self.x += 1

        if self.s1Loop == 3:
            self.s1 = False
            self.s2 = True

            if self.left is True:
                self.x -= 1.5

            if self.right is True:
                self.x += 1.5

        if self.s2Loop == 3:
            self.s2 = False
            self.s1Loop = 0
            self.s2Loop = 0
            self.cd = 0
            player2Mainclass.un_alpha2()
            player2Mainclass.un_alphaLeft2()

    

        if self.s1 is True:
            self.s1Loop += 0.2
            if self.s1Loop >= 3:
                self.s1Loop = 3
                #self.s1 = False
        
        if self.s2 is True:
            self.s2Loop += 0.2
            if self.s2Loop >= 3:
                self.s2Loop = 3
                #self.s2 = False




# OTHER CLASS +++++++++++++++++++++++++++++++++




class classA():
    def __init__(self):
        self.hp = 200
        self.hp2 = 200
        self.left = True
        self.right = True

        self.left2 = True
        self.right2 = True


        self.groundCheck = 0
        self.actionBarhp = 200



    def collider(self):
        global rightRect
        global leftRect
        self.x = mainclass.x
        self.y = mainclass.y

        

        if keyinput[pg.K_LEFT]:
            self.left = True
            self.right = False
        if keyinput[pg.K_RIGHT]:
            self.right = True
            self.left = False




        if self.left is True:
            leftRect = pg.draw.rect(window , (0,0,255) , (self.x , self.y + 15 , 10 , 10),2)   
            
            if playerRect2.colliderect(leftRect):
                if mainclass.s1 == True:
                    self.hp2 -= 1
                if mainclass.s2 == True:
                    self.hp2 -= 1
                if mainclass.s3 == True:
                    self.hp2 -= 1


        if self.right is True:
            rightRect = pg.draw.rect(window , (0,0,255) , (self.x + 20, self.y + 15, 10 , 10),2)

            if playerRect2.colliderect(rightRect):
                if mainclass.s1 == True:
                    self.hp2 -= 1
                if mainclass.s2 == True:
                    self.hp2 -= 1
                if mainclass.s3 == True:
                     self.hp2 -= 1

        print("PLAYER 2 HP ", self.hp2)




    def collider2(self):
        global rightRect2
        global leftRect2

        self.x2 = mainclass2.x
        self.y2 = mainclass2.y
        

        if keyinput[pg.K_a]:
            self.left2 = True
            self.right2 = False
        if keyinput[pg.K_d]:
            self.right2 = True
            self.left2 = False


 
        if self.left2 is True:
            leftRect2 = pg.draw.rect(window , (0,0,255) , (self.x2 , self.y2 + 15 , 10 , 10),2)

            if playerRect.colliderect(leftRect2):
                if mainclass2.s1 == True:
                    self.hp -= 1
                    self.actionBarhp += 1
                if mainclass2.s2 == True:
                    self.hp -= 1
                    self.actionBarhp += 1
                if mainclass2.s3 == True:
                    self.hp -= 1
                    self.actionBarhp += 1 
        
        
        if self.right2 is True:
            rightRect2 = pg.draw.rect(window , (0,0,255) , (self.x2 + 20, self.y2 + 15, 10 , 10),2)
       

            if playerRect.colliderect(rightRect2):
                if mainclass2.s1 == True:
                    self.hp -= 1
                    self.actionBarhp += 1
                if mainclass2.s2 == True:
                    self.hp -= 1
                    self.actionBarhp += 1
                if mainclass2.s3 == True:
                    self.hp -= 1
                    self.actionBarhp += 1
        

        print("PLAYER HP ", self.hp)





    def act_A(self):
        global loop

  
        if self.hp <= 0:
            logs.write("Green               (Alpha V0.1.1)")
            logs.write("\n")
            os.startfile(r"data\inf2.bat")
            loop = False


        if self.hp2 <= 0:
            logs.write("Black               (Alpha V0.1.1)")
            logs.write("\n")
            os.startfile(r"data\inf.bat")
            loop = False




#border
        if mainclass.x >= width/2 -25:
            mainclass.x = width/2 -25


        if mainclass2.x >= width/2 -25:
            mainclass2.x = width/2 -25


        if mainclass.x <= -5:
            mainclass.x = -5

        
        if mainclass2.x <= -5:
            mainclass2.x = -5

#HEALT BAR

        pg.draw.rect(window,(255,255,255),(action.actionBarhp/2 +100,3,200/2,5))
        pg.draw.rect(window,(0,255,0),(0,3,action.hp2/2,5))





# VFX SFX ++++++++++++++++++++++++++


class sfx_vfx(classA):
    def __init__(self):
        self.PlaySound = False
        self.particle = []
        self.line = []
        self.x = 0
        self.y = 0

        self.orb = []




    def sfx(self):

        if mainclass.s1 == True and mainclass.s1Loop == 1:
            if not playerRect2.colliderect(leftRect):
                effect.sfx.swing.play()
        if mainclass.s2 == True and mainclass.s2Loop == 1:
            if not playerRect2.colliderect(leftRect):
                effect.sfx.swing.play()

        if mainclass.s1 == True and mainclass.s1Loop == 1:
            if not playerRect2.colliderect(rightRect):
                effect.sfx.swing.play()
        if mainclass.s2 == True and mainclass.s2Loop == 1:
            if not playerRect2.colliderect(rightRect):
                effect.sfx.swing.play()


        if mainclass.s1 == True and mainclass.s1Loop ==1:
            if playerRect2.colliderect(leftRect):
                effect.sfx.cut.play()

        if mainclass.s2 == True and mainclass.s2Loop ==1:
            if playerRect2.colliderect(leftRect):
                effect.sfx.cut.play()



        if mainclass.s1 == True and mainclass.s1Loop ==1:
            if playerRect2.colliderect(rightRect):
                effect.sfx.cut.play()

        if mainclass.s2 == True and mainclass.s2Loop ==1:
            if playerRect2.colliderect(rightRect):
                effect.sfx.cut.play()

#P2

        if mainclass2.s1 == True and mainclass2.s1Loop == 1:
            if not playerRect.colliderect(leftRect2):
                effect.sfx.swing.play()
        if mainclass2.s2 == True and mainclass2.s2Loop == 1:
            if not playerRect.colliderect(leftRect2):
                effect.sfx.swing.play()

        if mainclass2.s1 == True and mainclass2.s1Loop == 1:
            if not playerRect.colliderect(rightRect2):
                effect.sfx.swing.play()
        if mainclass2.s2 == True and mainclass2.s2Loop == 1:
            if not playerRect.colliderect(rightRect2):
                effect.sfx.swing.play()


        if mainclass2.s1 == True and mainclass2.s1Loop ==1:
            if playerRect.colliderect(leftRect2):
                effect.sfx.cut.play()

        if mainclass2.s2 == True and mainclass2.s2Loop ==1:
            if playerRect.colliderect(leftRect2):
                effect.sfx.cut.play()



        if mainclass2.s1 == True and mainclass2.s1Loop ==1:
            if playerRect.colliderect(rightRect2):
                effect.sfx.cut.play()

        if mainclass2.s2 == True and mainclass2.s2Loop ==1:
            if playerRect.colliderect(rightRect2):
                effect.sfx.cut.play()


    def effects(self):

        if leftRect.colliderect(playerRect2):
            if mainclass.s1 >= 1:
                self.particle.append([[mainclass2.x + 15 ,mainclass2.y +20] , [random.randint(0,20)/10 , -2 +1] , random.randint(1,3)])

                for particles in self.particle:
                    particles[0][0] += particles[1][0]
                    particles[0][1] += particles[1][1]
                    particles[2] -= 0.1
                    particles[1][1] += 0.2
                    pg.draw.circle(window,(255,0,0),([int(particles[0][0]), int(particles[0][1])]), int(particles[2]))


                    if particles[2] <= 0:
                        self.particle.remove(particles)


            if mainclass.s2 >=1:
                self.particle.append([[mainclass2.x + 15 ,mainclass2.y +20] , [random.randint(0,20)/10 , -3 +1] , random.randint(1,3)])

                for particles in self.particle:
                    particles[0][0] += particles[1][0]
                    particles[0][1] += particles[1][1]
                    particles[2] -= 0.1
                    particles[1][1] += 0.1
                    pg.draw.circle(window,(255,0,0),([int(particles[0][0]), int(particles[0][1])]), int(particles[2]))    


                    if particles[2] <= 0:
                        self.particle.remove(particles)



        if rightRect.colliderect(playerRect2):
            if mainclass.s1 >= 1:
                self.particle.append([[mainclass2.x + 15 ,mainclass2.y +20] , [random.randint(0,20)/10 , -2 +1] , random.randint(1,3)])

                for particles in self.particle:
                    particles[0][0] += particles[1][0]
                    particles[0][1] += particles[1][1]
                    particles[2] -= 0.1
                    particles[1][1] += 0.2
                    pg.draw.circle(window,(255,0,0),([int(particles[0][0]), int(particles[0][1])]), int(particles[2]))


                    if particles[2] <= 0:
                        self.particle.remove(particles)


            if mainclass.s2 >=1:
                self.particle.append([[mainclass2.x + 15 ,mainclass2.y +20] , [random.randint(0,20)/10 , -3 +1] , random.randint(1,3)])

                for particles in self.particle:
                    particles[0][0] += particles[1][0]
                    particles[0][1] += particles[1][1]
                    particles[2] -= 0.1
                    particles[1][1] += 0.1
                    pg.draw.circle(window,(255,0,0),([int(particles[0][0]), int(particles[0][1])]), int(particles[2]))   


                    if particles[2] <= 0:
                        self.particle.remove(particles)




        if leftRect2.colliderect(playerRect):
            if mainclass.s1 >= 1:
                self.particle.append([[mainclass.x + 15 ,mainclass.y +20] , [random.randint(0,20)/10 , -2 +1] , random.randint(1,3)])

                for particles in self.particle:
                    particles[0][0] += particles[1][0]
                    particles[0][1] += particles[1][1]
                    particles[2] -= 0.1
                    particles[1][1] += 0.2
                    pg.draw.circle(window,(255,0,0),([int(particles[0][0]), int(particles[0][1])]), int(particles[2]))


                    if particles[2] <= 0:
                        self.particle.remove(particles)

            if mainclass2.s2 >=1:
                self.particle.append([[mainclass.x + 15 ,mainclass.y +20] , [random.randint(0,20)/10 , -3 +1] , random.randint(1,3)])

                for particles in self.particle:
                    particles[0][0] += particles[1][0]
                    particles[0][1] += particles[1][1]
                    particles[2] -= 0.1
                    particles[1][1] += 0.1
                    pg.draw.circle(window,(255,0,0),([int(particles[0][0]), int(particles[0][1])]), int(particles[2]))    


                    if particles[2] <= 0:
                        self.particle.remove(particles)

        if rightRect2.colliderect(playerRect):
            if mainclass2.s1 >= 1:
                self.particle.append([[mainclass.x + 15 ,mainclass.y +20] , [random.randint(0,20)/10 , -2 +1] , random.randint(1,3)])

                for particles in self.particle:
                    particles[0][0] += particles[1][0]
                    particles[0][1] += particles[1][1]
                    particles[2] -= 0.1
                    particles[1][1] += 0.2
                    pg.draw.circle(window,(255,0,0),([int(particles[0][0]), int(particles[0][1])]), int(particles[2]))

                    if particles[2] <= 0:
                        self.particle.remove(particles)

            if mainclass2.s2 >=1:
                self.particle.append([[mainclass.x + 15 ,mainclass.y +20] , [random.randint(0,20)/10 , -3 +1] , random.randint(1,3)])

                for particles in self.particle:
                    particles[0][0] += particles[1][0]
                    particles[0][1] += particles[1][1]
                    particles[2] -= 0.1
                    particles[1][1] += 0.1
                    pg.draw.circle(window,(255,0,0),([int(particles[0][0]), int(particles[0][1])]), int(particles[2]))


                    if particles[2] <= 0:
                        self.particle.remove(particles)  



    def bg_effects(self):


        self.line.append([-250,0 ,10000,10000])


        for lines in self.line:
            lines[0] += 50
            lines[1] += random.randint(1,2)
            lines[1] -= random.randint(1,2)
            if lines[0] >= 300:
                self.line.remove(lines)

            pg.draw.line(window,(random.randint(0,255),random.randint(0,255),random.randint(0,255)), (lines[0],lines[1]) ,(lines[2],lines[3]))
            pg.draw.line(window,(random.randint(0,255),random.randint(0,255),random.randint(0,255)), (0,lines[1]+182),(300, lines[1]+182))



        self.orb.append([[-50,-100] , [random.randint(0,20)/5, +1] , random.randint(1,3)])

        for orb in self.orb:
            orb[0][0] += orb[1][0]
            orb[0][1] += orb[1][1]
            #orb[2] -= 0.1
            #orb[1][1] += 0.1


            fx = pg.draw.circle(window,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),([int(orb[0][0]), int(orb[0][1])]), int(orb[2]))

            if fx.y >= 300:
                self.orb.remove(orb)




action = classA()
fx = sfx_vfx()
mainclass = mainClass()
mainclass2 = player2Mainclass()



def on_loop(loop):

    surf = pg.transform.scale(window , (width,height))
    display.blit(surf , (0,0))
    pg.display.flip()
    clock.tick(60)



# MENUU ++++++++++++++++++++++++++




def menu():
    if keyinput[pg.K_ESCAPE]:
        pass


loop = True
while loop == True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            loop = False



    mainclass.input()
    mainclass2.playerRects()
    mainclass.playerRects()
    action.collider2()
    action.collider()
    window.fill((50,50,50))
    fx.bg_effects()
    #window.blit(bg1,(0,0))

    
    mainclass.player()

    mainclass.count()
#player 2 ++++

    mainclass2.player()
    mainclass2.input()
    mainclass2.count()



# Action ++++++++++++++++++
    
    
    action.act_A()
    fx.sfx()
    fx.effects()
    menu()

# AIBOT ++
    #mainclass.enemie()
    on_loop(loop)