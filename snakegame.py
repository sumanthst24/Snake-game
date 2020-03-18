import pygame,sys,random

from pygame.locals import *

redColor=pygame.Color(255,0,0)

blackColor=pygame.Color(0,0,0)

whiteColor=pygame.Color(255,255,255)


def getResult(score):
        pygame.init()
        pygame.font.init()
        font=pygame.font.SysFont(None,20)
        text1='Game over'
        text2='Your final score '+str(score)
        fontText1=pygame.font.SysFont(None,60)
        fontText2=pygame.font.SysFont(None,38)
        renderText1=font.render(text1,1,(255,255,255))
        renderText2=font.render(text2,1,(255,255,255))
        gameSurface=pygame.display.set_mode((640,500))
        gameSurface.blit(renderText1,[60,100])
        gameSurface.blit(renderText2,[20,125])
        pygame.display.update()

def gameover(score):
    getResult(score)
    pygame.quit()
    sys.exit()



def main():
                pygame.init()
                pygame.font.init()
                font=pygame.font.SysFont(None,20)
                fpstime=pygame.time.Clock()
                gameSurface=pygame.display.set_mode((640,500))
                pygame.display.set_caption('Snake Hunt')
                snakePosition=[140,100]
                snakeBody=[[140,100],[120,100],[100,100]]
                foodPosition=[300,300]
                foodFlag=1
                direction='right'
                changeDirection=direction
                score=0

                while (True):
                        for event in pygame.event.get():
                                if(event.type==QUIT):
                                        pygame.quit()
                                        sys.exit()
                                elif (event.type==KEYDOWN):
                                        if (event.key==K_RIGHT):
                                                changeDirection='right'
                                        if (event.key==K_LEFT):
                                                changeDirection='left'
                                        if (event.key==K_UP):
                                                changeDirection='up'
                                        if (event.key==K_DOWN):
                                                changeDirection='down'
                                        if(event.type==K_ESCAPE):
                                                pygame.event.post(pygame.event.Event(QUIT))

                        if changeDirection=='right' and not direction=='left':
                                direction=changeDirection
                        if changeDirection=='left' and not direction=='right':
                                direction=changeDirection
                        if changeDirection=='up' and not direction=='down':
                                direction=changeDirection
                        if changeDirection=='down' and not direction=='up':
                                direction=changeDirection

                        if direction=='right':
                                snakePosition[0]=snakePosition[0]+20
                        if direction=='left':
                                snakePosition[0]=snakePosition[0]-20
                        if direction=='up':
                                snakePosition[1]=snakePosition[1]-20
                        if direction=='down':
                                snakePosition[1]=snakePosition[1]+20

                        snakeBody.insert(0,list(snakePosition))
                        if(snakePosition[0]==foodPosition[0] and foodPosition[1]==snakePosition[1]):
                                score=score+1
                                foodFlag=0
                        else:
                                snakeBody.pop()

                        if(foodFlag==0):
                                x=random.randrange(1,32)
                                y=random.randrange(1,24)
                                foodPosition=[int(x)*20,int(y)*20]
                                foodFlag=1


                        gameSurface.fill(blackColor)
                        for position in snakeBody:
                                pygame.draw.rect(gameSurface,whiteColor,Rect(position[0],position[1],20,20))

                        pygame.draw.rect(gameSurface,redColor,Rect(foodPosition[0],foodPosition[1],20,20))
                        gameSurface.blit(font.render('Your score '+str(score),1,(255,255,255)),(0,480))
                        pygame.display.flip()
                        fpstime.tick(5)

                        if(snakePosition[0]>620 or snakePosition[0]<0):
                            gameover(score)
                        elif(snakePosition[1]>460 or snakePosition[1]<0):
                            gameover(score)
                



main()
