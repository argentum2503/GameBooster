#Misha08
#-w
from tkinter import*
import keyboard
import os
def resetGPU():
    keyboard.press("win+ctrl+shift+b")
    keyboard.release("win+ctrl+shift+b")
def energyBOOST():
    os.system("powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61")
def cleanRAM():
    os.system("ipconfig/ flushdns")
def driversUPDATE():
    os.system("pnputil/ install")
def LITEBOOST():
    resetGPU()
    cleanRAM()
    driversUPDATE()
def BOOST():
    resetGPU()
    cleanRAM()
def MAXBOOST():
    energyBOOST()
    resetGPU()
    cleanRAM()
    driversUPDATE()
tk = Tk()
tk.geometry('250x200')
bt1 = Button(text="resetGPU", command=resetGPU)
bt2 = Button(text="energyBOOST", command=energyBOOST)
bt3 = Button(text="MAXBOOST", command=MAXBOOST)
bt4 = Button(text="cleanRAM", command=cleanRAM)
bt5 = Button(text="driversUPDATE", command=driversUPDATE)
bt6 = Button(text="LITEBOOST", command=LITEBOOST)
bt7 = Button(text="BOOST", command=BOOST)
tk.title("game-booster")
can = Canvas(tk, width=200, height=200, bg='white')
#can.pack()
bt1.pack()
bt2.pack()
bt4.pack()
bt5.pack()
bt7.pack()
bt6.pack()
bt3.pack()
tk.mainloop()
