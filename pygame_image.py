import os #ライブラリ読み込み
import sys
import pygame as pg #pygame

os.chdir(os.path.dirname(os.path.abspath(__file__)))#このファイルの位置を作業ディレクトリにする


def main():#メイン関数の定義
    pg.display.set_caption("はばたけ！こうかとん")#set_caption関数で画面のタイトルを設定する、引数が文字列
    screen = pg.display.set_mode((800, 600))#set_mode関数でsurfaceインスタンス生成,引数は幅と高さのタプル(800ピクセル,600ピクセル),戻り値が画面surface
    clock  = pg.time.Clock()#timeモジュールのclockクラス。clockという時間計測用オブジェクトを生成する。
    bg_img = pg.image.load("fig/pg_bg.jpg")  # imageモジュールのload関数でパスファイルを引数に、戻り値＝画像surfaceの生成。背景画像のSurface、bg_imgの作成　
    bg_img2 = pg.transform.flip(bg_img, True, False)  # #transformモジュールのflip関数で、上下左右の反転。左右反転boolをtrueにして背景画像を左右反転
    kk_img = pg.image.load("fig/3.png")  # こうかとん画像のSurface
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rct = kk_img.get_rect()  # こうかとん画像のRect、get_rectメソッドでkk.imgの範囲を取得して、kk_rctとして残す
    kk_rct.center = 300, 200  # こうかとん画像の中心座標を設定
    tmr = 0#フレーム用変数の初期化
    while True:
        for event in pg.event.get():#eventモジュールの、get関数。イベントキューから取得したすべてのイベント情報をeventインスタンスが並んだeventリストに返す。
            #イベントはキー入力やマウスクリックなどのこと。発生した順にキューに入る。getで取得したeventインスタンスはリストに入ったら、キューから削除される。
            if event.type == pg.QUIT: 
                return#eventモジュールのtype属性。イベントの種類を表すインスタンス変数。quitはxボタンのクリックのこと。そのあとリターン
        key_lst = pg.key.get_pressed()  #keyモジュールのget_pressed関数で キーの押下状態を取得しリストを作る。
        if key_lst[pg.K_UP]:  # keyも樹0ルのget_pressedで作ったリストのインデックス、キーボード定数で,キーボードの上キーが押下を取得。boolで返す。
            kk_rct.move_ip(0, -1)  # 上に移動、rectクラスのインスタンスをmove_ipメソッドで横と縦の速度を指定して動かす。
        if key_lst[pg.K_DOWN]:
            kk_rct.move_ip(0, +1)#下に移動。左上に原点があるから、yが+されると下にピクセルの位置が下がる。
        if key_lst[pg.K_LEFT]:
            kk_rct.move_ip(-1, 0)#左に移動。
        if key_lst[pg.K_RIGHT]:
            kk_rct.move_ip(+1, 0)#右に移動。

        x = tmr%3200#フレーム数(ループの回数)、%3200で3200を超えたときに、0に戻らせ、ループさせる。
        screen.blit(bg_img, [-x, 0])  # 1枚目　blitメソッドでsurfaceを別のsurfaceに貼り付ける。引数1は別のsurfaceインスタンス、引数2は位置座標を表すリストやタプル(Rectインスタンス)
        #-x(フレームごとに左に動かす。)背景を動かすことで、こうかとんが動いているように見える。
        screen.blit(bg_img2, [-x+1600, 0])  # 2枚目　1枚目の右に続く反転画像
        screen.blit(bg_img, [-x+3200, 0])  # 3枚目 さらにその右に続く3枚目　ループ用。
        # screen.blit(kk_img, [300, 200])
        screen.blit(kk_img, kk_rct)#kk_imgをscreenのkk_rct座標に貼り付け。
        pg.display.update()#update関数で画面の更新
        # print(tmr, x)
        tmr += 1    #ループの回数を毎回+1増やす    
        clock.tick(200)#tickメソッドを使えば、指定したフレーム分の遅延を発生できる。


if __name__ == "__main__":#importではなく、直接実行の際に、メイン処理を走らせる。
    pg.init()#pygameモジュールの初期化
    main()#main処理
    pg.quit()#pygameモジュールの初期化を解除
    sys.exit()#プログラムの終了、pg.quit,sys.exitはなくても動くが正常終了か異常終了かわかりやすくなる。