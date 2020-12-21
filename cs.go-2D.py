from pygame import  display, event, Rect, draw, key, K_UP
import time, pygame
d=display.set_mode([1500,800])
ct=Rect(50,700,20,20)
t=Rect(1450,100,20,20)

while 1==1:
    time.sleep(1/60)
    event.get()
    keys=key.get_pressed()
    #движение ct
    if keys[K_UP]:
        ct.y-=1
    if keys[pygame.K_DOWN]:
        ct.y+=1
    #движение t
    if keys[pygame.K_w]:
        t.y-=1
    if keys[pygame.K_s]:
        t.y+=1
    if keys[pygame.K_SPACE]:

    #отрисовка кадра
    d.fill([255,153,0])
    draw.rect(d, [0, 50, 180], t)
    draw.rect(d,[0,255,40],ct)
    display.flip()