import tkinter
import math
    
def btn_click():
    #テキスト取得
    a11=int(shiki11.get())
    a12=int(shiki12.get())
    a21=int(shiki21.get())
    a22=int(shiki22.get())
    an1=int(ans1.get())
    an2=int(ans2.get())
    
    #計算式
    anserx.insert(0,((an1*a22)-(a12*an2))/((a11*a22)-(a12*a21)))
    bunanserx.insert(0,((an1*a22)-(a12*an2))/((a11*a22)-(a12*a21)))
    
    ansery.insert(0,((a11*an2)-(an1*a21))/((a11*a22)-(a12*a21)))
    bunansery.insert(0,((a11*an2)-(an1*a21))/((a11*a22)-(a12*a21)))
    
    #右側のテキストボックスに取得した数字をセット
    bunshix11.insert(0,an1)
    bunshix12.insert(0,a12)
    bunshix21.insert(0,an2)
    bunshix22.insert(0,a22)
    bunbox11.insert(0,a11)
    bunbox12.insert(0,a12)
    bunbox21.insert(0,a21)
    bunbox22.insert(0,a22)
    bunshiy11.insert(0,a11)
    bunshiy12.insert(0,an1)
    bunshiy21.insert(0,a21)
    bunshiy22.insert(0,an2)
    bunboy11.insert(0,a11)
    bunboy12.insert(0,a12)
    bunboy21.insert(0,a21)
    bunboy22.insert(0,a22)
    
    #計算する前に前回の値を初期化

    bunshix11.delete(0,'end')
    bunshix11.insert(0,an1)

    bunshix12.delete(0,'end')
    bunshix12.insert(0,a12)

    bunshix21.delete(0,'end')
    bunshix21.insert(0,an2)

    bunshix22.delete(0,'end')
    bunshix22.insert(0,a22)

    bunbox11.delete(0,'end')
    bunbox11.insert(0,a11)

    bunbox12.delete(0,'end')
    bunbox12.insert(0,a12)

    bunbox21.delete(0,'end')
    bunbox21.insert(0,a21)

    bunbox22.delete(0,'end')
    bunbox22.insert(0,a22)

    bunshiy11.delete(0,'end')
    bunshiy11.insert(0,a11)

    bunshiy12.delete(0,'end')
    bunshiy12.insert(0,an1)

    bunshiy21.delete(0,'end')
    bunshiy21.insert(0,a21)

    bunshiy22.delete(0,'end')
    bunshiy22.insert(0,an2)

    bunboy11.delete(0,'end')
    bunboy11.insert(0,a11)

    bunboy12.delete(0,'end')
    bunboy12.insert(0,a12)

    bunboy21.delete(0,'end')
    bunboy21.insert(0,a21)

    bunboy22.delete(0,'end')
    bunboy22.insert(0,a22)

    anserx.delete(0,'end')
    anserx.insert(0,((an1*a22)-(a12*an2))/((a11*a22)-(a12*a21)))

    bunanserx.delete(0,'end')
    bunanserx.insert(0,((an1*a22)-(a12*an2))/((a11*a22)-(a12*a21)))
    
    ansery.delete(0,'end')
    ansery.insert(0,((a11*an2)-(an1*a21))/((a11*a22)-(a12*a21)))

    bunansery.delete(0,'end')
    bunansery.insert(0,((a11*an2)-(an1*a21))/((a11*a22)-(a12*a21)))
    



#画面作成
tki=tkinter.Tk()
tki.geometry('450x200')
tki.title('クラメルの公式を用いて連立方程式を解こう')
tki.resizable(width=0,height=0)
#ラベル
shiki1=tkinter.Label(text='x+         y=')
shiki1.place(x=60,y=40)
shiki2=tkinter.Label(text='x+         y=')
shiki2.place(x=60,y=70)
anserx=tkinter.Label(text='x=')
anserx.place(x=35,y=140)
ansery=tkinter.Label(text='y=')
ansery.place(x=100,y=140)

bunsenx=tkinter.Label(text='x=—————=')
bunsenx.place(x=180,y=70)
bunsenx=tkinter.Label(text='y=—————=')
bunsenx.place(x=300,y=70)
#テキストボックス生成

#入力側のテキストボックス
shiki11=tkinter.Entry(width=3)
shiki11.place(x=37,y=40)
shiki12=tkinter.Entry(width=3)
shiki12.place(x=77,y=40)
shiki21=tkinter.Entry(width=3)
shiki21.place(x=37,y=70)
shiki22=tkinter.Entry(width=3)
shiki22.place(x=77,y=70)

#入力側の答え
ans1=tkinter.Entry(width=3)
ans1.place(x=120,y=40)
ans2=tkinter.Entry(width=3)
ans2.place(x=120,y=70)

#計算ボタンを押した際に出る答えのテキストボックス
anserx=tkinter.Entry(width=4)
anserx.place(x=55,y=140)
ansery=tkinter.Entry(width=4)
ansery.place(x=120,y=140)

#右側のクラメルの公式のxの分子テキストボックス
bunshix11=tkinter.Entry(width=3)
bunshix11.place(x=200,y=35)
bunshix12=tkinter.Entry(width=3)
bunshix12.place(x=230,y=35)
bunshix21=tkinter.Entry(width=3)
bunshix21.place(x=200,y=58)
bunshix22=tkinter.Entry(width=3)
bunshix22.place(x=230,y=58)

#右側のクラメルの公式のxの分母テキストボックス
bunbox11=tkinter.Entry(width=3)
bunbox11.place(x=200,y=85)
bunbox12=tkinter.Entry(width=3)
bunbox12.place(x=230,y=85)
bunbox21=tkinter.Entry(width=3)
bunbox21.place(x=200,y=108)
bunbox22=tkinter.Entry(width=3)
bunbox22.place(x=230,y=108)

#右側のクラメルの公式のxの答えテキストボックス
bunanserx=tkinter.Entry(width=4)
bunanserx.place(x=270,y=70)

#右側のクラメルの公式のyの分子テキストボックス
bunshiy11=tkinter.Entry(width=3)
bunshiy11.place(x=322,y=35)
bunshiy12=tkinter.Entry(width=3)
bunshiy12.place(x=352,y=35)
bunshiy21=tkinter.Entry(width=3)
bunshiy21.place(x=322,y=58)
bunshiy22=tkinter.Entry(width=3)
bunshiy22.place(x=352,y=58)

#右側のクラメルの公式のyの分母テキストボックス
bunboy11=tkinter.Entry(width=3)
bunboy11.place(x=322,y=85)
bunboy12=tkinter.Entry(width=3)
bunboy12.place(x=352,y=85)
bunboy21=tkinter.Entry(width=3)
bunboy21.place(x=322,y=108)
bunboy22=tkinter.Entry(width=3)
bunboy22.place(x=352,y=108)

#右側のクラメルの公式のyの答えテキストボックス
bunansery=tkinter.Entry(width=4)
bunansery.place(x=392,y=70)

#ボタン生成
btn=tkinter.Button(tki,text='計算',command=btn_click)
btn.place(x=65,y=100)

#画面をそのまま表示
tki.mainloop()
