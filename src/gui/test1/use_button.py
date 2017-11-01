#coding=utf-8  
from tkinter import *  
  
def processOk():  
    print ("OK button is clicked.")  
  
def processCancel():  
    print ("Cancel button is clicked")  
  
# 创建一个窗口  
window = Tk()  
# 创建两个按钮  
btOk = Button(window,text = "OK", fg = "red", command = processOk)  
btCancel = Button(window,text = "cancel", bg = "yellow", command = processCancel)  
# 将按钮置在窗口上  
btOk.pack()  
btCancel.pack()  
# 创建一个事件循环，监测事件发生，直到窗口关闭  
window.mainloop()  