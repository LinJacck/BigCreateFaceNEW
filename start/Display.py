import time

import wx
from start.AttitudeDistinguish import attitude_distinguish


class AttitudeFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'好督导-课堂监督系统',size=(500,300))
        panel = wx.Panel(self)
        text1 = wx.TextCtrl(panel, pos=(150, 50), size=(200, 20), style=wx.ALIGN_CENTER_HORIZONTAL)  # 创建一个文本
        text1.SetValue("！！！开始进行检测！！！")
        attitude_distinguish()

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
        frame = AttitudeFrame(parent=None, id=-1)
        frame.Show()



if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = InsertFrame(parent=None,id=-1)
    frame.Show()
    app.MainLoop()

