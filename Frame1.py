#Boa:Frame:Frame1
# -*- coding: utf-8 -*-

import wx
import wx.gizmos
import os
import modUtc

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1PANEL1, wxID_FRAME1TEXTCTRL1, 
 wxID_FRAME1TEXTCTRL2, 
] = [wx.NewId() for _init_ctrls in range(5)]

def AnlSysRec(Rec):
    Str = Rec + '\r\n'
    RecType = int(Rec[4:6],16)
    Str += '--------------------'
    if RecType in (0x02,0x03,0x10,0x11,0x12,0x13,0x14,0x15,0x20,0x21,0x22,0x23,0x24,0x25):
        if 0x02 == RecType:
            Str += '单票制消费记录'
        elif 0x03 == RecType:
            Str += '单票制消费灰记录'
        elif 0x10 == RecType:
            Str += '站点分段上车记录'
        elif 0x11 == RecType:
            Str += '站点分段上车灰记录'
        elif 0x12 == RecType:
            Str += '站点分段下车记录'
        elif 0x13 == RecType:
            Str += '站点分段下车灰记录'
        elif 0x14 == RecType:
            Str += '站点分段逃票罚款记录'
        elif 0x15 == RecType:
            Str += '站点分段逃票罚款灰记录'
        elif 0x20 == RecType:
            Str += '里程分段上车记录'
        elif 0x21 == RecType:
            Str += '里程分段上车灰记录'
        elif 0x22 == RecType:
            Str += '里程分段下车记录'
        elif 0x23 == RecType:
            Str += '里程分段下车灰记录'
        elif 0x24 == RecType:
            Str += '里程分段逃票罚款记录'
        elif 0x25 == RecType:
            Str += '里程分段逃票罚款灰记录'
        Str += '--------------------\r\n'
        Str += '终端交易流水号：%s\r\n' % Rec[0:4]
        Str += '交易类型：%s\r\n' % Rec[4:6]
        Str += 'SID：%s\r\n' % Rec[6:22]
        Str += '卡号：%s\r\n' % Rec[22:38]
        Str += '交易时间：%s (%s)\r\n' % (Rec[38:46], modUtc.utc2dt(Rec[38:46]))
        Str += '换乘标识：%s (%s)\r\n' % (Rec[46:48], {'00':'不采用换乘算法', '01':'未换乘消费', '02':'换乘消费'}[Rec[46:48]])
        Str += '卡类型：%s\r\n' % Rec[48:50]
        Str += '累计交易次数：%s (%d)\r\n' % (Rec[50:54], int(Rec[50:54], 16))
        Str += '原额：%s (%s元)\r\n' % (Rec[54:62], float(int(Rec[54:62],16))/100)
        Str += '交易金额：%s (%s元)\r\n' % (Rec[62:68],  float(int(Rec[62:68],16))/100)
        Str += '组号：%s\r\n' % Rec[68:72]
        Str += '充值计数器：%s (%d)\r\n' % (Rec[72:76], int(Rec[72:76], 16))
        Str += 'TAC：%s\r\n' % Rec[76:84]
        Str += '司机卡号：%s\r\n' % Rec[84:100]
        Str += '司机上班时间：%s (%s)\r\n' % (Rec[100:108],  modUtc.utc2dt(Rec[100:108]))
        Str += '应用单位参数：%s\r\n' % Rec[108:124]
        Str += 'CRC：%s\r\n' % Rec[124:128]
    elif 0x30 == RecType:
        Str += '扩展记录--------------------\r\n'
        Str += '终端交易流水号：%s\r\n' % Rec[0:4]
        Str += '交易类型：%s\r\n' % Rec[4:6]
        Str += '应用单位参数：%s\r\n' % Rec[6:22]
        Str += '卡号：%s\r\n' % Rec[22:38]
        Str += '交易时间：%s (%s)\r\n' % (Rec[38:46], modUtc.utc2dt(Rec[38:46]))
        Str += '对应消费记录交易类型：%s\r\n' % Rec[46:48]
        Str += '上车刷卡站号/公里数：%s\r\n' % Rec[48:52]
        Str += '下车刷卡站号/公里数：%s\r\n' % Rec[52:56]
        Str += '机具设置全程票价：%s (%s元)\r\n' % (Rec[56:62],  float(int(Rec[56:62],16))/100)
        Str += '分段计费折扣(正常折扣)：%s (%d)\r\n' % (Rec[62:64], int(Rec[62:64], 16))
        Str += '换乘折扣：%s (%d)\r\n' % (Rec[64:66], int(Rec[64:66], 16))
        Str += '是否为补贴记录：%s\r\n' % Rec[66:68]
        Str += '预留：%s\r\n' % Rec[68:72]
        Str += '伪随机数：%s\r\n' % Rec[72:80]
        Str += '换乘信息：%s\r\n' % Rec[80:104]
        Str += 'GPS坐标：%s\r\n' % Rec[104:124]
        Str += 'CRC：%s\r\n' % Rec[124:128]
    elif 0xD1 == RecType:
        Str += '司机上班记录--------------------\r\n'
        Str += '终端交易流水号：%s\r\n' % Rec[0:4]
        Str += '交易类型：%s\r\n' % Rec[4:6]
        Str += '卡种类：%s\r\n' % Rec[6:8]
        Str += '卡芯片号：%s\r\n' % Rec[8:22]
        Str += '卡号：%s\r\n' % Rec[22:38]
        Str += '应用单位序列号：%s\r\n' % Rec[38:54]
        Str += '交易时间：%s (%s)\r\n' % (Rec[54:62], modUtc.utc2dt(Rec[54:62]))
        Str += '记录生成方式：%s (%s)\r\n' % (Rec[62:64], {'01':'正常', '02':'采集后', '03':'隔日后', '04':'参数卡或设置卡设置后'}[Rec[62:64]])
        Str += '市郊车标志：%s\r\n' % Rec[64:66]
        Str += 'PSAM卡号：%s\r\n' % Rec[66:78]
        Str += 'SID：%s\r\n' % Rec[78:94]
        Str += '机具软件版本号：%s\r\n' % Rec[94:102]
        Str += '黑名单版本：%s\r\n' % Rec[102:110]
        Str += '预留：%s\r\n' % Rec[110:124]
        Str += 'CRC：%s\r\n' % Rec[124:128]
    elif 0xD0 == RecType:
        Str += '黑名单刷卡记录--------------------\r\n'
        Str += '终端交易流水号：%s\r\n' % Rec[0:4]
        Str += '交易类型：%s\r\n' % Rec[4:6]
        Str += 'SID：%s\r\n' % Rec[6:22]
        Str += '卡号：%s\r\n' % Rec[22:38]
        Str += '交易时间：%s (%s)\r\n' % (Rec[38:46], modUtc.utc2dt(Rec[38:46]))
        Str += '卡类型：%s\r\n' % Rec[46:48]
        Str += '钱包累计交易次数：%s (%d)\r\n' % (Rec[48:52], int(Rec[48:52], 16))
        Str += '原额：%s (%s元)\r\n' % (Rec[52:60], float(int(Rec[52:60],16))/100)
        Str += '组号：%s\r\n' % Rec[60:64]
        Str += '钱包充值计数器：%s (%d)\r\n' % (Rec[64:68], int(Rec[64:68], 16))
        Str += '黑名单版本：%s\r\n' % Rec[68:76]
        Str += '应用单位参数：%s\r\n' % Rec[76:92]
        Str += '上车刷卡站号/里程数：%s\r\n' % Rec[92:96]
        Str += 'GPS坐标：%s\r\n' % Rec[96:116]
        Str += '预留：%s\r\n' % Rec[116:124]
        Str += 'CRC：%s\r\n' % Rec[124:128]
    elif 0xD9 == RecType:
        Str += '设置卡设置记录--------------------\r\n'
        Str += '终端交易流水号：%s\r\n' % Rec[0:4]
        Str += '交易类型：%s\r\n' % Rec[4:6]
        Str += 'SID：%s\r\n' % Rec[6:22]
        Str += '卡号：%s\r\n' % Rec[22:38]
        Str += '设置时间：%s (%s)\r\n' % (Rec[38:46], modUtc.utc2dt(Rec[38:46]))
        Str += '记录生成方式：%s\r\n' % Rec[46:48]
        Str += '原车辆号：%s\r\n' % Rec[48:54]
        Str += '新车辆号：%s\r\n' % Rec[54:60]
        Str += 'GPS坐标：%s\r\n' % Rec[60:80]
        Str += '预留：%s\r\n' % Rec[80:124]
        Str += 'CRC：%s\r\n' % Rec[124:128]
    elif 0xDA == RecType:
        Str += '运参卡设置记录--------------------\r\n'
        Str += '终端交易流水号：%s\r\n' % Rec[0:4]
        Str += '交易类型：%s\r\n' % Rec[4:6]
        Str += 'SID：%s\r\n' % Rec[6:22]
        Str += '卡号：%s\r\n' % Rec[22:38]
        Str += '设置时间：%s (%s)\r\n' % (Rec[38:46], modUtc.utc2dt(Rec[38:46]))
        Str += '记录生成方式：%s (%s)\r\n' % (Rec[46:48], {'01':'刷运参卡', '02':'远程设置'}[Rec[46:48]])
        Str += '原应用单位参数：%s\r\n' % Rec[48:58]
        Str += '新应用单位参数：%s\r\n' % Rec[58:68]
        Str += '原票价表版本号：%s\r\n' % Rec[68:80]
        Str += '新票价表版本号：%s\r\n' % Rec[80:92]
        Str += 'GPS坐标：%s\r\n' % Rec[92:112]
        Str += '预留：%s\r\n' % Rec[112:124]
        Str += 'CRC：%s\r\n' % Rec[124:128]
    elif 0xDB == RecType:
        Str += '采集/补采集记录--------------------\r\n'
        Str += '终端交易流水号：%s\r\n' % Rec[0:4]
        Str += '交易类型：%s\r\n' % Rec[4:6]
        Str += 'SID：%s\r\n' % Rec[6:22]
        Str += '卡号：%s\r\n' % Rec[22:38]
        Str += '采集时间：%s (%s)\r\n' % (Rec[38:46], modUtc.utc2dt(Rec[38:46]))
        Str += '记录生成方式：%s (%s)\r\n' % (Rec[46:48], {'01':'采集', '02':'补采集'}[Rec[46:48]])
        Str += '采集机设备号：%s\r\n' % Rec[48:52]
        Str += '本次采集的总记录数：%s (%d)\r\n' % (Rec[52:56], int(Rec[52:56], 16))
        Str += '应用单位参数：%s\r\n' % Rec[56:72]
        Str += 'IC卡机通讯地址：%s\r\n' % Rec[72:74]
        Str += '采集点号：%s\r\n' % Rec[74:82]
        Str += '补采集日期(YYYYMMDD)：%s\r\n' % Rec[82:90]
        Str += 'GPS坐标：%s\r\n' % Rec[90:110]
        Str += '预留：%s\r\n' % Rec[110:124]
        Str += 'CRC：%s\r\n' % Rec[124:128]
    return Str
        
class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(20, 23), size=wx.Size(1258, 730),
              style=wx.DEFAULT_FRAME_STYLE,
              title=u'Record Format Analysis (NEW)')
        self.SetClientSize(wx.Size(1242, 692))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(1242, 692),
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
              584), style=0)
        self.button1.SetHelpText(u'')
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.SetIcon(wx.Icon(os.path.join('ico', 'eating.ico'), wx.BITMAP_TYPE_ICO))

    def OnButton1Button(self, event):
        self.textCtrl2.Value = ''
        for s in self.textCtrl1.Value.splitlines():
            print('s = %s' % s)
            self.textCtrl2.Value += AnlSysRec(s)
        event.Skip()

