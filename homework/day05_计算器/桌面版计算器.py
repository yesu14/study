#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-05-02 下午 12:50
#  @Note    :

import wx
import win32api
import sys, os

APP_TITLE = u'基本框架'
APP_ICON = 'res/python.ico'  # 请更换成你的icon


class mainFrame(wx.Frame):
    '''程序主窗口类，继承自wx.Frame'''

    def __init__(self):
        '''构造函数'''

        wx.Frame.__init__(self, None, -1, APP_TITLE, style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
        # 默认style是下列项的组合：wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN

        self.SetBackgroundColour(wx.Colour(224, 224, 224))
        self.SetSize((800, 600))
        self.Center()

        # 以下代码处理图标
        # if hasattr(sys, "frozen") and getattr(sys, "frozen") == "windows_exe":
        #     exeName = win32api.GetModuleFileName(win32api.GetModuleHandle(None))
        #     icon = wx.Icon(exeName, wx.BITMAP_TYPE_ICO)
        # else:
        #     icon = wx.Icon(APP_ICON, wx.BITMAP_TYPE_ICO)
        # self.SetIcon(icon)

        # 以下可以添加各类控件
        wx.StaticText(self,-1,u"请输入公式:",pos=(10,55),size=(100,50),style=wx.ALIGN_RIGHT)
        self.tc1 = wx.TextCtrl(self,-1,"",pos=(145,50),size=(400,50),name="TC01",style=wx.TE_CENTER)
        btn_mea = wx.Button(self, -1, u'鼠标左键事件', pos=(150, 130), size=(100, 50))

class mainApp(wx.App):
    def OnInit(self):
        self.SetAppName(APP_TITLE)
        self.Frame = mainFrame()
        self.Frame.Show()
        return True


if __name__ == "__main__":
    app = mainApp(redirect=True, filename="debug.txt")
    app.MainLoop()