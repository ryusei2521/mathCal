import tkinter
import math
global btn_click

def btn_click():
    #テキスト取得
    a11=int(shiki11.get())
    a12=int(shiki12.get())
    a13=int(shiki13.get())
    a21=int(shiki21.get())
    a22=int(shiki22.get())
    a23=int(shiki23.get())
    a31=int(shiki31.get())
    a32=int(shiki32.get())
    a33=int(shiki33.get())
    an1=int(ans1.get())
    an2=int(ans2.get())
    an3=int(ans3.get())

    #xの分子
    Aa=(an1*a22*a33)
    Ab=(a12*a23*an3)
    Ac=(a13*an2*a32)

    Ba=(a13*a22*an3)
    Bb=(a12*an2*a33)
    Bc=(an1*a23*a32)

    #yの分子
    Ca=(a11*an2*a33)
    Cb=(an1*a23*a31)
    Cc=(a13*a21*an3)

    Da=(a13*an2*a31)
    Db=(an1*a21*a33)
    Dc=(a11*a23*an3)

    #zの分子
    Ea=(a11*a22*an3)
    Eb=(a12*an2*a31)
    Ec=(an1*a21*a32)

    Fa=(an1*a22*a31)
    Fb=(a12*a21*an3)
    Fc=(a11*an2*a32)

    #分母
    AA=(a11*a22*a33)
    AB=(a12*a23*a31)
    AC=(a13*a21*a32)

    BA=(a13*a22*a31)
    BB=(a12*a21*a33)
    BC=(a11*a23*a32)




    #計算式
    anserx.insert(0,(((Aa+Ab+Ac)-(Ba+Bb+Bc))/((AA+AB+AC)-(BA+BB+BC))))
    bunanserx.insert(0,(((Aa+Ab+Ac)-(Ba+Bb+Bc))/((AA+AB+AC)-(BA+BB+BC))))

    ansery.insert(0,(((Ca+Cb+Cc)-(Da+Db+Dc))/((AA+AB+AC)-(BA+BB+BC))))
    bunansery.insert(0,(((Ca+Cb+Cc)-(Da+Db+Dc))/((AA+AB+AC)-(BA+BB+BC))))

    anserz.insert(0,(((Ea+Eb+Ec)-(Fa+Fb+Fc))/((AA+AB+AC)-(BA+BB+BC))))
    bunanserz.insert(0,(((Ea+Eb+Ec)-(Fa+Fb+Fc))/((AA+AB+AC)-(BA+BB+BC))))

    
    
    #右側のテキストボックスに取得した数字をセット
    bunshix11.insert(0,an1)
    bunshix12.insert(0,a12)
    bunshix13.insert(0,a13)
    bunshix21.insert(0,an2)
    bunshix22.insert(0,a22)
    bunshix23.insert(0,a23)
    bunshix31.insert(0,an3)
    bunshix32.insert(0,a32)
    bunshix33.insert(0,a33)
    bunbox11.insert(0,a11)
    bunbox12.insert(0,a12)
    bunbox13.insert(0,a13)
    bunbox21.insert(0,a21)
    bunbox22.insert(0,a22)
    bunbox23.insert(0,a23)
    bunbox31.insert(0,a31)
    bunbox32.insert(0,a32)
    bunbox33.insert(0,a33)
    bunshiy11.insert(0,a11)
    bunshiy12.insert(0,an1)
    bunshiy13.insert(0,a13)
    bunshiy21.insert(0,a21)
    bunshiy22.insert(0,an2)
    bunshiy23.insert(0,a23)
    bunshiy31.insert(0,a31)
    bunshiy32.insert(0,an3)
    bunshiy33.insert(0,a33)
    bunboy11.insert(0,a11)
    bunboy12.insert(0,a12)
    bunboy13.insert(0,a13)
    bunboy21.insert(0,a21)
    bunboy22.insert(0,a22)
    bunboy23.insert(0,a23)
    bunboy31.insert(0,a31)
    bunboy32.insert(0,a32)
    bunboy33.insert(0,a33)

    bunshiz11.insert(0,a11)
    bunshiz12.insert(0,a12)
    bunshiz13.insert(0,an1)
    bunshiz21.insert(0,a21)
    bunshiz22.insert(0,a21)
    bunshiz23.insert(0,an2)
    bunshiz31.insert(0,a31)
    bunshiz32.insert(0,a31)
    bunshiz33.insert(0,a32)
    bunboz11.insert(0,an3)
    bunboz12.insert(0,a12)
    bunboz13.insert(0,a13)
    bunboz21.insert(0,a21)
    bunboz22.insert(0,a22)
    bunboz23.insert(0,a23)
    bunboz31.insert(0,a31)
    bunboz32.insert(0,a32)
    bunboz33.insert(0,a33)
    
    #計算する前に前回の値を初期化

    #x
    bunshix11.delete(0,'end')
    bunshix11.insert(0,an1)
    bunshix12.delete(0,'end')
    bunshix12.insert(0,a12)
    bunshix13.delete(0,'end')
    bunshix13.insert(0,a13)

    bunshix21.delete(0,'end')
    bunshix21.insert(0,an2)
    bunshix22.delete(0,'end')
    bunshix22.insert(0,a22)
    bunshix23.delete(0,'end')
    bunshix23.insert(0,a23)

    bunshix31.delete(0,'end')
    bunshix31.insert(0,an3)
    bunshix32.delete(0,'end')
    bunshix32.insert(0,a32)
    bunshix33.delete(0,'end')
    bunshix33.insert(0,a33)

    bunbox11.delete(0,'end')
    bunbox11.insert(0,a11)
    bunbox12.delete(0,'end')
    bunbox12.insert(0,a12)
    bunbox13.delete(0,'end')
    bunbox13.insert(0,a13)

    bunbox21.delete(0,'end')
    bunbox21.insert(0,a21)
    bunbox22.delete(0,'end')
    bunbox22.insert(0,a22)
    bunbox23.delete(0,'end')
    bunbox23.insert(0,a23)

    bunbox31.delete(0,'end')
    bunbox31.insert(0,a31)
    bunbox32.delete(0,'end')
    bunbox32.insert(0,a32)
    bunbox33.delete(0,'end')
    bunbox33.insert(0,a33)

    #y
    bunshiy11.delete(0,'end')
    bunshiy11.insert(0,a11)
    bunshiy12.delete(0,'end')
    bunshiy12.insert(0,an1)
    bunshiy13.delete(0,'end')
    bunshiy13.insert(0,a13)

    bunshiy21.delete(0,'end')
    bunshiy21.insert(0,a21)
    bunshiy22.delete(0,'end')
    bunshiy22.insert(0,an2)
    bunshiy23.delete(0,'end')
    bunshiy23.insert(0,a23)

    bunshiy31.delete(0,'end')
    bunshiy31.insert(0,a31)
    bunshiy32.delete(0,'end')
    bunshiy32.insert(0,an3)
    bunshiy33.delete(0,'end')
    bunshiy33.insert(0,a33)

    bunboy11.delete(0,'end')
    bunboy11.insert(0,a11)
    bunboy12.delete(0,'end')
    bunboy12.insert(0,a12)
    bunboy13.delete(0,'end')
    bunboy13.insert(0,a13)

    bunboy21.delete(0,'end')
    bunboy21.insert(0,a21)
    bunboy22.delete(0,'end')
    bunboy22.insert(0,a22)
    bunboy23.delete(0,'end')
    bunboy23.insert(0,a23)

    bunboy31.delete(0,'end')
    bunboy31.insert(0,a31)
    bunboy32.delete(0,'end')
    bunboy32.insert(0,a32)
    bunboy33.delete(0,'end')
    bunboy33.insert(0,a33)

    #z
    bunshiz11.delete(0,'end')
    bunshiz11.insert(0,a11)
    bunshiz12.delete(0,'end')
    bunshiz12.insert(0,a12)
    bunshiz13.delete(0,'end')
    bunshiz13.insert(0,an3)

    bunshiz21.delete(0,'end')
    bunshiz21.insert(0,a21)
    bunshiz22.delete(0,'end')
    bunshiz22.insert(0,a22)
    bunshiz23.delete(0,'end')
    bunshiz23.insert(0,an2)

    bunshiz31.delete(0,'end')
    bunshiz31.insert(0,a31)
    bunshiz32.delete(0,'end')
    bunshiz32.insert(0,a32)
    bunshiz33.delete(0,'end')
    bunshiz33.insert(0,an3)

    bunboz11.delete(0,'end')
    bunboz11.insert(0,a11)
    bunboz12.delete(0,'end')
    bunboz12.insert(0,a12)
    bunboz13.delete(0,'end')
    bunboz13.insert(0,a13)

    bunboz21.delete(0,'end')
    bunboz21.insert(0,a21)
    bunboz22.delete(0,'end')
    bunboz22.insert(0,a22)
    bunboz23.delete(0,'end')
    bunboz23.insert(0,a23)

    bunboz31.delete(0,'end')
    bunboz31.insert(0,a31)
    bunboz32.delete(0,'end')
    bunboz32.insert(0,a32)
    bunboz33.delete(0,'end')
    bunboz33.insert(0,a33)

#画面作成
tki=tkinter.Tk()
tki.geometry('670x250')
tki.title('クラメルの公式を用いて連立方程式を解こう')
tki.resizable(width=0,height=0)
#ラベル
shiki1=tkinter.Label(text='x+         y+        z=')
shiki1.place(x=60,y=40)
shiki2=tkinter.Label(text='x+         y+        z=')
shiki2.place(x=60,y=70)
shiki3=tkinter.Label(text='x+         y+        z=')
shiki3.place(x=60,y=100)
anserx=tkinter.Label(text='x=')
anserx.place(x=15,y=160)
ansery=tkinter.Label(text='y=')
ansery.place(x=70,y=160)
anserz=tkinter.Label(text='z=')
anserz.place(x=125,y=160)

bunsenx=tkinter.Label(text='x=————————=')
bunsenx.place(x=180,y=93)
bunsenx=tkinter.Label(text='y=————————=')
bunsenx.place(x=335,y=93)
bunsenx=tkinter.Label(text='z=————————=')
bunsenx.place(x=490,y=93)
#テキストボックス生成

#入力側のテキストボックス
shiki11=tkinter.Entry(width=3)
shiki11.place(x=37,y=40)
shiki12=tkinter.Entry(width=3)
shiki12.place(x=77,y=40)
shiki13=tkinter.Entry(width=3)
shiki13.place(x=117,y=40)
shiki21=tkinter.Entry(width=3)
shiki21.place(x=37,y=70)
shiki22=tkinter.Entry(width=3)
shiki22.place(x=77,y=70)
shiki23=tkinter.Entry(width=3)
shiki23.place(x=117,y=70)
shiki31=tkinter.Entry(width=3)
shiki31.place(x=37,y=100)
shiki32=tkinter.Entry(width=3)
shiki32.place(x=77,y=100)
shiki33=tkinter.Entry(width=3)
shiki33.place(x=117,y=100)

#入力側の答え
ans1=tkinter.Entry(width=3)
ans1.place(x=158,y=40)
ans2=tkinter.Entry(width=3)
ans2.place(x=158,y=70)
ans3=tkinter.Entry(width=3)
ans3.place(x=158,y=100)

#計算ボタンを押した際に出る答えのテキストボックス
anserx=tkinter.Entry(width=4)
anserx.place(x=35,y=160)
ansery=tkinter.Entry(width=4)
ansery.place(x=90,y=160)
anserz=tkinter.Entry(width=4)
anserz.place(x=145,y=160)

#右側のクラメルの公式のxの分子テキストボックス
bunshix11=tkinter.Entry(width=3)
bunshix11.place(x=200,y=35)
bunshix12=tkinter.Entry(width=3)
bunshix12.place(x=230,y=35)
bunshix13=tkinter.Entry(width=3)
bunshix13.place(x=260,y=35)
bunshix21=tkinter.Entry(width=3)
bunshix21.place(x=200,y=58)
bunshix22=tkinter.Entry(width=3)
bunshix22.place(x=230,y=58)
bunshix23=tkinter.Entry(width=3)
bunshix23.place(x=260,y=58)
bunshix31=tkinter.Entry(width=3)
bunshix31.place(x=200,y=81)
bunshix32=tkinter.Entry(width=3)
bunshix32.place(x=230,y=81)
bunshix33=tkinter.Entry(width=3)
bunshix33.place(x=260,y=81)

#右側のクラメルの公式のxの分母テキストボックス
bunbox11=tkinter.Entry(width=3)
bunbox11.place(x=200,y=108)
bunbox12=tkinter.Entry(width=3)
bunbox12.place(x=230,y=108)
bunbox13=tkinter.Entry(width=3)
bunbox13.place(x=260,y=108)
bunbox21=tkinter.Entry(width=3)
bunbox21.place(x=200,y=131)
bunbox22=tkinter.Entry(width=3)
bunbox22.place(x=230,y=131)
bunbox23=tkinter.Entry(width=3)
bunbox23.place(x=260,y=131)
bunbox31=tkinter.Entry(width=3)
bunbox31.place(x=200,y=154)
bunbox32=tkinter.Entry(width=3)
bunbox32.place(x=230,y=154)
bunbox33=tkinter.Entry(width=3)
bunbox33.place(x=260,y=154)

#右側のクラメルの公式のxの答えテキストボックス
bunanserx=tkinter.Entry(width=4)
bunanserx.place(x=303,y=93)

#右側のクラメルの公式のyの分子テキストボックス
bunshiy11=tkinter.Entry(width=3)
bunshiy11.place(x=360,y=35)
bunshiy12=tkinter.Entry(width=3)
bunshiy12.place(x=390,y=35)
bunshiy13=tkinter.Entry(width=3)
bunshiy13.place(x=420,y=35)
bunshiy21=tkinter.Entry(width=3)
bunshiy21.place(x=360,y=58)
bunshiy22=tkinter.Entry(width=3)
bunshiy22.place(x=390,y=58)
bunshiy23=tkinter.Entry(width=3)
bunshiy23.place(x=420,y=58)
bunshiy31=tkinter.Entry(width=3)
bunshiy31.place(x=360,y=81)
bunshiy32=tkinter.Entry(width=3)
bunshiy32.place(x=390,y=81)
bunshiy33=tkinter.Entry(width=3)
bunshiy33.place(x=420,y=81)

#右側のクラメルの公式のyの分母テキストボックス
bunboy11=tkinter.Entry(width=3)
bunboy11.place(x=360,y=108)
bunboy12=tkinter.Entry(width=3)
bunboy12.place(x=390,y=108)
bunboy13=tkinter.Entry(width=3)
bunboy13.place(x=420,y=108)
bunboy21=tkinter.Entry(width=3)
bunboy21.place(x=360,y=131)
bunboy22=tkinter.Entry(width=3)
bunboy22.place(x=390,y=131)
bunboy23=tkinter.Entry(width=3)
bunboy23.place(x=420,y=131)
bunboy31=tkinter.Entry(width=3)
bunboy31.place(x=360,y=154)
bunboy32=tkinter.Entry(width=3)
bunboy32.place(x=390,y=154)
bunboy33=tkinter.Entry(width=3)
bunboy33.place(x=420,y=154)

#右側のクラメルの公式のyの答えテキストボックス
bunansery=tkinter.Entry(width=4)
bunansery.place(x=458,y=93)

#右側のクラメルの公式のzの分子テキストボックス
bunshiz11=tkinter.Entry(width=3)
bunshiz11.place(x=520,y=35)
bunshiz12=tkinter.Entry(width=3)
bunshiz12.place(x=550,y=35)
bunshiz13=tkinter.Entry(width=3)
bunshiz13.place(x=580,y=35)
bunshiz21=tkinter.Entry(width=3)
bunshiz21.place(x=520,y=58)
bunshiz22=tkinter.Entry(width=3)
bunshiz22.place(x=550,y=58)
bunshiz23=tkinter.Entry(width=3)
bunshiz23.place(x=580,y=58)
bunshiz31=tkinter.Entry(width=3)
bunshiz31.place(x=520,y=81)
bunshiz32=tkinter.Entry(width=3)
bunshiz32.place(x=550,y=81)
bunshiz33=tkinter.Entry(width=3)
bunshiz33.place(x=580,y=81)

#右側のクラメルの公式のzの分母テキストボックス
bunboz11=tkinter.Entry(width=3)
bunboz11.place(x=520,y=108)
bunboz12=tkinter.Entry(width=3)
bunboz12.place(x=550,y=108)
bunboz13=tkinter.Entry(width=3)
bunboz13.place(x=580,y=108)
bunboz21=tkinter.Entry(width=3)
bunboz21.place(x=520,y=131)
bunboz22=tkinter.Entry(width=3)
bunboz22.place(x=550,y=131)
bunboz23=tkinter.Entry(width=3)
bunboz23.place(x=580,y=131)
bunboz31=tkinter.Entry(width=3)
bunboz31.place(x=520,y=154)
bunboz32=tkinter.Entry(width=3)
bunboz32.place(x=550,y=154)
bunboz33=tkinter.Entry(width=3)
bunboz33.place(x=580,y=154)

#右側のクラメルの公式のzの答えテキストボックス
bunanserz=tkinter.Entry(width=4)
bunanserz.place(x=613,y=93)



#ボタン生成
btn=tkinter.Button(tki,text='計算',command=btn_click)
btn.place(x=80,y=125)

#画面をそのまま表示
tki.mainloop()