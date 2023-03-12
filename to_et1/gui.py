import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter.filedialog import *
from PIL import ImageTk,Image
import os
import fileinput
import cv2
import numpy as np
from main import *
from calc_params import *
import calc_params as cp
from test_file2 import *
root = Tk()
root.minsize(width=1200, height=850)
root.wm_title("DCT calculator")
root.config(background = "#FFFFFF")



def open_file():
    global content
    global file_path

    filename = askopenfilename()
    infile = open(filename, 'rb')
    content = infile.read()
    file_path = os.path.abspath(filename)
    tekst1.delete(0, END)
    tekst1.insert(0, file_path)
    return content


'''
for el in range(1,65):
    wartosc + str(el) = mat[x,y]
'''

qXX = np.array([[1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1]])

#
# quality_dict = {
#     "q10" : np.array([[80, 60, 50, 80, 120, 200, 255, 255],
#                     [55, 60, 70, 95, 130, 255, 255, 255],
#                     [70, 65, 80, 120, 200, 255, 255, 255],
#                     [70, 85, 110, 145, 255, 255, 255, 255],
#                     [90, 110, 185, 255, 255, 255, 255, 255],
#                     [120, 175, 255, 255, 255, 255, 255, 255],
#                     [245, 255, 255, 255, 255, 255, 255, 255],
#                     [255, 255, 255, 255, 255, 255, 255, 255]]),
#
#     "q50" : np.array([[16, 11, 10, 16, 24, 40, 51, 61],
#                     [12, 12, 14, 19, 26, 58, 60, 55],
#                     [14, 13, 16, 24, 40, 57, 69, 56],
#                     [14, 17, 22, 29, 51, 87, 80, 62],
#                     [18, 22, 37, 56, 68, 109, 103, 77],
#                     [24, 35, 55, 64, 81, 104, 113, 92],
#                     [49, 64, 78, 87, 103, 121, 120, 101],
#                     [72, 92, 95, 98, 112, 100, 130, 99]]),
#
#     "q90" : np.array([[3, 2, 2, 3, 5, 8, 10, 12],
#                     [2, 2, 3, 4, 5, 12, 12, 11],
#                     [3, 3, 3, 5, 8, 11, 14, 11],
#                     [3, 3, 4, 6, 10, 17, 16, 12],
#                     [4, 4, 7, 11, 14, 22, 21, 15],
#                     [5, 7, 11, 13, 16, 12, 23, 18],
#                     [10, 13, 16, 17, 21, 24, 24, 21],
#                     [14, 18, 19, 20, 22, 20, 20, 20]]),
#
#     "q1" : np.array([[1, 1, 1, 1, 1, 1, 1, 1],
#                     [1, 1, 1, 1, 1, 1, 1, 1],
#                     [1, 1, 1, 1, 1, 1, 1, 1],
#                     [1, 1, 1, 1, 1, 1, 1, 1],
#                     [1, 1, 1, 1, 1, 1, 1, 1],
#                     [1, 1, 1, 1, 1, 1, 1, 1],
#                     [1, 1, 1, 1, 1, 1, 1, 1],
#                     [1, 1, 1, 1, 1, 1, 1, 1]])
# }


def q10():
    global qXX
    qXX = select_q_matrix("q10")


def q50():
    global qXX
    qXX = select_q_matrix("q50")

def q90():
    global qXX
    qXX = select_q_matrix("q90")

def q1():
    global qXX
    qXX = select_q_matrix("q1")


######wiersz0##########

def callback_00(event):
    root.focus_set()
    if B1.bind("<Button-3>", callback_00):
        qXX[0,0]+= -1
        B1['text'] = qXX[0,0]
def callback00(event):
    root.focus_set()
    if B1.bind("<Button-1>", callback00):
        qXX[0,0] += 1
        B1['text'] = qXX[0,0]
def b1():
    #B1.bind("<Double-Button-1>", callback3)
    B1.bind("<Button-3>", callback_00)
    B1.bind("<Button-1>", callback00)
    print(qXX)


def callback_01(event):
    root.focus_set()
    if B2.bind("<Button-3>", callback_01):
        qXX[0,1]+= -1
        B2['text'] = qXX[0,1]
def callback01(event):
    root.focus_set()
    if B2.bind("<Button-1>", callback01):
        qXX[0,1] += 1
        B2['text'] = qXX[0,1]
def b2():
    #B1.bind("<Double-Button-1>", callback3)
    B2.bind("<Button-3>", callback_01)
    B2.bind("<Button-1>", callback01)


def callback_02(event):
    root.focus_set()
    if B3.bind("<Button-3>", callback_02):
        qXX[0,2]+= -1
        B3['text'] = qXX[0,2]
def callback02(event):
    root.focus_set()
    if B3.bind("<Button-1>", callback02):
        qXX[0,2] += 1
        B3['text'] = qXX[0,2]
def b3():
    B3.bind("<Button-3>", callback_02)
    B3.bind("<Button-1>", callback02)


def callback_03(event):
    root.focus_set()
    if B4.bind("<Button-3>", callback_03):
        qXX[0,3]+= -1
        B4['text'] = qXX[0,3]
def callback03(event):
    root.focus_set()
    if B4.bind("<Button-1>", callback03):
        qXX[0,3] += 1
        B4['text'] = qXX[0,3]
def b4():
    B4.bind("<Button-3>", callback_03)
    B4.bind("<Button-1>", callback03)


def callback_04(event):
    root.focus_set()
    if B5.bind("<Button-3>", callback_04):
        qXX[0,4]+= -1
        B5['text'] = qXX[0,4]
def callback04(event):
    root.focus_set()
    if B5.bind("<Button-1>", callback04):
        qXX[0,4] += 1
        B5['text'] = qXX[0,4]
def b5():
    B5.bind("<Button-3>", callback_04)
    B5.bind("<Button-1>", callback04)


def callback_05(event):
    root.focus_set()
    if B6.bind("<Button-3>", callback_05):
        qXX[0,5]+= -1
        B5['text'] = qXX[0,5]
def callback05(event):
    root.focus_set()
    if B6.bind("<Button-1>", callback05):
        qXX[0,5] += 1
        B5['text'] = qXX[0,5]
def b6():
    B6.bind("<Button-3>", callback_05)
    B6.bind("<Button-1>", callback05)


def callback_06(event):
    root.focus_set()
    if B7.bind("<Button-3>", callback_06):
        qXX[0,6]+= -1
        B7['text'] = qXX[0,6]
def callback06(event):
    root.focus_set()
    if B7.bind("<Button-1>", callback06):
        qXX[0,6] += 1
        B7['text'] = qXX[0,6]
def b7():
    B7.bind("<Button-3>", callback_06)
    B7.bind("<Button-1>", callback06)


def callback_07(event):
    root.focus_set()
    if B8.bind("<Button-3>", callback_07):
        qXX[0,7]+= -1
        B8['text'] = qXX[0,7]
def callback07(event):
    root.focus_set()
    if B8.bind("<Button-1>", callback07):
        qXX[0,7] += 1
        B8['text'] = qXX[0,7]
def b8():
    B8.bind("<Button-3>", callback_07)
    B8.bind("<Button-1>", callback07)


######wiersz1##########


def callback_10(event):
    root.focus_set()
    if B9.bind("<Button-3>", callback_10):
        qXX[1,0]+= -1
        B9['text'] = qXX[1,0]
def callback10(event):
    root.focus_set()
    if B9.bind("<Button-1>", callback10):
        qXX[1,0] += 1
        B9['text'] = qXX[1,0]
def b9():
    B9.bind("<Button-3>", callback_10)
    B9.bind("<Button-1>", callback10)


def callback_11(event):
    root.focus_set()
    if B10.bind("<Button-3>", callback_11):
        qXX[1,1]+= -1
        B10['text'] = qXX[1,1]
def callback11(event):
    root.focus_set()
    if B10.bind("<Button-1>", callback11):
        qXX[1,1] += 1
        B10['text'] = qXX[1,1]
def b10():
    B10.bind("<Button-3>", callback_11)
    B10.bind("<Button-1>", callback11)


def callback_12(event):
    root.focus_set()
    if B11.bind("<Button-3>", callback_12):
        qXX[1,2]+= -1
        B11['text'] = qXX[1,2]
def callback12(event):
    root.focus_set()
    if B11.bind("<Button-1>", callback12):
        qXX[1,2] += 1
        B11['text'] = qXX[1,2]
def b11():
    B11.bind("<Button-3>", callback_12)
    B11.bind("<Button-1>", callback12)


def callback_13(event):
    root.focus_set()
    if B12.bind("<Button-3>", callback_13):
        qXX[1,3]+= -1
        B12['text'] = qXX[1,3]
def callback13(event):
    root.focus_set()
    if B12.bind("<Button-1>", callback13):
        qXX[1,3] += 1
        B12['text'] = qXX[1,3]
def b12():
    B12.bind("<Button-3>", callback_13)
    B12.bind("<Button-1>", callback13)


def callback_14(event):
    root.focus_set()
    if B13.bind("<Button-3>", callback_14):
        qXX[1,4]+= -1
        B13['text'] = qXX[1,4]
def callback14(event):
    root.focus_set()
    if B13.bind("<Button-1>", callback14):
        qXX[1,4] += 1
        B13['text'] = qXX[1,4]
def b13():
    B13.bind("<Button-3>", callback_14)
    B13.bind("<Button-1>", callback14)



def callback_15(event):
    root.focus_set()
    if B14.bind("<Button-3>", callback_15):
        qXX[1,5]+= -1
        B14['text'] = qXX[1,5]
def callback15(event):
    root.focus_set()
    if B14.bind("<Button-1>", callback15):
        qXX[1,5] += 1
        B14['text'] = qXX[1,5]
def b14():
    B14.bind("<Button-3>", callback_15)
    B14.bind("<Button-1>", callback15)


def callback_16(event):
    root.focus_set()
    if B15.bind("<Button-3>", callback_16):
        qXX[1,6]+= -1
        B15['text'] = qXX[1,6]
def callback16(event):
    root.focus_set()
    if B15.bind("<Button-1>", callback16):
        qXX[1,6] += 1
        B15['text'] = qXX[1,6]
def b15():
    B15.bind("<Button-3>", callback_16)
    B15.bind("<Button-1>", callback16)


def callback_17(event):
    root.focus_set()
    if B16.bind("<Button-3>", callback_17):
        qXX[1,7]+= -1
        B16['text'] = qXX[1,7]
def callback17(event):
    root.focus_set()
    if B16.bind("<Button-1>", callback17):
        qXX[1,7] += 1
        B16['text'] = qXX[1,7]
def b16():
    B16.bind("<Button-3>", callback_17)
    B16.bind("<Button-1>", callback17)

######wiersz2##########

def callback_20(event):
    root.focus_set()
    if B17.bind("<Button-3>", callback_20):
        qXX[2, 0] += -1
        B17['text'] = qXX[2, 0]
def callback20(event):
    root.focus_set()
    if B17.bind("<Button-1>", callback20):
        qXX[2, 0] += 1
        B17['text'] = qXX[2, 0]
def b17():
    B17.bind("<Button-3>", callback_20)
    B17.bind("<Button-1>", callback20)


def callback_21(event):
    root.focus_set()
    if B18.bind("<Button-3>", callback_21):
        qXX[2, 1] += -1
        B18['text'] = qXX[2, 1]
def callback21(event):
    root.focus_set()
    if B18.bind("<Button-1>", callback21):
        qXX[2, 1] += 1
        B18['text'] = qXX[2, 1]
def b18():
    B18.bind("<Button-3>", callback_21)
    B18.bind("<Button-1>", callback21)


def callback_22(event):
    root.focus_set()
    if B19.bind("<Button-3>", callback_22):
        qXX[2, 2] += -1
        B19['text'] = qXX[2, 2]
def callback22(event):
    root.focus_set()
    if B19.bind("<Button-1>", callback22):
        qXX[2, 2] += 1
        B19['text'] = qXX[2, 2]
def b19():
    B19.bind("<Button-3>", callback_22)
    B19.bind("<Button-1>", callback22)


def callback_23(event):
    root.focus_set()
    if B20.bind("<Button-3>", callback_23):
        qXX[2, 3] += -1
        B20['text'] = qXX[2, 3]
def callback23(event):
    root.focus_set()
    if B20.bind("<Button-1>", callback23):
        qXX[2, 3] += 1
        B20['text'] = qXX[2, 3]
def b20():
    B20.bind("<Button-3>", callback_23)
    B20.bind("<Button-1>", callback23)


def callback_24(event):
    root.focus_set()
    if B21.bind("<Button-3>", callback_24):
        qXX[2, 4] += -1
        B21['text'] = qXX[2, 4]
def callback24(event):
    root.focus_set()
    if B21.bind("<Button-1>", callback24):
        qXX[2, 4] += 1
        B21['text'] = qXX[2, 4]
def b21():
    B21.bind("<Button-3>", callback_24)
    B21.bind("<Button-1>", callback24)


def callback_25(event):
    root.focus_set()
    if B22.bind("<Button-3>", callback_25):
        qXX[2, 5] += -1
        B22['text'] = qXX[2, 5]
def callback25(event):
    root.focus_set()
    if B22.bind("<Button-1>", callback25):
        qXX[2, 5] += 1
        B22['text'] = qXX[2, 5]
def b22():
    B22.bind("<Button-3>", callback_25)
    B22.bind("<Button-1>", callback25)


def callback_26(event):
    root.focus_set()
    if B23.bind("<Button-3>", callback_26):
        qXX[2, 6] += -1
        B23['text'] = qXX[2, 6]
def callback26(event):
    root.focus_set()
    if B23.bind("<Button-1>", callback16):
        qXX[2, 6] += 1
        B23['text'] = qXX[2, 6]
def b23():
    B23.bind("<Button-3>", callback_26)
    B23.bind("<Button-1>", callback26)


def callback_27(event):
    root.focus_set()
    if B24.bind("<Button-3>", callback_27):
        qXX[2, 7] += -1
        B24['text'] = qXX[2, 7]
def callback27(event):
    root.focus_set()
    if B24.bind("<Button-1>", callback17):
        qXX[2, 7] += 1
        B24['text'] = qXX[2, 7]
def b24():
    B24.bind("<Button-3>", callback_27)
    B24.bind("<Button-1>", callback27)


######wiersz3##########

def callback_30(event):
    root.focus_set()
    if B25.bind("<Button-3>", callback_30):
        qXX[3, 0] += -1
        B25['text'] = qXX[3, 0]
def callback30(event):
    root.focus_set()
    if B25.bind("<Button-1>", callback30):
        qXX[3, 0] += 1
        B25['text'] = qXX[3, 0]
def b25():
    B25.bind("<Button-3>", callback_30)
    B25.bind("<Button-1>", callback30)


def callback_31(event):
    root.focus_set()
    if B26.bind("<Button-3>", callback_31):
        qXX[3, 1] += -1
        B26['text'] = qXX[3, 1]
def callback31(event):
    root.focus_set()
    if B26.bind("<Button-1>", callback31):
        qXX[3, 1] += 1
        B26['text'] = qXX[3, 1]
def b26():
    B26.bind("<Button-3>", callback_31)
    B26.bind("<Button-1>", callback31)


def callback_32(event):
    root.focus_set()
    if B27.bind("<Button-3>", callback_32):
        qXX[3, 2] += -1
        B27['text'] = qXX[3, 2]
def callback32(event):
    root.focus_set()
    if B27.bind("<Button-1>", callback32):
        qXX[3, 2] += 1
        B27['text'] = qXX[3, 2]
def b27():
    B27.bind("<Button-3>", callback_32)
    B27.bind("<Button-1>", callback32)


def callback_33(event):
    root.focus_set()
    if B28.bind("<Button-3>", callback_33):
        qXX[3, 3] += -1
        B28['text'] = qXX[3, 3]
def callback33(event):
    root.focus_set()
    if B28.bind("<Button-1>", callback33):
        qXX[3, 3] += 1
        B28['text'] = qXX[3, 3]
def b28():
    B28.bind("<Button-3>", callback_33)
    B28.bind("<Button-1>", callback33)


def callback_34(event):
    root.focus_set()
    if B29.bind("<Button-3>", callback_34):
        qXX[3, 4] += -1
        B29['text'] = qXX[3, 4]
def callback34(event):
    root.focus_set()
    if B29.bind("<Button-1>", callback34):
        qXX[3, 4] += 1
        B29['text'] = qXX[3, 4]
def b29():
    B29.bind("<Button-3>", callback_34)
    B29.bind("<Button-1>", callback34)


def callback_35(event):
    root.focus_set()
    if B30.bind("<Button-3>", callback_35):
        qXX[3, 5] += -1
        B30['text'] = qXX[3, 5]
def callback35(event):
    root.focus_set()
    if B30.bind("<Button-1>", callback35):
        qXX[3, 5] += 1
        B30['text'] = qXX[3, 5]
def b30():
    B30.bind("<Button-3>", callback_35)
    B30.bind("<Button-1>", callback35)


def callback_36(event):
    root.focus_set()
    if B31.bind("<Button-3>", callback_36):
        qXX[3, 6] += -1
        B31['text'] = qXX[3, 6]
def callback36(event):
    root.focus_set()
    if B31.bind("<Button-1>", callback36):
        qXX[3, 6] += 1
        B31['text'] = qXX[3, 6]
def b31():
    B31.bind("<Button-3>", callback_36)
    B31.bind("<Button-1>", callback36)


def callback_37(event):
    root.focus_set()
    if B32.bind("<Button-3>", callback_37):
        qXX[3, 7] += -1
        B32['text'] = qXX[3, 7]
def callback37(event):
    root.focus_set()
    if B32.bind("<Button-1>", callback37):
        qXX[3, 7] += 1
        B32['text'] = qXX[3, 7]
def b32():
    B32.bind("<Button-3>", callback_37)
    B32.bind("<Button-1>", callback37)


######wiersz4##########

def callback_40(event):
    root.focus_set()
    if B33.bind("<Button-3>", callback_40):
        qXX[4, 0] += -1
        B33['text'] = qXX[4, 0]
def callback40(event):
    root.focus_set()
    if B33.bind("<Button-1>", callback40):
        qXX[4, 0] += 1
        B33['text'] = qXX[4, 0]
def b33():
    B33.bind("<Button-3>", callback_40)
    B33.bind("<Button-1>", callback40)


def callback_41(event):
    root.focus_set()
    if B34.bind("<Button-3>", callback_41):
        qXX[4, 1] += -1
        B34['text'] = qXX[4, 1]
def callback41(event):
    root.focus_set()
    if B34.bind("<Button-1>", callback41):
        qXX[4, 1] += 1
        B34['text'] = qXX[4, 1]
def b34():
    B34.bind("<Button-3>", callback_41)
    B34.bind("<Button-1>", callback41)


def callback_42(event):
    root.focus_set()
    if B35.bind("<Button-3>", callback_42):
        qXX[4, 2] += -1
        B35['text'] = qXX[4, 2]
def callback42(event):
    root.focus_set()
    if B35.bind("<Button-1>", callback42):
        qXX[4, 2] += 1
        B35['text'] = qXX[4, 2]
def b35():
    B35.bind("<Button-3>", callback_42)
    B35.bind("<Button-1>", callback42)


def callback_43(event):
    root.focus_set()
    if B36.bind("<Button-3>", callback_43):
        qXX[4, 3] += -1
        B36['text'] = qXX[4, 3]
def callback43(event):
    root.focus_set()
    if B36.bind("<Button-1>", callback43):
        qXX[4, 3] += 1
        B36['text'] = qXX[4, 3]
def b36():
    B36.bind("<Button-3>", callback_43)
    B36.bind("<Button-1>", callback43)


def callback_44(event):
    root.focus_set()
    if B37.bind("<Button-3>", callback_44):
        qXX[4, 4] += -1
        B37['text'] = qXX[4, 4]
def callback44(event):
    root.focus_set()
    if B37.bind("<Button-1>", callback44):
        qXX[4, 4] += 1
        B37['text'] = qXX[4, 4]
def b37():
    B37.bind("<Button-3>", callback_44)
    B37.bind("<Button-1>", callback44)


def callback_45(event):
    root.focus_set()
    if B38.bind("<Button-3>", callback_45):
        qXX[4, 5] += -1
        B38['text'] = qXX[4, 5]
def callback45(event):
    root.focus_set()
    if B38.bind("<Button-1>", callback45):
        qXX[4, 5] += 1
        B38['text'] = qXX[4, 5]
def b38():
    B38.bind("<Button-3>", callback_45)
    B38.bind("<Button-1>", callback45)


def callback_46(event):
    root.focus_set()
    if B39.bind("<Button-3>", callback_46):
        qXX[4, 6] += -1
        B39['text'] = qXX[4, 6]
def callback46(event):
    root.focus_set()
    if B39.bind("<Button-1>", callback46):
        qXX[4, 6] += 1
        B39['text'] = qXX[4, 6]
def b39():
    B39.bind("<Button-3>", callback_46)
    B39.bind("<Button-1>", callback46)


def callback_47(event):
    root.focus_set()
    if B40.bind("<Button-3>", callback_47):
        qXX[4, 7] += -1
        B40['text'] = qXX[4, 7]
def callback47(event):
    root.focus_set()
    if B40.bind("<Button-1>", callback47):
        qXX[4, 7] += 1
        B40['text'] = qXX[4, 7]
def b40():
    B40.bind("<Button-3>", callback_47)
    B40.bind("<Button-1>", callback47)


######wiersz5##########

def callback_50(event):
    root.focus_set()
    if B41.bind("<Button-3>", callback_50):
        qXX[5, 0] += -1
        B41['text'] = qXX[5, 0]
def callback50(event):
    root.focus_set()
    if B41.bind("<Button-1>", callback50):
        qXX[5, 0] += 1
        B41['text'] = qXX[5, 0]
def b41():
    B41.bind("<Button-3>", callback_50)
    B41.bind("<Button-1>", callback50)


def callback_51(event):
    root.focus_set()
    if B42.bind("<Button-3>", callback_51):
        qXX[5, 1] += -1
        B42['text'] = qXX[5, 1]
def callback51(event):
    root.focus_set()
    if B42.bind("<Button-1>", callback51):
        qXX[5, 1] += 1
        B42['text'] = qXX[5, 1]
def b42():
    B42.bind("<Button-3>", callback_51)
    B42.bind("<Button-1>", callback51)


def callback_52(event):
    root.focus_set()
    if B43.bind("<Button-3>", callback_52):
        qXX[5, 2] += -1
        B43['text'] = qXX[5, 2]
def callback52(event):
    root.focus_set()
    if B43.bind("<Button-1>", callback52):
        qXX[5, 2] += 1
        B43['text'] = qXX[5, 2]
def b43():
    B43.bind("<Button-3>", callback_52)
    B43.bind("<Button-1>", callback52)


def callback_53(event):
    root.focus_set()
    if B44.bind("<Button-3>", callback_53):
        qXX[5, 3] += -1
        B44['text'] = qXX[5, 3]
def callback53(event):
    root.focus_set()
    if B44.bind("<Button-1>", callback53):
        qXX[5, 3] += 1
        B44['text'] = qXX[5, 3]
def b44():
    B44.bind("<Button-3>", callback_53)
    B44.bind("<Button-1>", callback53)


def callback_54(event):
    root.focus_set()
    if B45.bind("<Button-3>", callback_54):
        qXX[5, 4] += -1
        B45['text'] = qXX[5, 4]
def callback54(event):
    root.focus_set()
    if B45.bind("<Button-1>", callback54):
        qXX[5, 4] += 1
        B45['text'] = qXX[5, 4]
def b45():
    B45.bind("<Button-3>", callback_54)
    B45.bind("<Button-1>", callback54)


def callback_55(event):
    root.focus_set()
    if B46.bind("<Button-3>", callback_55):
        qXX[5, 5] += -1
        B46['text'] = qXX[5, 5]
def callback55(event):
    root.focus_set()
    if B46.bind("<Button-1>", callback55):
        qXX[5, 5] += 1
        B46['text'] = qXX[5, 5]
def b46():
    B46.bind("<Button-3>", callback_55)
    B46.bind("<Button-1>", callback55)


def callback_56(event):
    root.focus_set()
    if B47.bind("<Button-3>", callback_56):
        qXX[5, 6] += -1
        B47['text'] = qXX[5, 6]
def callback56(event):
    root.focus_set()
    if B47.bind("<Button-1>", callback56):
        qXX[5, 6] += 1
        B47['text'] = qXX[5, 6]
def b47():
    B47.bind("<Button-3>", callback_56)
    B47.bind("<Button-1>", callback56)


def callback_57(event):
    root.focus_set()
    if B48.bind("<Button-3>", callback_57):
        qXX[5, 7] += -1
        B48['text'] = qXX[5, 7]
def callback57(event):
    root.focus_set()
    if B48.bind("<Button-1>", callback57):
        qXX[5, 7] += 1
        B48['text'] = qXX[5, 7]
def b48():
    B48.bind("<Button-3>", callback_57)
    B48.bind("<Button-1>", callback57)


######wiersz6##########

def callback_60(event):
    root.focus_set()
    if B49.bind("<Button-3>", callback_60):
        qXX[6, 0] += -1
        B49['text'] = qXX[6, 0]
def callback60(event):
    root.focus_set()
    if B49.bind("<Button-1>", callback60):
        qXX[6, 0] += 1
        B49['text'] = qXX[6, 0]
def b49():
    B49.bind("<Button-3>", callback_60)
    B49.bind("<Button-1>", callback60)


def callback_61(event):
    root.focus_set()
    if B50.bind("<Button-3>", callback_61):
        qXX[6, 1] += -1
        B50['text'] = qXX[6, 1]
def callback61(event):
    root.focus_set()
    if B50.bind("<Button-1>", callback61):
        qXX[6, 1] += 1
        B50['text'] = qXX[6, 1]
def b50():
    B50.bind("<Button-3>", callback_61)
    B50.bind("<Button-1>", callback61)


def callback_62(event):
    root.focus_set()
    if B51.bind("<Button-3>", callback_62):
        qXX[6, 2] += -1
        B51['text'] = qXX[6, 2]
def callback62(event):
    root.focus_set()
    if B51.bind("<Button-1>", callback62):
        qXX[6, 2] += 1
        B51['text'] = qXX[6, 2]
def b51():
    B51.bind("<Button-3>", callback_62)
    B51.bind("<Button-1>", callback62)


def callback_63(event):
    root.focus_set()
    if B52.bind("<Button-3>", callback_63):
        qXX[6, 3] += -1
        B52['text'] = qXX[6, 3]
def callback63(event):
    root.focus_set()
    if B52.bind("<Button-1>", callback63):
        qXX[6, 3] += 1
        B52['text'] = qXX[6, 3]
def b52():
    B52.bind("<Button-3>", callback_63)
    B52.bind("<Button-1>", callback63)


def callback_64(event):
    root.focus_set()
    if B53.bind("<Button-3>", callback_64):
        qXX[6, 4] += -1
        B53['text'] = qXX[6, 4]
def callback64(event):
    root.focus_set()
    if B53.bind("<Button-1>", callback64):
        qXX[6, 4] += 1
        B53['text'] = qXX[6, 4]
def b53():
    B53.bind("<Button-3>", callback_64)
    B53.bind("<Button-1>", callback64)


def callback_65(event):
    root.focus_set()
    if B54.bind("<Button-3>", callback_65):
        qXX[6, 5] += -1
        B54['text'] = qXX[6, 5]
def callback65(event):
    root.focus_set()
    if B54.bind("<Button-1>", callback65):
        qXX[6, 5] += 1
        B54['text'] = qXX[6, 5]
def b54():
    B54.bind("<Button-3>", callback_65)
    B54.bind("<Button-1>", callback65)


def callback_66(event):
    root.focus_set()
    if B55.bind("<Button-3>", callback_66):
        qXX[6, 6] += -1
        B55['text'] = qXX[6, 6]
def callback66(event):
    root.focus_set()
    if B55.bind("<Button-1>", callback66):
        qXX[6, 6] += 1
        B55['text'] = qXX[6, 6]
def b55():
    B55.bind("<Button-3>", callback_66)
    B55.bind("<Button-1>", callback66)


def callback_67(event):
    root.focus_set()
    if B56.bind("<Button-3>", callback_67):
        qXX[6, 7] += -1
        B56['text'] = qXX[6, 7]
def callback67(event):
    root.focus_set()
    if B56.bind("<Button-1>", callback67):
        qXX[6, 7] += 1
        B56['text'] = qXX[6, 7]
def b56():
    B56.bind("<Button-3>", callback_67)
    B56.bind("<Button-1>", callback67)

######wiersz7##########

def callback_70(event):
    root.focus_set()
    if B57.bind("<Button-3>", callback_70):
        qXX[7, 0] += -1
        B57['text'] = qXX[7, 0]
def callback70(event):
    root.focus_set()
    if B57.bind("<Button-1>", callback70):
        qXX[7, 0] += 1
        B57['text'] = qXX[7, 0]
def b57():
    B57.bind("<Button-3>", callback_70)
    B57.bind("<Button-1>", callback70)


def callback_71(event):
    root.focus_set()
    if B58.bind("<Button-3>", callback_71):
        qXX[7, 1] += -1
        B58['text'] = qXX[7, 1]
def callback71(event):
    root.focus_set()
    if B58.bind("<Button-1>", callback71):
        qXX[7, 1] += 1
        B58['text'] = qXX[7, 1]
def b58():
    B58.bind("<Button-3>", callback_71)
    B58.bind("<Button-1>", callback71)


def callback_72(event):
    root.focus_set()
    if B59.bind("<Button-3>", callback_72):
        qXX[7, 2] += -1
        B59['text'] = qXX[7, 2]
def callback72(event):
    root.focus_set()
    if B59.bind("<Button-1>", callback72):
        qXX[7, 2] += 1
        B59['text'] = qXX[7, 2]
def b59():
    B59.bind("<Button-3>", callback_72)
    B59.bind("<Button-1>", callback72)


def callback_73(event):
    root.focus_set()
    if B60.bind("<Button-3>", callback_73):
        qXX[7, 3] += -1
        B60['text'] = qXX[7, 3]
def callback73(event):
    root.focus_set()
    if B60.bind("<Button-1>", callback73):
        qXX[7, 3] += 1
        B60['text'] = qXX[7, 3]
def b60():
    B60.bind("<Button-3>", callback_73)
    B60.bind("<Button-1>", callback73)


def callback_74(event):
    root.focus_set()
    if B61.bind("<Button-3>", callback_74):
        qXX[7, 4] += -1
        B61['text'] = qXX[7, 4]
def callback74(event):
    root.focus_set()
    if B61.bind("<Button-1>", callback74):
        qXX[7, 4] += 1
        B61['text'] = qXX[7, 4]
def b61():
    B61.bind("<Button-3>", callback_74)
    B61.bind("<Button-1>", callback74)


def callback_75(event):
    root.focus_set()
    if B62.bind("<Button-3>", callback_75):
        qXX[7, 5] += -1
        B62['text'] = qXX[7, 5]
def callback75(event):
    root.focus_set()
    if B62.bind("<Button-1>", callback75):
        qXX[7, 5] += 1
        B62['text'] = qXX[7, 5]
def b62():
    B62.bind("<Button-3>", callback_75)
    B62.bind("<Button-1>", callback75)


def callback_76(event):
    root.focus_set()
    if B63.bind("<Button-3>", callback_76):
        qXX[7, 6] += -1
        B63['text'] = qXX[7, 6]
def callback76(event):
    root.focus_set()
    if B63.bind("<Button-1>", callback76):
        qXX[7, 6] += 1
        B63['text'] = qXX[7, 6]
def b63():
    B63.bind("<Button-3>", callback_76)
    B63.bind("<Button-1>", callback76)


def callback_77(event):
    root.focus_set()
    if B64.bind("<Button-3>", callback_77):
        qXX[7, 7] += -1
        B64['text'] = qXX[7, 7]
def callback77(event):
    root.focus_set()
    if B64.bind("<Button-1>", callback77):
        qXX[7, 7] += 1
        B64['text'] = qXX[7, 7]
def b64():
    B64.bind("<Button-3>", callback_77)
    B64.bind("<Button-1>", callback77)




upframe = Frame(root,width=1190, height = 100, bg='white',highlightbackground="gray", highlightthickness=1)
#upframe.pack(side = LEFT)
upframe.place(x=5, y=5)

#path = r"C:\Users\user\Desktop\TO_proj\to_et1\lena_mono.png"
""" globalna sciezka zapisu zdjec"""
photoframe = Frame(root, width=520, height=520, bg = '#FFFAF0',highlightbackground="gray", highlightthickness=8)
photoframe.place(x=130, y=140)
#image = ImageTk.PhotoImage(Image.open(path))
#photo = Label(photoframe, image=image)
#photo.place(x=130, y=140)





infoframe = Frame(root, width=390, height=650, bg = 'grey')
infoframe.place(x=780, y=120)

matrixframe = Frame(infoframe, width=352, height=352, bg = 'blue')
matrixframe.place(x=20, y=20)



file_path = StringVar()
Btnfile = Button(upframe, width=20, height=20, text="Browse",highlightbackground="gray", highlightthickness=2,command=open_file)
Btnfile.place(width=100,height=30,x=500,y=15)
Btnfile.place(x=540,y=15)

input_text = StringVar()
tekst1 = tk.Entry(upframe, width=80,  textvariable=file_path, bg='white',highlightbackground="gray", highlightthickness=2)
tekst1.place(width=510,height=30,x=10,y=15)
tekst1.place(x=10,y=15)





labelPSNR = Label(infoframe, text='PSNR:',bg="gray",font='Times 20', fg='#000000')
labelPSNR.place(width=100,height=40,x=40,y=390)




labelSSIM = Label(infoframe, text='SSIM:',bg="gray",font='Times 20', fg='#000000')
labelSSIM.place(width=100,height=40,x=40,y=450)

labelSME = Label(infoframe, text='MSE:',bg="gray",font='Times 20', fg='#000000')
labelSME.place(width=100,height=40,x=40,y=510)

mag_value = tk.StringVar(value=1)
mag_box = tk.Spinbox(
    root,
    from_=1,
    to=64,
    textvariable=mag_value,
    wrap=True,
    background="#FAFAD2"
)
mag_box.pack()
mag_box.place(width=105,height=35,x=140,y=750)

frec_value = tk.StringVar(value=1)
frec_box = tk.Spinbox(
    root,
    from_=1,
    to=14,
    textvariable=frec_value,
    wrap=True,
    background="#FFEFD5"
)
frec_box.pack()
frec_box.place(width=105,height=35,x=270,y=750)
#Btn1 = Button(root, text="Przycisk1")
#Btn1.place(x=130,y=740)

def quantize_full(dct_coeffs_matrix, quality):  # quality -> podaje sie:  "qXX"
    """ Najwazniejsza funkcja kwantyzujaca, przeprowadza rowniez proces dekwantyzacji """
    q_matrix = qXX
    no_x_blocks = dct_coeffs_matrix.shape[1] // len(q_matrix)  # q_matrix jest 8x8 wiec 8
    no_y_blocks = dct_coeffs_matrix.shape[0] // len(q_matrix)
    # block_size wybierany na podstawie macierzy jakości QUALITY

    after_quant_matrix = np.zeros_like(dct_coeffs_matrix, dtype=np.int16)  # dtype=np.float64 dtype=np.uint8
    # TODO ustalic typ after_quant_matrix

    quant_temp = quant_once(dct_coeffs_matrix, no_x_blocks, no_y_blocks, q_matrix, "d")
    after_quant_matrix = quant_once(quant_temp, no_x_blocks, no_y_blocks, q_matrix, "m")
    # print(f"\n\n\n\n##########\n {type(after_quant_matrix[0,0])}\n\n\n\n")
    return after_quant_matrix
def zaladuj_photo():
    global photoframe
    global photo
    img = cv2.imread(tekst1.get(), cv2.IMREAD_UNCHANGED)
    path2 = tekst1.get()
    photoframe.destroy()
    photoframe = Frame(root, width=524, height=524, bg='green', highlightbackground="gray", highlightthickness=4)
    photoframe.place(x=120, y=140)

    image1 = ImageTk.PhotoImage(Image.open(path2).resize((512, 512), Image.Resampling.LANCZOS))
    # image2 = image1.resize(250,250)
    photo = Label(photoframe, image=image1)
    photo.place(x=0, y=0)
    photoframe.mainloop()

def zobacz_oryginal():
    global photoframe
    global photo
    img1 = cv2.imread(tekst1.get(), cv2.IMREAD_UNCHANGED)
    path3 = tekst1.get()
    photoframe.destroy()
    photoframe = Frame(root, width=524, height=524, bg='green', highlightbackground="gray", highlightthickness=4)
    photoframe.place(x=120, y=140)

    image3 = ImageTk.PhotoImage(Image.open(path3).resize((512, 512), Image.Resampling.LANCZOS))
    # image2 = image1.resize(250,250)
    photo = Label(photoframe, image=image3)
    photo.place(x=0, y=0)
    photoframe.mainloop()
def btn_quant():
    global qXX

    img = cv2.imread(tekst1.get(), cv2.IMREAD_UNCHANGED)
    dct_coeffs = dct_image(img, 8)
    result_of_quant = quantize_full(dct_coeffs, qXX)
    img_rec = idct_image(result_of_quant, 8)
    # cv2.imwrite("q50_1wspl_WYBORprzedKWANT.jpg", img_rec)
    #cv2.imshow("Wynikowy_1wspol", img_rec)
    cv2.imwrite("wynikowy.jpg", img_rec)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #ksize = (5, 5)
    psnr_val = cp.calc_psnr(img, img_rec)
    mse_val = cp.calc_mse(img, img_rec)
    ssim_val = cp.calc_ssim(img, img_rec)
    labelPSNRdata = Label(infoframe, text=psnr_val, bg="gray", font='Times 20', fg='#000000')
    labelPSNRdata.place(width=100, height=40, x=160, y=390)
   # ssim_val = calc_ssim(img, img_rec)
    labelSSIMdata = Label(infoframe, text=ssim_val, bg="gray", font='Times 20', fg='#000000')
    labelSSIMdata.place(width=100, height=40, x=160, y=450)
  # mse_val = calc_mse(img, img_rec)
    labelSMEdata = Label(infoframe, text=mse_val, bg="gray", font='Times 20', fg='#000000')
    labelSMEdata.place(width=100, height=40, x=160, y=510)
    global photoframe
    global photo

    path1 = ".\\wynikowy.jpg"
    photoframe.destroy()
    photoframe = Frame(root, width=524, height=524, bg='green', highlightbackground="gray", highlightthickness=4)
    photoframe.place(x=120, y=140)

    image1 = ImageTk.PhotoImage(Image.open(path1).resize((512,512),Image.Resampling.LANCZOS))
    #image1 = image1.resize(512,250)
    photo = Label(photoframe, image=image1)
    photo.place(x=0, y=0)
    photoframe.mainloop()

def magnitude():
    global qXX

    img = cv2.imread(tekst1.get(), cv2.COLOR_BGR2GRAY)
    dct_coeffs = dct_image(img, 8)
    print(qXX)
    result_of_choice = apply_chosen_coeffs(dct_coeffs, 8, int(mag_box.get()), "mag")
    result_of_quant = quantize_full(result_of_choice, "qXX")
    img_rec = idct_image(result_of_quant, 8)
    # cv2.imwrite("q50_1wspl_WYBORprzedKWANT.jpg", img_rec)
    # cv2.imshow("Wynikowy_1wspol", img_rec)
    cv2.imwrite("wynikowymagnitude.jpg", img_rec)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    psnr_val = calc_psnr(img, img_rec)
    labelPSNRdata = Label(infoframe, text=psnr_val, bg="gray", font='Times 20', fg='#000000')
    labelPSNRdata.place(width=100, height=40, x=160, y=390)
    ssim_val = calc_ssim(img, img_rec)
    labelSSIMdata = Label(infoframe, text=ssim_val, bg="gray", font='Times 20', fg='#000000')
    labelSSIMdata.place(width=100, height=40, x=160, y=450)
    mse_val = calc_mse(img, img_rec)
    labelSMEdata = Label(infoframe, text=mse_val, bg="gray", font='Times 20', fg='#000000')
    labelSMEdata.place(width=100, height=40, x=160, y=510)
    global photoframe
    global photo

    path1 = ".\\wynikowymagnitude.jpg"
    photoframe.destroy()
    photoframe = Frame(root, width=524, height=524, bg='green', highlightbackground="gray", highlightthickness=4)
    photoframe.place(x=120, y=140)

    image1 = ImageTk.PhotoImage(Image.open(path1).resize((512, 512), Image.Resampling.LANCZOS))
    # image1 = image1.resize(512,250)
    photo = Label(photoframe, image=image1)
    photo.place(x=0, y=0)
    photoframe.mainloop()


def frec():
    global qXX

    img = cv2.imread(tekst1.get(), cv2.COLOR_BGR2GRAY)
    dct_coeffs = dct_image(img, 8)
    print(qXX)
    result_of_choice = apply_chosen_coeffs(dct_coeffs, 8, int(frec_box.get()), "frec")
    result_of_quant = quantize_full(result_of_choice, "qXX")
    img_rec = idct_image(result_of_quant, 8)
    # cv2.imwrite("q50_1wspl_WYBORprzedKWANT.jpg", img_rec)
    # cv2.imshow("Wynikowy_1wspol", img_rec)
    cv2.imwrite("wynikowyfrec.jpg", img_rec)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    psnr_val = calc_psnr(img, img_rec)
    labelPSNRdata = Label(infoframe, text=psnr_val, bg="gray", font='Times 20', fg='#000000')
    labelPSNRdata.place(width=100, height=40, x=160, y=390)
    ssim_val = calc_ssim(img, img_rec)
    labelSSIMdata = Label(infoframe, text=ssim_val, bg="gray", font='Times 20', fg='#000000')
    labelSSIMdata.place(width=100, height=40, x=160, y=450)
    mse_val = calc_mse(img, img_rec)
    labelSMEdata = Label(infoframe, text=mse_val, bg="gray", font='Times 20', fg='#000000')
    labelSMEdata.place(width=100, height=40, x=160, y=510)
    global photoframe
    global photo

    path1 = ".\\wynikowyfrec.jpg"
    photoframe.destroy()
    photoframe = Frame(root, width=524, height=524, bg='green', highlightbackground="gray", highlightthickness=4)
    photoframe.place(x=120, y=140)

    image1 = ImageTk.PhotoImage(Image.open(path1).resize((512, 512), Image.Resampling.LANCZOS))
    # image1 = image1.resize(512,250)
    photo = Label(photoframe, image=image1)
    photo.place(x=0, y=0)
    photoframe.mainloop()

Btn0 = Button(root, text="Po amplitudzie",bg="#FAFAD2",command=magnitude)
Btn0.place(width=105,height=40,x=140,y=700)

Btn1 = Button(root, bg="#FFEFD5",text="Po obszarze",command=frec)
Btn1.place(width=105,height=40,x=270,y=700)



Btn2 = Button(root, text="Zobacz oryginalny",bg="#FFE4B5",command=zobacz_oryginal)
Btn2.place(width=105,height=40,x=400,y=700)
#Btn3 = Button(root, text="Licz kwantyzacje",command=lambda: [btn_quant(),refresh_photo()])
Btn3 = Button(root, text="Licz kwantyzacje",bg="#FFA07A",command=btn_quant)
Btn3.place(width=105,height=40,x=530,y=700)

var1 = IntVar()
#R1 = Radiobutton(upframe, text="8x8", variable=var1, value=1)
#R1.place(width=100,height=30,x=10,y=55)
#R1.pack( anchor = W )

#R3 = Radiobutton(upframe, text="cały", variable=var1, value=2)
#R3.place(width=100,height=30,x=250,y=55)
#R3.pack( anchor = W)


Btq10 = Button(upframe, text="q10", command=lambda: [q10(), refresh()])
Btq10.place(width=50,height=30,x=785,y=35)

Btq50 = Button(upframe, text="q50", command=lambda: [q50(), refresh()])
Btq50.place(width=50,height=30,x=885,y=35)

Btq90 = Button(upframe, text="q90", command=lambda: [q90(), refresh()])
Btq90.place(width=50,height=30,x=985,y=35)

Btq1 = Button(upframe, text="q1", command=lambda: [q1(), refresh()])
Btq1.place(width=50,height=30,x=1085,y=35)


##############################################  WSPOLCZYNNIKI #################################################################################################

B1 = Button(matrixframe, text=qXX[0,0],command=b1)
B1.place(width=43.75,height=43.75,x=0,y=0)

B2 = Button(matrixframe, text=qXX[0,1],command=b2)
B2.place(width=43.75,height=43.75,x=43.75,y=0)

B3 = Button(matrixframe, text=qXX[0,2],command=b3)
B3.place(width=43.75,height=43.75,x=87.5,y=0)

B4 = Button(matrixframe, text=qXX[0,3],command=b4)
B4.place(width=43.75,height=43.75,x=132,y=0)

B5 = Button(matrixframe, text=qXX[0,4],command=b5)
B5.place(width=43.75,height=43.75,x=176,y=0)

B6 = Button(matrixframe, text=qXX[0,5],command=b6)
B6.place(width=43.75,height=43.75,x=219.75,y=0)

B7 = Button(matrixframe, text=qXX[0,6],command=b7)
B7.place(width=43.75,height=43.75,x=263.75,y=0)

B8 = Button(matrixframe, text=qXX[0,7],command=b8)
B8.place(width=43.75,height=43.75,x=307.75,y=0)

B9 = Button(matrixframe, text=qXX[1,0],command=b9)
B9.place(width=43.75,height=43.75,x=0,y=43.75)

B10= Button(matrixframe, text=qXX[1,1],command=b10)
B10.place(width=43.75,height=43.75,x=43.75,y=43.75)

B11 = Button(matrixframe, text=qXX[1,2],command=b11)
B11.place(width=43.75,height=43.75,x=87.5,y=43.75)

B12 = Button(matrixframe, text=qXX[1,3],command=b12)
B12.place(width=43.75,height=43.75,x=132,y=43.75)

B13 = Button(matrixframe, text=qXX[1,4],command=b13)
B13.place(width=43.75,height=43.75,x=176,y=43.75)

B14 = Button(matrixframe, text=qXX[1,5],command=b14)
B14.place(width=43.75,height=43.75,x=219.75,y=43.75)

B15 = Button(matrixframe, text=qXX[1,6],command=b15)
B15.place(width=43.75,height=43.75,x=263.75,y=43.75)

B16 = Button(matrixframe, text=qXX[1,7],command=b16)
B16.place(width=43.75,height=43.75,x=307.75,y=43.75)

B17 = Button(matrixframe, text=qXX[2,0],command=b17)
B17.place(width=43.75,height=43.75,x=0,y=87.5)

B18= Button(matrixframe, text=qXX[2,1],command=b18)
B18.place(width=43.75,height=43.75,x=43.75,y=87.5)

B19 = Button(matrixframe, text=qXX[2,2],command=b19)
B19.place(width=43.75,height=43.75,x=87.5,y=87.5)

B20 = Button(matrixframe, text=qXX[2,3],command=b20)
B20.place(width=43.75,height=43.75,x=132,y=87.5)

B21 = Button(matrixframe, text=qXX[2,4],command=b21)
B21.place(width=43.75,height=43.75,x=176,y=87.5)

B22 = Button(matrixframe, text=qXX[2,5],command=b22)
B22.place(width=43.75,height=43.75,x=219.75,y=87.5)

B23 = Button(matrixframe, text=qXX[2,6],command=b23)
B23.place(width=43.75,height=43.75,x=263.75,y=87.5)

B24 = Button(matrixframe, text=qXX[2,7],command=b24)
B24.place(width=43.75,height=43.75,x=307.75,y=87.5)

B25 = Button(matrixframe, text=qXX[3,0],command=b25)
B25.place(width=43.75,height=43.75,x=0,y=132)

B26= Button(matrixframe, text=qXX[3,1],command=b26)
B26.place(width=43.75,height=43.75,x=43.75,y=132)

B27 = Button(matrixframe, text=qXX[3,2],command=b27)
B27.place(width=43.75,height=43.75,x=87.5,y=132)

B28 = Button(matrixframe, text=qXX[3,3],command=b28)
B28.place(width=43.75,height=43.75,x=132,y=132)

B29 = Button(matrixframe, text=qXX[3,4],command=b29)
B29.place(width=43.75,height=43.75,x=176,y=132)

B30 = Button(matrixframe, text=qXX[3,5],command=b30)
B30.place(width=43.75,height=43.75,x=219.75,y=132)

B31 = Button(matrixframe, text=qXX[3,6],command=b31)
B31.place(width=43.75,height=43.75,x=263.75,y=132)

B32 = Button(matrixframe, text=qXX[3,7],command=b32)
B32.place(width=43.75,height=43.75,x=307.75,y=132)

B33 = Button(matrixframe, text=qXX[4,0],command=b33)
B33.place(width=43.75,height=43.75,x=0,y=176)

B34= Button(matrixframe, text=qXX[4,1],command=b34)
B34.place(width=43.75,height=43.75,x=43.75,y=176)

B35 = Button(matrixframe, text=qXX[4,2],command=b35)
B35.place(width=43.75,height=43.75,x=87.5,y=176)

B36 = Button(matrixframe, text=qXX[4,3],command=b36)
B36.place(width=43.75,height=43.75,x=132,y=176)

B37 = Button(matrixframe, text=qXX[4,4],command=b37)
B37.place(width=43.75,height=43.75,x=176,y=176)

B38 = Button(matrixframe, text=qXX[4,5],command=b38)
B38.place(width=43.75,height=43.75,x=219.75,y=176)

B39 = Button(matrixframe, text=qXX[4,6],command=b39)
B39.place(width=43.75,height=43.75,x=263.75,y=176)

B40 = Button(matrixframe, text=qXX[4,7],command=b40)
B40.place(width=43.75,height=43.75,x=307.75,y=176)

B41 = Button(matrixframe, text=qXX[5,0],command=b41)
B41.place(width=43.75,height=43.75,x=0,y=219.75)

B42= Button(matrixframe, text=qXX[5,1],command=b42)
B42.place(width=43.75,height=43.75,x=43.75,y=219.75)

B43 = Button(matrixframe, text=qXX[5,2],command=b43)
B43.place(width=43.75,height=43.75,x=87.5,y=219.75)

B44 = Button(matrixframe, text=qXX[5,3],command=b44)
B44.place(width=43.75,height=43.75,x=132,y=219.75)

B45 = Button(matrixframe, text=qXX[5,4],command=b45)
B45.place(width=43.75,height=43.75,x=176,y=219.75)

B46 = Button(matrixframe, text=qXX[5,5],command=b46)
B46.place(width=43.75,height=43.75,x=219.75,y=219.75)

B47 = Button(matrixframe, text=qXX[5,6],command=b47)
B47.place(width=43.75,height=43.75,x=263.75,y=219.75)

B48 = Button(matrixframe, text=qXX[5,7],command=b48)
B48.place(width=43.75,height=43.75,x=307.75,y=219.75)

B49 = Button(matrixframe, text=qXX[6,0],command=b49)
B49.place(width=43.75,height=43.75,x=0,y=263.75)

B50= Button(matrixframe, text=qXX[6,1],command=b50)
B50.place(width=43.75,height=43.75,x=43.75,y=263.75)

B51 = Button(matrixframe, text=qXX[6,2],command=b51)
B51.place(width=43.75,height=43.75,x=87.5,y=263.75)

B52 = Button(matrixframe, text=qXX[6,3],command=b52)
B52.place(width=43.75,height=43.75,x=132,y=263.75)

B53 = Button(matrixframe, text=qXX[6,4],command=b53)
B53.place(width=43.75,height=43.75,x=176,y=263.75)

B54 = Button(matrixframe, text=qXX[6,5],command=b54)
B54.place(width=43.75,height=43.75,x=219.75,y=263.75)

B55 = Button(matrixframe, text=qXX[6,6],command=b55)
B55.place(width=43.75,height=43.75,x=263.75,y=263.75)

B56 = Button(matrixframe, text=qXX[6,7],command=b56)
B56.place(width=43.75,height=43.75,x=307.75,y=263.75)

B57 = Button(matrixframe, text=qXX[7,0],command=b57)
B57.place(width=43.75,height=43.75,x=0,y=307.75)

B58= Button(matrixframe, text=qXX[7,1],command=b58)
B58.place(width=43.75,height=43.75,x=43.75,y=307.75)

B59 = Button(matrixframe, text=qXX[7,2],command=b59)
B59.place(width=43.75,height=43.75,x=87.5,y=307.75)

B60 = Button(matrixframe, text=qXX[7,3],command=b60)
B60.place(width=43.75,height=43.75,x=132,y=307.75)

B61 = Button(matrixframe, text=qXX[7,4],command=b61)
B61.place(width=43.75,height=43.75,x=176,y=307.75)

B62 = Button(matrixframe, text=qXX[7,5],command=b62)
B62.place(width=43.75,height=43.75,x=219.75,y=307.75)

B63 = Button(matrixframe, text=qXX[7,6],command=b63)
B63.place(width=43.75,height=43.75,x=263.75,y=307.75)

B64 = Button(matrixframe, text=qXX[7,7],command=b64)
B64.place(width=43.75,height=43.75,x=307.75,y=307.75)


"""
openfileBtn = Button(upframe, text="Open file",command=openfile)
openfileBtn.place(x=120,y=20)
"""



#root.mainloop() #start monitoring and updating the GUI
def refresh():
    ######wiersz0##########

    def callback_00(event):
        root.focus_set()
        if B1.bind("<Button-3>", callback_00):
            qXX[0, 0] += -1
            B1['text'] = qXX[0, 0]

    def callback00(event):
        root.focus_set()
        if B1.bind("<Button-1>", callback00):
            qXX[0, 0] += 1
            B1['text'] = qXX[0, 0]

    def b1():
        # B1.bind("<Double-Button-1>", callback3)
        B1.bind("<Button-3>", callback_00)
        B1.bind("<Button-1>", callback00)
        print(qXX)

    def callback_01(event):
        root.focus_set()
        if B2.bind("<Button-3>", callback_01):
            qXX[0, 1] += -1
            B2['text'] = qXX[0, 1]

    def callback01(event):
        root.focus_set()
        if B2.bind("<Button-1>", callback01):
            qXX[0, 1] += 1
            B2['text'] = qXX[0, 1]

    def b2():
        # B1.bind("<Double-Button-1>", callback3)
        B2.bind("<Button-3>", callback_01)
        B2.bind("<Button-1>", callback01)

    def callback_02(event):
        root.focus_set()
        if B3.bind("<Button-3>", callback_02):
            qXX[0, 2] += -1
            B3['text'] = qXX[0, 2]

    def callback02(event):
        root.focus_set()
        if B3.bind("<Button-1>", callback02):
            qXX[0, 2] += 1
            B3['text'] = qXX[0, 2]

    def b3():
        B3.bind("<Button-3>", callback_02)
        B3.bind("<Button-1>", callback02)

    def callback_03(event):
        root.focus_set()
        if B4.bind("<Button-3>", callback_03):
            qXX[0, 3] += -1
            B4['text'] = qXX[0, 3]

    def callback03(event):
        root.focus_set()
        if B4.bind("<Button-1>", callback03):
            qXX[0, 3] += 1
            B4['text'] = qXX[0, 3]

    def b4():
        B4.bind("<Button-3>", callback_03)
        B4.bind("<Button-1>", callback03)

    def callback_04(event):
        root.focus_set()
        if B5.bind("<Button-3>", callback_04):
            qXX[0, 4] += -1
            B5['text'] = qXX[0, 4]

    def callback04(event):
        root.focus_set()
        if B5.bind("<Button-1>", callback04):
            qXX[0, 4] += 1
            B5['text'] = qXX[0, 4]

    def b5():
        B5.bind("<Button-3>", callback_04)
        B5.bind("<Button-1>", callback04)

    def callback_05(event):
        root.focus_set()
        if B6.bind("<Button-3>", callback_05):
            qXX[0, 5] += -1
            B5['text'] = qXX[0, 5]

    def callback05(event):
        root.focus_set()
        if B6.bind("<Button-1>", callback05):
            qXX[0, 5] += 1
            B5['text'] = qXX[0, 5]

    def b6():
        B6.bind("<Button-3>", callback_05)
        B6.bind("<Button-1>", callback05)

    def callback_06(event):
        root.focus_set()
        if B7.bind("<Button-3>", callback_06):
            qXX[0, 6] += -1
            B7['text'] = qXX[0, 6]

    def callback06(event):
        root.focus_set()
        if B7.bind("<Button-1>", callback06):
            qXX[0, 6] += 1
            B7['text'] = qXX[0, 6]

    def b7():
        B7.bind("<Button-3>", callback_06)
        B7.bind("<Button-1>", callback06)

    def callback_07(event):
        root.focus_set()
        if B8.bind("<Button-3>", callback_07):
            qXX[0, 7] += -1
            B8['text'] = qXX[0, 7]

    def callback07(event):
        root.focus_set()
        if B8.bind("<Button-1>", callback07):
            qXX[0, 7] += 1
            B8['text'] = qXX[0, 7]

    def b8():
        B8.bind("<Button-3>", callback_07)
        B8.bind("<Button-1>", callback07)

    ######wiersz1##########

    def callback_10(event):
        root.focus_set()
        if B9.bind("<Button-3>", callback_10):
            qXX[1, 0] += -1
            B9['text'] = qXX[1, 0]

    def callback10(event):
        root.focus_set()
        if B9.bind("<Button-1>", callback10):
            qXX[1, 0] += 1
            B9['text'] = qXX[1, 0]

    def b9():
        B9.bind("<Button-3>", callback_10)
        B9.bind("<Button-1>", callback10)

    def callback_11(event):
        root.focus_set()
        if B10.bind("<Button-3>", callback_11):
            qXX[1, 1] += -1
            B10['text'] = qXX[1, 1]

    def callback11(event):
        root.focus_set()
        if B10.bind("<Button-1>", callback11):
            qXX[1, 1] += 1
            B10['text'] = qXX[1, 1]

    def b10():
        B10.bind("<Button-3>", callback_11)
        B10.bind("<Button-1>", callback11)

    def callback_12(event):
        root.focus_set()
        if B11.bind("<Button-3>", callback_12):
            qXX[1, 2] += -1
            B11['text'] = qXX[1, 2]

    def callback12(event):
        root.focus_set()
        if B11.bind("<Button-1>", callback12):
            qXX[1, 2] += 1
            B11['text'] = qXX[1, 2]

    def b11():
        B11.bind("<Button-3>", callback_12)
        B11.bind("<Button-1>", callback12)

    def callback_13(event):
        root.focus_set()
        if B12.bind("<Button-3>", callback_13):
            qXX[1, 3] += -1
            B12['text'] = qXX[1, 3]

    def callback13(event):
        root.focus_set()
        if B12.bind("<Button-1>", callback13):
            qXX[1, 3] += 1
            B12['text'] = qXX[1, 3]

    def b12():
        B12.bind("<Button-3>", callback_13)
        B12.bind("<Button-1>", callback13)

    def callback_14(event):
        root.focus_set()
        if B13.bind("<Button-3>", callback_14):
            qXX[1, 4] += -1
            B13['text'] = qXX[1, 4]

    def callback14(event):
        root.focus_set()
        if B13.bind("<Button-1>", callback14):
            qXX[1, 4] += 1
            B13['text'] = qXX[1, 4]

    def b13():
        B13.bind("<Button-3>", callback_14)
        B13.bind("<Button-1>", callback14)

    def callback_15(event):
        root.focus_set()
        if B14.bind("<Button-3>", callback_15):
            qXX[1, 5] += -1
            B14['text'] = qXX[1, 5]

    def callback15(event):
        root.focus_set()
        if B14.bind("<Button-1>", callback15):
            qXX[1, 5] += 1
            B14['text'] = qXX[1, 5]

    def b14():
        B14.bind("<Button-3>", callback_15)
        B14.bind("<Button-1>", callback15)

    def callback_16(event):
        root.focus_set()
        if B15.bind("<Button-3>", callback_16):
            qXX[1, 6] += -1
            B15['text'] = qXX[1, 6]

    def callback16(event):
        root.focus_set()
        if B15.bind("<Button-1>", callback16):
            qXX[1, 6] += 1
            B15['text'] = qXX[1, 6]

    def b15():
        B15.bind("<Button-3>", callback_16)
        B15.bind("<Button-1>", callback16)

    def callback_17(event):
        root.focus_set()
        if B16.bind("<Button-3>", callback_17):
            qXX[1, 7] += -1
            B16['text'] = qXX[1, 7]

    def callback17(event):
        root.focus_set()
        if B16.bind("<Button-1>", callback17):
            qXX[1, 7] += 1
            B16['text'] = qXX[1, 7]

    def b16():
        B16.bind("<Button-3>", callback_17)
        B16.bind("<Button-1>", callback17)

    ######wiersz2##########

    def callback_20(event):
        root.focus_set()
        if B17.bind("<Button-3>", callback_20):
            qXX[2, 0] += -1
            B17['text'] = qXX[2, 0]

    def callback20(event):
        root.focus_set()
        if B17.bind("<Button-1>", callback20):
            qXX[2, 0] += 1
            B17['text'] = qXX[2, 0]

    def b17():
        B17.bind("<Button-3>", callback_20)
        B17.bind("<Button-1>", callback20)

    def callback_21(event):
        root.focus_set()
        if B18.bind("<Button-3>", callback_21):
            qXX[2, 1] += -1
            B18['text'] = qXX[2, 1]

    def callback21(event):
        root.focus_set()
        if B18.bind("<Button-1>", callback21):
            qXX[2, 1] += 1
            B18['text'] = qXX[2, 1]

    def b18():
        B18.bind("<Button-3>", callback_21)
        B18.bind("<Button-1>", callback21)

    def callback_22(event):
        root.focus_set()
        if B19.bind("<Button-3>", callback_22):
            qXX[2, 2] += -1
            B19['text'] = qXX[2, 2]

    def callback22(event):
        root.focus_set()
        if B19.bind("<Button-1>", callback22):
            qXX[2, 2] += 1
            B19['text'] = qXX[2, 2]

    def b19():
        B19.bind("<Button-3>", callback_22)
        B19.bind("<Button-1>", callback22)

    def callback_23(event):
        root.focus_set()
        if B20.bind("<Button-3>", callback_23):
            qXX[2, 3] += -1
            B20['text'] = qXX[2, 3]

    def callback23(event):
        root.focus_set()
        if B20.bind("<Button-1>", callback23):
            qXX[2, 3] += 1
            B20['text'] = qXX[2, 3]

    def b20():
        B20.bind("<Button-3>", callback_23)
        B20.bind("<Button-1>", callback23)

    def callback_24(event):
        root.focus_set()
        if B21.bind("<Button-3>", callback_24):
            qXX[2, 4] += -1
            B21['text'] = qXX[2, 4]

    def callback24(event):
        root.focus_set()
        if B21.bind("<Button-1>", callback24):
            qXX[2, 4] += 1
            B21['text'] = qXX[2, 4]

    def b21():
        B21.bind("<Button-3>", callback_24)
        B21.bind("<Button-1>", callback24)

    def callback_25(event):
        root.focus_set()
        if B22.bind("<Button-3>", callback_25):
            qXX[2, 5] += -1
            B22['text'] = qXX[2, 5]

    def callback25(event):
        root.focus_set()
        if B22.bind("<Button-1>", callback25):
            qXX[2, 5] += 1
            B22['text'] = qXX[2, 5]

    def b22():
        B22.bind("<Button-3>", callback_25)
        B22.bind("<Button-1>", callback25)

    def callback_26(event):
        root.focus_set()
        if B23.bind("<Button-3>", callback_26):
            qXX[2, 6] += -1
            B23['text'] = qXX[2, 6]

    def callback26(event):
        root.focus_set()
        if B23.bind("<Button-1>", callback16):
            qXX[2, 6] += 1
            B23['text'] = qXX[2, 6]

    def b23():
        B23.bind("<Button-3>", callback_26)
        B23.bind("<Button-1>", callback26)

    def callback_27(event):
        root.focus_set()
        if B24.bind("<Button-3>", callback_27):
            qXX[2, 7] += -1
            B24['text'] = qXX[2, 7]

    def callback27(event):
        root.focus_set()
        if B24.bind("<Button-1>", callback17):
            qXX[2, 7] += 1
            B24['text'] = qXX[2, 7]

    def b24():
        B24.bind("<Button-3>", callback_27)
        B24.bind("<Button-1>", callback27)

    ######wiersz3##########

    def callback_30(event):
        root.focus_set()
        if B25.bind("<Button-3>", callback_30):
            qXX[3, 0] += -1
            B25['text'] = qXX[3, 0]

    def callback30(event):
        root.focus_set()
        if B25.bind("<Button-1>", callback30):
            qXX[3, 0] += 1
            B25['text'] = qXX[3, 0]

    def b25():
        B25.bind("<Button-3>", callback_30)
        B25.bind("<Button-1>", callback30)

    def callback_31(event):
        root.focus_set()
        if B26.bind("<Button-3>", callback_31):
            qXX[3, 1] += -1
            B26['text'] = qXX[3, 1]

    def callback31(event):
        root.focus_set()
        if B26.bind("<Button-1>", callback31):
            qXX[3, 1] += 1
            B26['text'] = qXX[3, 1]

    def b26():
        B26.bind("<Button-3>", callback_31)
        B26.bind("<Button-1>", callback31)

    def callback_32(event):
        root.focus_set()
        if B27.bind("<Button-3>", callback_32):
            qXX[3, 2] += -1
            B27['text'] = qXX[3, 2]

    def callback32(event):
        root.focus_set()
        if B27.bind("<Button-1>", callback32):
            qXX[3, 2] += 1
            B27['text'] = qXX[3, 2]

    def b27():
        B27.bind("<Button-3>", callback_32)
        B27.bind("<Button-1>", callback32)

    def callback_33(event):
        root.focus_set()
        if B28.bind("<Button-3>", callback_33):
            qXX[3, 3] += -1
            B28['text'] = qXX[3, 3]

    def callback33(event):
        root.focus_set()
        if B28.bind("<Button-1>", callback33):
            qXX[3, 3] += 1
            B28['text'] = qXX[3, 3]

    def b28():
        B28.bind("<Button-3>", callback_33)
        B28.bind("<Button-1>", callback33)

    def callback_34(event):
        root.focus_set()
        if B29.bind("<Button-3>", callback_34):
            qXX[3, 4] += -1
            B29['text'] = qXX[3, 4]

    def callback34(event):
        root.focus_set()
        if B29.bind("<Button-1>", callback34):
            qXX[3, 4] += 1
            B29['text'] = qXX[3, 4]

    def b29():
        B29.bind("<Button-3>", callback_34)
        B29.bind("<Button-1>", callback34)

    def callback_35(event):
        root.focus_set()
        if B30.bind("<Button-3>", callback_35):
            qXX[3, 5] += -1
            B30['text'] = qXX[3, 5]

    def callback35(event):
        root.focus_set()
        if B30.bind("<Button-1>", callback35):
            qXX[3, 5] += 1
            B30['text'] = qXX[3, 5]

    def b30():
        B30.bind("<Button-3>", callback_35)
        B30.bind("<Button-1>", callback35)

    def callback_36(event):
        root.focus_set()
        if B31.bind("<Button-3>", callback_36):
            qXX[3, 6] += -1
            B31['text'] = qXX[3, 6]

    def callback36(event):
        root.focus_set()
        if B31.bind("<Button-1>", callback36):
            qXX[3, 6] += 1
            B31['text'] = qXX[3, 6]

    def b31():
        B31.bind("<Button-3>", callback_36)
        B31.bind("<Button-1>", callback36)

    def callback_37(event):
        root.focus_set()
        if B32.bind("<Button-3>", callback_37):
            qXX[3, 7] += -1
            B32['text'] = qXX[3, 7]

    def callback37(event):
        root.focus_set()
        if B32.bind("<Button-1>", callback37):
            qXX[3, 7] += 1
            B32['text'] = qXX[3, 7]

    def b32():
        B32.bind("<Button-3>", callback_37)
        B32.bind("<Button-1>", callback37)

    ######wiersz4##########

    def callback_40(event):
        root.focus_set()
        if B33.bind("<Button-3>", callback_40):
            qXX[4, 0] += -1
            B33['text'] = qXX[4, 0]

    def callback40(event):
        root.focus_set()
        if B33.bind("<Button-1>", callback40):
            qXX[4, 0] += 1
            B33['text'] = qXX[4, 0]

    def b33():
        B33.bind("<Button-3>", callback_40)
        B33.bind("<Button-1>", callback40)

    def callback_41(event):
        root.focus_set()
        if B34.bind("<Button-3>", callback_41):
            qXX[4, 1] += -1
            B34['text'] = qXX[4, 1]

    def callback41(event):
        root.focus_set()
        if B34.bind("<Button-1>", callback41):
            qXX[4, 1] += 1
            B34['text'] = qXX[4, 1]

    def b34():
        B34.bind("<Button-3>", callback_41)
        B34.bind("<Button-1>", callback41)

    def callback_42(event):
        root.focus_set()
        if B35.bind("<Button-3>", callback_42):
            qXX[4, 2] += -1
            B35['text'] = qXX[4, 2]

    def callback42(event):
        root.focus_set()
        if B35.bind("<Button-1>", callback42):
            qXX[4, 2] += 1
            B35['text'] = qXX[4, 2]

    def b35():
        B35.bind("<Button-3>", callback_42)
        B35.bind("<Button-1>", callback42)

    def callback_43(event):
        root.focus_set()
        if B36.bind("<Button-3>", callback_43):
            qXX[4, 3] += -1
            B36['text'] = qXX[4, 3]

    def callback43(event):
        root.focus_set()
        if B36.bind("<Button-1>", callback43):
            qXX[4, 3] += 1
            B36['text'] = qXX[4, 3]

    def b36():
        B36.bind("<Button-3>", callback_43)
        B36.bind("<Button-1>", callback43)

    def callback_44(event):
        root.focus_set()
        if B37.bind("<Button-3>", callback_44):
            qXX[4, 4] += -1
            B37['text'] = qXX[4, 4]

    def callback44(event):
        root.focus_set()
        if B37.bind("<Button-1>", callback44):
            qXX[4, 4] += 1
            B37['text'] = qXX[4, 4]

    def b37():
        B37.bind("<Button-3>", callback_44)
        B37.bind("<Button-1>", callback44)

    def callback_45(event):
        root.focus_set()
        if B38.bind("<Button-3>", callback_45):
            qXX[4, 5] += -1
            B38['text'] = qXX[4, 5]

    def callback45(event):
        root.focus_set()
        if B38.bind("<Button-1>", callback45):
            qXX[4, 5] += 1
            B38['text'] = qXX[4, 5]

    def b38():
        B38.bind("<Button-3>", callback_45)
        B38.bind("<Button-1>", callback45)

    def callback_46(event):
        root.focus_set()
        if B39.bind("<Button-3>", callback_46):
            qXX[4, 6] += -1
            B39['text'] = qXX[4, 6]

    def callback46(event):
        root.focus_set()
        if B39.bind("<Button-1>", callback46):
            qXX[4, 6] += 1
            B39['text'] = qXX[4, 6]

    def b39():
        B39.bind("<Button-3>", callback_46)
        B39.bind("<Button-1>", callback46)

    def callback_47(event):
        root.focus_set()
        if B40.bind("<Button-3>", callback_47):
            qXX[4, 7] += -1
            B40['text'] = qXX[4, 7]

    def callback47(event):
        root.focus_set()
        if B40.bind("<Button-1>", callback47):
            qXX[4, 7] += 1
            B40['text'] = qXX[4, 7]

    def b40():
        B40.bind("<Button-3>", callback_47)
        B40.bind("<Button-1>", callback47)

    ######wiersz5##########

    def callback_50(event):
        root.focus_set()
        if B41.bind("<Button-3>", callback_50):
            qXX[5, 0] += -1
            B41['text'] = qXX[5, 0]

    def callback50(event):
        root.focus_set()
        if B41.bind("<Button-1>", callback50):
            qXX[5, 0] += 1
            B41['text'] = qXX[5, 0]

    def b41():
        B41.bind("<Button-3>", callback_50)
        B41.bind("<Button-1>", callback50)

    def callback_51(event):
        root.focus_set()
        if B42.bind("<Button-3>", callback_51):
            qXX[5, 1] += -1
            B42['text'] = qXX[5, 1]

    def callback51(event):
        root.focus_set()
        if B42.bind("<Button-1>", callback51):
            qXX[5, 1] += 1
            B42['text'] = qXX[5, 1]

    def b42():
        B42.bind("<Button-3>", callback_51)
        B42.bind("<Button-1>", callback51)

    def callback_52(event):
        root.focus_set()
        if B43.bind("<Button-3>", callback_52):
            qXX[5, 2] += -1
            B43['text'] = qXX[5, 2]

    def callback52(event):
        root.focus_set()
        if B43.bind("<Button-1>", callback52):
            qXX[5, 2] += 1
            B43['text'] = qXX[5, 2]

    def b43():
        B43.bind("<Button-3>", callback_52)
        B43.bind("<Button-1>", callback52)

    def callback_53(event):
        root.focus_set()
        if B44.bind("<Button-3>", callback_53):
            qXX[5, 3] += -1
            B44['text'] = qXX[5, 3]

    def callback53(event):
        root.focus_set()
        if B44.bind("<Button-1>", callback53):
            qXX[5, 3] += 1
            B44['text'] = qXX[5, 3]

    def b44():
        B44.bind("<Button-3>", callback_53)
        B44.bind("<Button-1>", callback53)

    def callback_54(event):
        root.focus_set()
        if B45.bind("<Button-3>", callback_54):
            qXX[5, 4] += -1
            B45['text'] = qXX[5, 4]

    def callback54(event):
        root.focus_set()
        if B45.bind("<Button-1>", callback54):
            qXX[5, 4] += 1
            B45['text'] = qXX[5, 4]

    def b45():
        B45.bind("<Button-3>", callback_54)
        B45.bind("<Button-1>", callback54)

    def callback_55(event):
        root.focus_set()
        if B46.bind("<Button-3>", callback_55):
            qXX[5, 5] += -1
            B46['text'] = qXX[5, 5]

    def callback55(event):
        root.focus_set()
        if B46.bind("<Button-1>", callback55):
            qXX[5, 5] += 1
            B46['text'] = qXX[5, 5]

    def b46():
        B46.bind("<Button-3>", callback_55)
        B46.bind("<Button-1>", callback55)

    def callback_56(event):
        root.focus_set()
        if B47.bind("<Button-3>", callback_56):
            qXX[5, 6] += -1
            B47['text'] = qXX[5, 6]

    def callback56(event):
        root.focus_set()
        if B47.bind("<Button-1>", callback56):
            qXX[5, 6] += 1
            B47['text'] = qXX[5, 6]

    def b47():
        B47.bind("<Button-3>", callback_56)
        B47.bind("<Button-1>", callback56)

    def callback_57(event):
        root.focus_set()
        if B48.bind("<Button-3>", callback_57):
            qXX[5, 7] += -1
            B48['text'] = qXX[5, 7]

    def callback57(event):
        root.focus_set()
        if B48.bind("<Button-1>", callback57):
            qXX[5, 7] += 1
            B48['text'] = qXX[5, 7]

    def b48():
        B48.bind("<Button-3>", callback_57)
        B48.bind("<Button-1>", callback57)

    ######wiersz6##########

    def callback_60(event):
        root.focus_set()
        if B49.bind("<Button-3>", callback_60):
            qXX[6, 0] += -1
            B49['text'] = qXX[6, 0]

    def callback60(event):
        root.focus_set()
        if B49.bind("<Button-1>", callback60):
            qXX[6, 0] += 1
            B49['text'] = qXX[6, 0]

    def b49():
        B49.bind("<Button-3>", callback_60)
        B49.bind("<Button-1>", callback60)

    def callback_61(event):
        root.focus_set()
        if B50.bind("<Button-3>", callback_61):
            qXX[6, 1] += -1
            B50['text'] = qXX[6, 1]

    def callback61(event):
        root.focus_set()
        if B50.bind("<Button-1>", callback61):
            qXX[6, 1] += 1
            B50['text'] = qXX[6, 1]

    def b50():
        B50.bind("<Button-3>", callback_61)
        B50.bind("<Button-1>", callback61)

    def callback_62(event):
        root.focus_set()
        if B51.bind("<Button-3>", callback_62):
            qXX[6, 2] += -1
            B51['text'] = qXX[6, 2]

    def callback62(event):
        root.focus_set()
        if B51.bind("<Button-1>", callback62):
            qXX[6, 2] += 1
            B51['text'] = qXX[6, 2]

    def b51():
        B51.bind("<Button-3>", callback_62)
        B51.bind("<Button-1>", callback62)

    def callback_63(event):
        root.focus_set()
        if B52.bind("<Button-3>", callback_63):
            qXX[6, 3] += -1
            B52['text'] = qXX[6, 3]

    def callback63(event):
        root.focus_set()
        if B52.bind("<Button-1>", callback63):
            qXX[6, 3] += 1
            B52['text'] = qXX[6, 3]

    def b52():
        B52.bind("<Button-3>", callback_63)
        B52.bind("<Button-1>", callback63)

    def callback_64(event):
        root.focus_set()
        if B53.bind("<Button-3>", callback_64):
            qXX[6, 4] += -1
            B53['text'] = qXX[6, 4]

    def callback64(event):
        root.focus_set()
        if B53.bind("<Button-1>", callback64):
            qXX[6, 4] += 1
            B53['text'] = qXX[6, 4]

    def b53():
        B53.bind("<Button-3>", callback_64)
        B53.bind("<Button-1>", callback64)

    def callback_65(event):
        root.focus_set()
        if B54.bind("<Button-3>", callback_65):
            qXX[6, 5] += -1
            B54['text'] = qXX[6, 5]

    def callback65(event):
        root.focus_set()
        if B54.bind("<Button-1>", callback65):
            qXX[6, 5] += 1
            B54['text'] = qXX[6, 5]

    def b54():
        B54.bind("<Button-3>", callback_65)
        B54.bind("<Button-1>", callback65)

    def callback_66(event):
        root.focus_set()
        if B55.bind("<Button-3>", callback_66):
            qXX[6, 6] += -1
            B55['text'] = qXX[6, 6]

    def callback66(event):
        root.focus_set()
        if B55.bind("<Button-1>", callback66):
            qXX[6, 6] += 1
            B55['text'] = qXX[6, 6]

    def b55():
        B55.bind("<Button-3>", callback_66)
        B55.bind("<Button-1>", callback66)

    def callback_67(event):
        root.focus_set()
        if B56.bind("<Button-3>", callback_67):
            qXX[6, 7] += -1
            B56['text'] = qXX[6, 7]

    def callback67(event):
        root.focus_set()
        if B56.bind("<Button-1>", callback67):
            qXX[6, 7] += 1
            B56['text'] = qXX[6, 7]

    def b56():
        B56.bind("<Button-3>", callback_67)
        B56.bind("<Button-1>", callback67)

    ######wiersz7##########

    def callback_70(event):
        root.focus_set()
        if B57.bind("<Button-3>", callback_70):
            qXX[7, 0] += -1
            B57['text'] = qXX[7, 0]

    def callback70(event):
        root.focus_set()
        if B57.bind("<Button-1>", callback70):
            qXX[7, 0] += 1
            B57['text'] = qXX[7, 0]

    def b57():
        B57.bind("<Button-3>", callback_70)
        B57.bind("<Button-1>", callback70)

    def callback_71(event):
        root.focus_set()
        if B58.bind("<Button-3>", callback_71):
            qXX[7, 1] += -1
            B58['text'] = qXX[7, 1]

    def callback71(event):
        root.focus_set()
        if B58.bind("<Button-1>", callback71):
            qXX[7, 1] += 1
            B58['text'] = qXX[7, 1]

    def b58():
        B58.bind("<Button-3>", callback_71)
        B58.bind("<Button-1>", callback71)

    def callback_72(event):
        root.focus_set()
        if B59.bind("<Button-3>", callback_72):
            qXX[7, 2] += -1
            B59['text'] = qXX[7, 2]

    def callback72(event):
        root.focus_set()
        if B59.bind("<Button-1>", callback72):
            qXX[7, 2] += 1
            B59['text'] = qXX[7, 2]

    def b59():
        B59.bind("<Button-3>", callback_72)
        B59.bind("<Button-1>", callback72)

    def callback_73(event):
        root.focus_set()
        if B60.bind("<Button-3>", callback_73):
            qXX[7, 3] += -1
            B60['text'] = qXX[7, 3]

    def callback73(event):
        root.focus_set()
        if B60.bind("<Button-1>", callback73):
            qXX[7, 3] += 1
            B60['text'] = qXX[7, 3]

    def b60():
        B60.bind("<Button-3>", callback_73)
        B60.bind("<Button-1>", callback73)

    def callback_74(event):
        root.focus_set()
        if B61.bind("<Button-3>", callback_74):
            qXX[7, 4] += -1
            B61['text'] = qXX[7, 4]

    def callback74(event):
        root.focus_set()
        if B61.bind("<Button-1>", callback74):
            qXX[7, 4] += 1
            B61['text'] = qXX[7, 4]

    def b61():
        B61.bind("<Button-3>", callback_74)
        B61.bind("<Button-1>", callback74)

    def callback_75(event):
        root.focus_set()
        if B62.bind("<Button-3>", callback_75):
            qXX[7, 5] += -1
            B62['text'] = qXX[7, 5]

    def callback75(event):
        root.focus_set()
        if B62.bind("<Button-1>", callback75):
            qXX[7, 5] += 1
            B62['text'] = qXX[7, 5]

    def b62():
        B62.bind("<Button-3>", callback_75)
        B62.bind("<Button-1>", callback75)

    def callback_76(event):
        root.focus_set()
        if B63.bind("<Button-3>", callback_76):
            qXX[7, 6] += -1
            B63['text'] = qXX[7, 6]

    def callback76(event):
        root.focus_set()
        if B63.bind("<Button-1>", callback76):
            qXX[7, 6] += 1
            B63['text'] = qXX[7, 6]

    def b63():
        B63.bind("<Button-3>", callback_76)
        B63.bind("<Button-1>", callback76)

    def callback_77(event):
        root.focus_set()
        if B64.bind("<Button-3>", callback_77):
            qXX[7, 7] += -1
            B64['text'] = qXX[7, 7]

    def callback77(event):
        root.focus_set()
        if B64.bind("<Button-1>", callback77):
            qXX[7, 7] += 1
            B64['text'] = qXX[7, 7]

    def b64():
        B64.bind("<Button-3>", callback_77)
        B64.bind("<Button-1>", callback77)

    global matrixframe
    matrixframe.destroy()
    matrixframe = Frame(infoframe, width=352, height=352, bg='blue')
    matrixframe.place(x=20, y=20)
    B1 = Button(matrixframe, text=qXX[0, 0], command=b1)
    B1.place(width=43.75, height=43.75, x=0, y=0)

    B2 = Button(matrixframe, text=qXX[0, 1], command=b2)
    B2.place(width=43.75, height=43.75, x=43.75, y=0)

    B3 = Button(matrixframe, text=qXX[0, 2], command=b3)
    B3.place(width=43.75, height=43.75, x=87.5, y=0)

    B4 = Button(matrixframe, text=qXX[0, 3], command=b4)
    B4.place(width=43.75, height=43.75, x=132, y=0)

    B5 = Button(matrixframe, text=qXX[0, 4], command=b5)
    B5.place(width=43.75, height=43.75, x=176, y=0)

    B6 = Button(matrixframe, text=qXX[0, 5], command=b6)
    B6.place(width=43.75, height=43.75, x=219.75, y=0)

    B7 = Button(matrixframe, text=qXX[0, 6], command=b7)
    B7.place(width=43.75, height=43.75, x=263.75, y=0)

    B8 = Button(matrixframe, text=qXX[0, 7], command=b8)
    B8.place(width=43.75, height=43.75, x=307.75, y=0)

    B9 = Button(matrixframe, text=qXX[1, 0], command=b9)
    B9.place(width=43.75, height=43.75, x=0, y=43.75)

    B10 = Button(matrixframe, text=qXX[1, 1], command=b10)
    B10.place(width=43.75, height=43.75, x=43.75, y=43.75)

    B11 = Button(matrixframe, text=qXX[1, 2], command=b11)
    B11.place(width=43.75, height=43.75, x=87.5, y=43.75)

    B12 = Button(matrixframe, text=qXX[1, 3], command=b12)
    B12.place(width=43.75, height=43.75, x=132, y=43.75)

    B13 = Button(matrixframe, text=qXX[1, 4], command=b13)
    B13.place(width=43.75, height=43.75, x=176, y=43.75)

    B14 = Button(matrixframe, text=qXX[1, 5], command=b14)
    B14.place(width=43.75, height=43.75, x=219.75, y=43.75)

    B15 = Button(matrixframe, text=qXX[1, 6], command=b15)
    B15.place(width=43.75, height=43.75, x=263.75, y=43.75)

    B16 = Button(matrixframe, text=qXX[1, 7], command=b16)
    B16.place(width=43.75, height=43.75, x=307.75, y=43.75)

    B17 = Button(matrixframe, text=qXX[2, 0], command=b17)
    B17.place(width=43.75, height=43.75, x=0, y=87.5)

    B18 = Button(matrixframe, text=qXX[2, 1], command=b18)
    B18.place(width=43.75, height=43.75, x=43.75, y=87.5)

    B19 = Button(matrixframe, text=qXX[2, 2], command=b19)
    B19.place(width=43.75, height=43.75, x=87.5, y=87.5)

    B20 = Button(matrixframe, text=qXX[2, 3], command=b20)
    B20.place(width=43.75, height=43.75, x=132, y=87.5)

    B21 = Button(matrixframe, text=qXX[2, 4], command=b21)
    B21.place(width=43.75, height=43.75, x=176, y=87.5)

    B22 = Button(matrixframe, text=qXX[2, 5], command=b22)
    B22.place(width=43.75, height=43.75, x=219.75, y=87.5)

    B23 = Button(matrixframe, text=qXX[2, 6], command=b23)
    B23.place(width=43.75, height=43.75, x=263.75, y=87.5)

    B24 = Button(matrixframe, text=qXX[2, 7], command=b24)
    B24.place(width=43.75, height=43.75, x=307.75, y=87.5)

    B25 = Button(matrixframe, text=qXX[3, 0], command=b25)
    B25.place(width=43.75, height=43.75, x=0, y=132)

    B26 = Button(matrixframe, text=qXX[3, 1], command=b26)
    B26.place(width=43.75, height=43.75, x=43.75, y=132)

    B27 = Button(matrixframe, text=qXX[3, 2], command=b27)
    B27.place(width=43.75, height=43.75, x=87.5, y=132)

    B28 = Button(matrixframe, text=qXX[3, 3], command=b28)
    B28.place(width=43.75, height=43.75, x=132, y=132)

    B29 = Button(matrixframe, text=qXX[3, 4], command=b29)
    B29.place(width=43.75, height=43.75, x=176, y=132)

    B30 = Button(matrixframe, text=qXX[3, 5], command=b30)
    B30.place(width=43.75, height=43.75, x=219.75, y=132)

    B31 = Button(matrixframe, text=qXX[3, 6], command=b31)
    B31.place(width=43.75, height=43.75, x=263.75, y=132)

    B32 = Button(matrixframe, text=qXX[3, 7], command=b32)
    B32.place(width=43.75, height=43.75, x=307.75, y=132)

    B33 = Button(matrixframe, text=qXX[4, 0], command=b33)
    B33.place(width=43.75, height=43.75, x=0, y=176)

    B34 = Button(matrixframe, text=qXX[4, 1], command=b34)
    B34.place(width=43.75, height=43.75, x=43.75, y=176)

    B35 = Button(matrixframe, text=qXX[4, 2], command=b35)
    B35.place(width=43.75, height=43.75, x=87.5, y=176)

    B36 = Button(matrixframe, text=qXX[4, 3], command=b36)
    B36.place(width=43.75, height=43.75, x=132, y=176)

    B37 = Button(matrixframe, text=qXX[4, 4], command=b37)
    B37.place(width=43.75, height=43.75, x=176, y=176)

    B38 = Button(matrixframe, text=qXX[4, 5], command=b38)
    B38.place(width=43.75, height=43.75, x=219.75, y=176)

    B39 = Button(matrixframe, text=qXX[4, 6], command=b39)
    B39.place(width=43.75, height=43.75, x=263.75, y=176)

    B40 = Button(matrixframe, text=qXX[4, 7], command=b40)
    B40.place(width=43.75, height=43.75, x=307.75, y=176)

    B41 = Button(matrixframe, text=qXX[5, 0], command=b41)
    B41.place(width=43.75, height=43.75, x=0, y=219.75)

    B42 = Button(matrixframe, text=qXX[5, 1], command=b42)
    B42.place(width=43.75, height=43.75, x=43.75, y=219.75)

    B43 = Button(matrixframe, text=qXX[5, 2], command=b43)
    B43.place(width=43.75, height=43.75, x=87.5, y=219.75)

    B44 = Button(matrixframe, text=qXX[5, 3], command=b44)
    B44.place(width=43.75, height=43.75, x=132, y=219.75)

    B45 = Button(matrixframe, text=qXX[5, 4], command=b45)
    B45.place(width=43.75, height=43.75, x=176, y=219.75)

    B46 = Button(matrixframe, text=qXX[5, 5], command=b46)
    B46.place(width=43.75, height=43.75, x=219.75, y=219.75)

    B47 = Button(matrixframe, text=qXX[5, 6], command=b47)
    B47.place(width=43.75, height=43.75, x=263.75, y=219.75)

    B48 = Button(matrixframe, text=qXX[5, 7], command=b48)
    B48.place(width=43.75, height=43.75, x=307.75, y=219.75)

    B49 = Button(matrixframe, text=qXX[6, 0], command=b49)
    B49.place(width=43.75, height=43.75, x=0, y=263.75)

    B50 = Button(matrixframe, text=qXX[6, 1], command=b50)
    B50.place(width=43.75, height=43.75, x=43.75, y=263.75)

    B51 = Button(matrixframe, text=qXX[6, 2], command=b51)
    B51.place(width=43.75, height=43.75, x=87.5, y=263.75)

    B52 = Button(matrixframe, text=qXX[6, 3], command=b52)
    B52.place(width=43.75, height=43.75, x=132, y=263.75)

    B53 = Button(matrixframe, text=qXX[6, 4], command=b53)
    B53.place(width=43.75, height=43.75, x=176, y=263.75)

    B54 = Button(matrixframe, text=qXX[6, 5], command=b54)
    B54.place(width=43.75, height=43.75, x=219.75, y=263.75)

    B55 = Button(matrixframe, text=qXX[6, 6], command=b55)
    B55.place(width=43.75, height=43.75, x=263.75, y=263.75)

    B56 = Button(matrixframe, text=qXX[6, 7], command=b56)
    B56.place(width=43.75, height=43.75, x=307.75, y=263.75)

    B57 = Button(matrixframe, text=qXX[7, 0], command=b57)
    B57.place(width=43.75, height=43.75, x=0, y=307.75)

    B58 = Button(matrixframe, text=qXX[7, 1], command=b58)
    B58.place(width=43.75, height=43.75, x=43.75, y=307.75)

    B59 = Button(matrixframe, text=qXX[7, 2], command=b59)
    B59.place(width=43.75, height=43.75, x=87.5, y=307.75)

    B60 = Button(matrixframe, text=qXX[7, 3], command=b60)
    B60.place(width=43.75, height=43.75, x=132, y=307.75)

    B61 = Button(matrixframe, text=qXX[7, 4], command=b61)
    B61.place(width=43.75, height=43.75, x=176, y=307.75)

    B62 = Button(matrixframe, text=qXX[7, 5], command=b62)
    B62.place(width=43.75, height=43.75, x=219.75, y=307.75)

    B63 = Button(matrixframe, text=qXX[7, 6], command=b63)
    B63.place(width=43.75, height=43.75, x=263.75, y=307.75)

    B64 = Button(matrixframe, text=qXX[7, 7], command=b64)
    B64.place(width=43.75, height=43.75, x=307.75, y=307.75)

Btnstart = Button(upframe, width=300, height=20, text="Start",bg="#ADFF2F", font='Times 15',command=zaladuj_photo)
Btnstart.place(width=340,height=30,x=150,y=55)
Btnstart.place(x=295,y=55)



root.mainloop()