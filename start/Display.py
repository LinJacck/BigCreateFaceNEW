import time

import cv2
import wx
import _thread

from bin.face_display import FaceDisplay
from common.global_read import GlobalRead
from common.global_write import GlobalWrite
from common.time_second import TimeSecond
from start.AttitudeDistinguish import attitude_distinguish
from start.FaceSearch import FaceSearch

def Contrast():#判断人脸签到
    result = FaceSearch()
    confirm = ConfirmFrame(parent=None,id=-1, result=result)
    # confirm.Confirm(result)
    # frame = AttitudeFrame(parent=None, id=-1)



class ConfirmFrame(wx.Frame):
    """Frame class that displays an image."""
    def __init__(self, parent, id, result):
        self.result = result
        wx.Frame.__init__(self, parent, id, '好督导-课堂监督系统', size=(500, 300))
        self.panel = wx.Panel(self)
        self.text1 = wx.TextCtrl(self.panel, pos=(150, 50), size=(200, 20), style=wx.ALIGN_CENTER_HORIZONTAL)  # 创建一个文本
        if result != 'no':
            text = '你是：  '+ result+ '  吗？'
            self.text1.SetValue(text)
            start = wx.Button(self.panel, label="是的", pos=(50, 140), size=(180, 50))
            exit = wx.Button(self.panel, label="不是", pos=(250, 140), size=(180, 50))
        if result == 'no':
            text = '抱歉数据库内未有你的信息，请联系管理员'
            self.text1.SetValue(text)
            exit = wx.Button(self.panel, label="好的", pos=(150, 140), size=(180, 50))
        self.Bind(wx.EVT_BUTTON, self.OnCloseStart, start)
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, exit)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        self.Show()

    def OnCloseMe(self,event):
        self.flag = 1
        self.Close(True)


    def OnCloseWindow(self,event):
        self.flag = 1
        self.Destroy()

    def OnCloseStart(self,event):
        self.Close(True)
        AttitudeFrame(parent=None, id=-1, result=self.result)

class AttitudeFrame(wx.Frame):
    def __init__(self,parent,id,result):
        self.flag = 0
        wx.Frame.__init__(self,parent,id,'好督导-课堂监督系统',size=(1000,500))
        self.panel = wx.Panel(self)
        text1 = wx.TextCtrl(self.panel, pos=(200, 5), size=(200, 20), style=wx.ALIGN_CENTER_HORIZONTAL)  # 创建一个文本
        text1.SetValue("！！！开始进行检测！！！")
        text2 = wx.TextCtrl(self.panel, pos=(700, 5), size=(200, 20), style=wx.ALIGN_CENTER_HORIZONTAL)  # 创建一个文本
        text = '==='+result + '课堂情况==='
        text2.SetValue(text)
        self.text3 = wx.TextCtrl(self.panel, pos=(650, 35), size=(300, 300),style = wx.BORDER_SIMPLE | wx.TE_MULTILINE | wx.HSCROLL)  # 创建一个文本
        _thread.start_new_thread(self.StartAttitude, ())
        _thread.start_new_thread(self.StartDraw, ())
        start = wx.Button(self.panel, label="课间\上课", pos=(650, 400), size=(130, 50))
        exit = wx.Button(self.panel, label="点击下课", pos=(800, 400), size=(130, 50))
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, exit)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        self.Bind(wx.EVT_BUTTON, self.OnCloseStart, self.StartDraw)
        GlobalWrite('good', 0)#初始化goodbad
        GlobalWrite('bad', 0)




    def StartAttitude(self):
        attitude_distinguish()


    def StartDraw(self):
        while (1):
            if self.flag == 1:
                break
            if TimeSecond() % 2 == 0:
                time.sleep(0.3)
                image = wx.Image('2.jpg', wx.BITMAP_TYPE_JPEG)
                temp = wx.Bitmap(image)
                self.bmp = wx.StaticBitmap(parent=self.panel, bitmap=temp,pos=(0, 25),size=(600,500))
                global_name = GlobalRead()
                global_time = global_name['time']
                if time.time()-global_time>3:
                    print(global_name['attitude'])
                    text = '\n'+time.strftime('%Y.%m.%d %H:%M:%S ',time.localtime(global_time))+'到'+time.strftime('%H:%M:%S ',time.localtime(time.time()))+global_name['attitude']
                    self.text3.AppendText(text)
                    GlobalWrite(global_name['attitude'],time.time())
                    if global_name['attitude'] == "GOOD_BOY":
                        global_good = global_name['good']
                        
            self.Show()


    def OnCloseMe(self,event):
        self.flag = 1
        self.Close(True)


    def OnCloseWindow(self,event):
        self.flag = 1
        self.Destroy()

class DisplayFrame(wx.Frame):
    """Frame class that displays an image."""
    def __init__(self, parent=None, id=-1,
                 pos=wx.DefaultPosition,
                 title='好督导-课堂监督系统'):
        """Create a Frame instance and display image."""
        self.flag = 0 #关机键
        wx.Frame.__init__(self, parent, id, title, pos,size = (800,500))
        self.panel = wx.Panel(self)
        start = wx.Button(self.panel, label="点击签到", pos=(650, 100), size=(100, 50))
        exit = wx.Button(self.panel, label="点击退出", pos=(650, 300), size=(100, 50))
        self.Show()
        cap = cv2.VideoCapture(0)
        started = FaceDisplay()
        _thread.start_new_thread(self.ThreadDisplay,(cap,started,exit,start))

    def ThreadDisplay(self,cap,started,exit,start):#线程启动摄像头
        while (1):
            if self.flag == 1:
                break
            self.Bind(wx.EVT_BUTTON, self.OnCloseMe, exit)
            self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
            self.Bind(wx.EVT_BUTTON, self.OnCloseStart, start)
            started.start(cap)
            image = wx.Image('1.jpg', wx.BITMAP_TYPE_JPEG)
            temp = wx.Bitmap(image)
            self.bmp = wx.StaticBitmap(parent=self.panel, bitmap=temp,size=(600,500))
            self.Show()


    def OnCloseMe(self,event):
        self.flag = 1
        self.Close(True)


    def OnCloseWindow(self,event):
        self.flag = 1
        self.Destroy()


    def OnCloseStart(self, event):
        self.flag = 1
        cd = cv2.imread('1.jpg')
        cv2.imwrite('3.jpg',cd)
        self.Close(True)
        Contrast()




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

