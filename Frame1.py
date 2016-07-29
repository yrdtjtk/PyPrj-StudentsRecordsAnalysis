#Boa:Frame:Frame1
# -*- coding: utf-8 -*-

import wx
import wx.gizmos
import os
import modRec
import modPack

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BTNNETPACKANALYSIS, wxID_FRAME1BUTTON1, 
 wxID_FRAME1PANEL1, wxID_FRAME1TEXTCTRL1, wxID_FRAME1TEXTCTRL2, 
] = [wx.NewId() for _init_ctrls in range(6)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(86, 0), size=wx.Size(1261, 729),
              style=wx.DEFAULT_FRAME_STYLE,
              title=u'Record Format Analysis (NEW)')
        self.SetClientSize(wx.Size(1245, 691))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(1245, 691),
              style=wx.TAB_TRAVERSAL)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self.panel1, pos=wx.Point(0, 0), size=wx.Size(1240, 102),
              style=wx.TE_MULTILINE, value=u'')

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL2, name='textCtrl2',
              parent=self.panel1, pos=wx.Point(0, 104), size=wx.Size(1182, 584),
              style=wx.TE_MULTILINE, value=u'')

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1,
              label=u'\u8bb0\u5f55\u89e3\u6790', name='button1',
              parent=self.panel1, pos=wx.Point(1184, 104), size=wx.Size(56,
              120), style=0)
        self.button1.SetHelpText(u'')
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

        self.btnNetPackAnalysis = wx.Button(id=wxID_FRAME1BTNNETPACKANALYSIS,
              label=u'\u7f51\u7edc\u62a5\u6587\n\u89e3\u6790',
              name=u'btnNetPackAnalysis', parent=self.panel1, pos=wx.Point(1184,
              232), size=wx.Size(56, 456), style=0)
        self.btnNetPackAnalysis.Bind(wx.EVT_BUTTON,
              self.OnBtnNetPackAnalysisButton,
              id=wxID_FRAME1BTNNETPACKANALYSIS)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.SetIcon(wx.Icon(os.path.join('ico', 'eating.ico'), wx.BITMAP_TYPE_ICO))

    def OnButton1Button(self, event):
        self.textCtrl2.Value = ''
        for s in self.textCtrl1.Value.splitlines():
            print('s = %s' % s)
            self.textCtrl2.Value += modRec.AnlSysRec(s)
        event.Skip()

    def OnBtnNetPackAnalysisButton(self, event):
        self.textCtrl2.Value = ''
        for s in self.textCtrl1.Value.splitlines():
            print('s = %s' % s)
            t,c = s.split('=')
            if t.find('↑') >= 0:
                self.textCtrl2.Value += modPack.UpPackAnalysis(modPack.Unpack(c))
            elif t.find('↓') >= 0:
                self.textCtrl2.Value += modPack.DownPackAnalysis(modPack.Unpack(c))
        event.Skip()

