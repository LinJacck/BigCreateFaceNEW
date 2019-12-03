import time

import cv2
import wx
import threading

from bin.face_display import FaceDisplay
from start.AttitudeDistinguish import attitude_distinguish


class AttitudeFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'好督导-课堂监督系统',size=(500,300))
        panel = wx.Panel(self)
        text1 = wx.TextCtrl(panel, pos=(150, 50), size=(200, 20), style=wx.ALIGN_CENTER_HORIZONTAL)  # 创建一个文本
        text1.SetValue("！！！开始进行检测！！！")
        attitude_distinguish()

class DisplayFrame(wx.Frame):
    """Frame class that displays an image."""
    def __init__(self, parent=None, id=-1,
                 pos=wx.DefaultPosition,
                 title='好督导-课堂监督系统'):
        """Create a Frame instance and display image."""
        wx.Frame.__init__(self, parent, id, title, pos,size = (800,500))
        self.panel = wx.Panel(self)
        start = wx.Button(self.panel, label="点击签到", pos=(660, 100), size=(100, 50))
        exit = wx.Button(self.panel, label="点击退出", pos=(660, 300), size=(100, 50))
        self.Show()
        cap = cv2.VideoCapture(0)
        start = FaceDisplay()
        thread = threading.Thread(target=self.ThreadDisplay(cap, start))
        thread.start()




    def ThreadDisplay(self,cap,start):
        start.start(cap)
        image = wx.Image('1.jpg', wx.BITMAP_TYPE_JPEG)
        temp = wx.Bitmap(image)
        self.bmp = wx.StaticBitmap(parent=self.panel, bitmap=temp,size=(600,500))
        self.Show()


class InsertFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'好督导-课堂监督系统',size=(500,300))
        panel = wx.Panel(self)
        text1 = wx.TextCtrl(panel, pos=(150, 50), size=(200, 20), style=wx.ALIGN_CENTER_HORIZONTAL)  # 创建一个文本
        text1.SetValue("欢迎使用：好督导-课堂监督系统")
        start = wx.Button(panel, label="点击登录", pos=(50, 140), size=(180, 50))
        exit = wx.Button(panel, label="点击退出", pos=(250, 140), size=(180, 50))
        self.Bind(wx.EVT_BUTTON, self.OnCloseStart, start)
        self.Bind(wx.EVT_BUTTON,self.OnCloseMe,exit)
        self.Bind(wx.EVT_CLOSE,self.OnCloseWindow)

    def OnCloseMe(self,event):
        self.Close(True)

    def OnCloseWindow(self,event):
        self.Destroy()

    def OnCloseStart(self,event):
        self.Close(True)
        # frame = AttitudeFrame(parent=None, id=-1)
        # frame.Show()
        # image = wx.Image('1.jpg', wx.BITMAP_TYPE_JPEG)
        # t = threading.Thread(target=FaceDisplay())
        # t.start()  # 启动线程，即让线程开始执行
        DisplayFrame()




if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = InsertFrame(parent=None,id=-1)
    frame.Show()
    app.MainLoop()

