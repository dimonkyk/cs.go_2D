from pygame import  display, event, Rect, draw, key, K_UP
import time, pygame
x=50
y=700
d=display.set_mode([1500,800])
ct=Rect(x,y,20,20)
t=Rect(1450,100,20,20)
p=None
p2=None
while 1==1:

    time.sleep(1/60)
    event.get()
    keys=key.get_pressed()
    #движение ct
    if keys[K_UP]:
        ct.y-=1
        y-=1
    if keys[pygame.K_DOWN]:
        ct.y+=1
        y+=1
    #движение t
    if keys[pygame.K_w]:
        t.y-=1
    if keys[pygame.K_s]:
        t.y+=1
    if keys[pygame.K_SPACE]:
        p = Rect(x, y, 3, 2)
    if keys[pygame.K_DELETE]:
        p2 = Rect(t.x,t.y,3,2)

    if  p!=None:
        p.x+=1
    if p2!=None:
        p2.x-=1
    #отрисовка кадра
    d.fill([255,153,0])
    if p!=None:
        draw.rect(d, [0, 0, 0], p)
    if p2!=None:
        draw.rect(d,[0,0,0],p2)
    draw.rect(d, [0, 50, 180], t)
    draw.rect(d,[0,255,40],ct)
    display.flip()