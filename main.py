'''
Author       : WuWei
LastEditors  : WuWei
Date         : 2021-07-16 09:14:00
LastEditTime : 2021-07-16 17:00:34
Description  : Do not edit
'''
# -*- coding: utf-8 -*-
import wx
from  moviepy.editor import *



class Entry(wx.Frame):

    def __init__(self, *args, **kw):
        super(Entry, self).__init__(*args, **kw)
        # self.FileName = wx.TextCtrl(self, pos=(5, 5), size=(230, 25))
        # self.FileContent = wx.TextCtrl(self, pos=(5, 35), size=(620, 480), style=(wx.TE_MULTILINE))
        self.InitUI()

    def InitUI(self):

        pnl = wx.Panel(self)
        closeButton = wx.Button(pnl, label='open file', pos=(360, 185))

        closeButton.Bind(wx.EVT_BUTTON, self.OnOpenFile)

        self.SetSize((800, 400))
        self.SetTitle('video2gif')
        self.Centre()

    def OnOpenFile(self, e):
        wildcard = 'All files(*.*)|*.*'
        dialog = wx.FileDialog(None, 'select', os.getcwd(), '', wildcard)
        if dialog.ShowModal() == wx.ID_OK:
            print(dialog.GetPath(), dialog.GetFilename(), dialog.GetFilenames())
            self.ToGif(dialog.GetPath(), dialog.GetFilename())

    def ToGif(self, path, name):
        clipVideo = VideoFileClip(path)
        final = clipVideo.write_gif(path.strip(name) + name + ".gif", fps=clipVideo.fps * 0.02)

def main():

    app = wx.App()
    ex = Entry(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()

