import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")  # 背景画像のSurface
    bg_img2 = pg.transform.flip(bg_img, True, False)  # 背景画像を反転
    kk_img = pg.image.load("fig/3.png")  # こうかとん画像のSurface
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rct = kk_img.get_rect()  # こうかとん画像のRect
    kk_rct.center = 300, 200  # こうかとん画像の中心座標を設定
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()  # キーの押下状態を取得
        if key_lst[pg.K_UP]:  # 上キーが押されたら
            kk_rct.move_ip(0, -1)  # 上に移動
        if key_lst[pg.K_DOWN]:
            kk_rct.move_ip(0, +1)
        if key_lst[pg.K_LEFT]:
            kk_rct.move_ip(-1, 0)
        if key_lst[pg.K_RIGHT]:
            kk_rct.move_ip(+1, 0)

        x = tmr%3200
        screen.blit(bg_img, [-x, 0])  # 1枚目
        screen.blit(bg_img2, [-x+1600, 0])  # 2枚目
        screen.blit(bg_img, [-x+3200, 0])  # 3枚目
        # screen.blit(kk_img, [300, 200])
        screen.blit(kk_img, kk_rct)
        pg.display.update()
        # print(tmr, x)
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()