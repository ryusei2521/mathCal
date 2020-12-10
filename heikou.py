import tkinter
import math
    
def btn_click():
    #テキスト取得
    a11=int(Aa.get())
    a12=int(Ab.get())
    a13=int(Ac.get())
    b11=int(Ba.get())
    b12=int(Bb.get())
    b13=int(Bc.get())
    c11=int(Ca.get())
    c12=int(Cb.get())
    c13=int(Cc.get())
    
    
    AA=(a11*b12*c13)
    AB=(b11*c12*a13)
    AC=(c11*a12*b13)

    BA=(c11*b12*a13)
    BB=(b11*a12*c13)
    BC=(a11*c12*b13)
    
    #計算式
    taianser.insert(0,((AA+AB+AC)-(BA+BB+BC)))

    #計算する前に値を初期化
    taianser.delete(0,'end')
    taianser.insert(0,((AA+AB+AC)-(BA+BB+BC)))

#画面作成
tki=tkinter.Tk()
tki.geometry('180x200')
tki.title('クラメルの公式を用いて連立方程式を解こう')
tki.resizable(width=0,height=0)
#ラベル
Akakko=tkinter.Label(text='A(         ,         ,        )')
Akakko.place(x=30,y=40)
Bkakko=tkinter.Label(text='B(         ,         ,        )')
Bkakko.place(x=30,y=70)
Bkakko=tkinter.Label(text='C(         ,         ,        )')
Bkakko.place(x=30,y=100)


taianser=tkinter.Label(text='体積は     　   です。')
taianser.place(x=30,y=160)

#テキストボックス生成

#Aのテキストボックス
Aa=tkinter.Entry(width=3)
Aa.place(x=47,y=40)
Ab=tkinter.Entry(width=3)
Ab.place(x=77,y=40)
Ac=tkinter.Entry(width=3)
Ac.place(x=105,y=40)

#Bのテキストボックス
Ba=tkinter.Entry(width=3)
Ba.place(x=47,y=70)
Bb=tkinter.Entry(width=3)
Bb.place(x=77,y=70)
Bc=tkinter.Entry(width=3)
Bc.place(x=105,y=70)

#Cのテキストボックス
Ca=tkinter.Entry(width=3)
Ca.place(x=47,y=100)
Cb=tkinter.Entry(width=3)
Cb.place(x=77,y=100)
Cc=tkinter.Entry(width=3)
Cc.place(x=105,y=100)

#体積の答えテキストボックス
taianser=tkinter.Entry(width=4)
taianser.place(x=70,y=160)

#ボタン生成
btn=tkinter.Button(tki,text='計算',command=btn_click)
btn.place(x=65,y=130)

#画面をそのまま表示
tki.mainloop()
