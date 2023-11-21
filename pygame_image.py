import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    ch_img = pg.image.load("ex01/fig/3.png")
    ch_img = pg.transform.flip(ch_img, True, False)
    tmr = 0
    x=0
    ch_images=[ch_img,pg.transform.rotate(ch_img,10)]
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x=tmr%1600
        screen.blit(bg_img, [-x, 0])
        screen.blit(ch_images[tmr%2], [300, 300])
        print(tmr)
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()