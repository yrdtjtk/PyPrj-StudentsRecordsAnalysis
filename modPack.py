# -*- coding: utf-8 -*-
import os
import modStr

mapFileType = {'41':'黑名单全表', '42':'黑名单差异表', '54':'梯形表', '4C':'参数表', '50':'程序文件'}

def IsPackValid(dt):
    if isinstance(dt, (str, unicode)):
        return True
    else:
        return False
    
def Pack(dt):
    print('In Func Pack,dt=%s' % dt)
    dt1 = dt.replace(' ', '')
    dt2 = dt1.upper()
    dt3 = modStr.multiple_replace(dt2, {'24':'5E01', '23':'5E02', '40':'5E03', '5E':'5E04'})
    return dt3

def Unpack(dt):
    print('In Func Unpack,dt=%s' % dt)
    dt1 = dt.replace(' ', '')
    dt2 = dt1.upper()
    dt3 = modStr.multiple_replace(dt2, {'5E01':'24', '5E02':'23', '5E03':'40', '5E04':'5E'})
    return dt3

def UpPackAnalysis(dt):
    ThrCmd = ''
    Str = ''
    if dt.startswith(('40', '24')) and dt.endswith('23'):
        Str += dt[0:2] + ' : 开始符\r\n'
        f = dt[2:4]
        Str += dt[2:4] + ' : 命令字\r\n'
        if 'EB' == f:
            f = int(dt[4:6], 16) + int(dt[6:8], 16)*256
            Str += dt[4:8] + ' : (%d) 数据块长度\r\n' % f
            Str += dt[8:10] + ' : 版本\r\n'
            Str += dt[10:22] + ' : 传输时间\r\n'
            Str += dt[22:26] + ' : 公司\r\n'
            Str += dt[26:32] + ' : 线路\r\n'
            Str += dt[32:38] + ' : 车辆\r\n'
            Str += dt[38:40] + ' : 设备类型\r\n'
            L1 = int(dt[40:42], 16)
            Str += dt[40:42+(L1*2)] + ' : 设备标识\r\n'
            f = dt[42+(L1*2):42+(L1*2)+4]
            Str += f + ' : (%d) 透传数据长度\r\n' % int(f, 16)
            dt1 = dt[42+(L1*2)+4:]
            ThrCmd = dt1[0:2]
            Str += '    ' + ThrCmd + ' : 数据类型\r\n'
            Str += '    ' + dt1[2:10] + ' : IC卡机号\r\n'
            Str += '    ' + dt1[10:26] + ' : 消息流水号\r\n'
            Str += '    ' + dt1[26:30] + ' : 公司号\r\n'
            Str += '    ' + dt1[30:36] + ' : 线路号\r\n'
            Str += '    ' + dt1[36:42] + ' : 车辆号\r\n'
            Str += '    ' + dt1[42:44] + ' : 设备类型\r\n'
            L2 = int(dt1[44:46], 16)
            Str += '    ' + dt1[44:46+(L2*2)] + ' : SID标志\r\n'
            dt2 = dt1[46+(L2*2):]
            if 'D1' == ThrCmd:
                Str = '----------------注册--发送---------------\r\n' + Str
                Str += '        ' + dt2[0:8] + ' : 程序版本\r\n'
                Str += '        ' + dt2[8:12] + ' : 程序CRC\r\n'
                Str += '        ' + dt2[12:20] + ' : 黑名单版本\r\n'
                Str += '        ' + dt2[20:24] + ' : 黑名单CRC\r\n'
                Str += '        ' + dt2[24:36] + ' : 参数版本\r\n'
                Str += '        ' + dt2[36:40] + ' : 参数CRC\r\n'
                Str += '        ' + dt2[40:48] + ' : 梯形表版本\r\n'
                Str += '        ' + dt2[48:52] + ' : 梯形表CRC\r\n'
                Str += '        ' + dt2[52:60] + ' : 白名单版本\r\n'
                Str += '        ' + dt2[60:64] + ' : 白名单CRC\r\n'
                Str += '        ' + dt2[64:72] + ' : 卡BIN文件版本\r\n'
                Str += '        ' + dt2[72:76] + ' : 卡BIN文件CRC\r\n'
                Str += '        ' + dt2[76:84] + ' : 公钥文件版本\r\n'
                Str += '        ' + dt2[84:88] + ' : 公钥文件CRC\r\n'
                Str += '        ' + dt2[88:90] + ' : 下载文件类型\r\n'
                Str += '        ' + dt2[90:102] + ' : 下载文件版本号\r\n'
                Str += '        ' + dt2[102:106] + ' : 下载文件当前包号\r\n'
                Str += '        ' + dt2[106:110] + ' : 下载文件总包号\r\n'
            elif 'D2' == ThrCmd:
                Str = '----------------上传记录--发送---------------\r\n' + Str
                RecNum = int(dt2[0:2], 16)
                Str += '        ' + dt2[0:2] + ' : (%d) 记录条数\r\n' % RecNum
                RecLen = int(dt2[2:4], 16)
                Str += '        ' + dt2[2:4] + ' : (%d) 记录宽度\r\n' % RecLen
                for i in range(RecNum):
                    Str += '          ' + dt2[4+(i*RecLen*2):4+((i+1)*RecLen*2)] + '\r\n'
            elif 'D3' == ThrCmd:
                FileType = dt2[0:2]
                Str = '----------------请求文件头--发送--%s-------------\r\n' % FileType + Str
                Str += '        ' + FileType + ' : (%s) 文件类型\r\n' % mapFileType[FileType]
                Str += '        ' + dt2[2:14] + ' : 文件当前版本\r\n'
                Str += '        ' + dt2[14:18] + ' : 文件CRC\r\n'
            elif 'D4' == ThrCmd:
                FileType = dt2[0:2]
                Str = '----------------请求文件体--发送--%s-------------\r\n' % FileType + Str
                Str += '        ' + FileType + ' : (%s) 文件类型\r\n' % mapFileType[FileType]
                Str += '        ' + dt2[2:14] + ' : 所请求文件的版本\r\n'
                f = dt2[14:18]
                Str += '        ' + f + ' : (%s) 所请求文件的包号\r\n' % int(f, 16)
                f = dt2[18:22]
                Str += '        ' + f + ' : (%s) 所请求文件的总包数\r\n' % int(f, 16)
            elif 'D5' == ThrCmd:
                Str = '----------------请求补采集任务--发送---------------\r\n' + Str
                Str += '        ' + dt2[0:12] + ' : 补采集任务标识\r\n'
            elif 'D6' == ThrCmd:
                Str = '----------------补采集记录上传--发送---------------\r\n' + Str
                Str += '        ' + dt2[0:12] + ' : 补采集任务标识\r\n'
                f = dt2[12:14]
                Str += '        ' + f + ' : (%s) 补采集模式\r\n' % {'00':'', '01':'按地址', '02':'按时间'}[f]
                Str += '        ' + dt2[14:18] + ' : 补采集开始地址\r\n'
                Str += '        ' + dt2[18:22] + ' : 补采集结束地址\r\n'
                Str += '        ' + dt2[22:26] + ' : 本包末条记录地址\r\n'
                RecNum = int(dt2[26:28], 16)
                Str += '        ' + dt2[26:28] + ' : (%d)记录条数\r\n' % RecNum
                RecLen = int(dt2[28:30], 16)
                Str += '        ' + dt2[28:30] + ' : (%d)记录宽度\r\n' % RecLen
                for i in range(RecNum):
                    Str += '          ' + dt2[30+(i*RecLen*2):30+((i+1)*RecLen*2)] + '\r\n'
            else:
                pass
        else:
            pass
        Str += dt[-4:-2] + ' : 校验位\r\n'
        Str += dt[-2:] + ' : 结束符\r\n'
    else:
        Str = ''
    return Str
    


def DownPackAnalysis(dt):
    ThrCmd = ''
    Str = ''
    if dt.startswith(('40', '24')) and dt.endswith('23'):
        Str += dt[0:2] + ' : 开始符\r\n'
        f = dt[2:4]
        Str += dt[2:4] + ' : 命令字\r\n'
        if 'EB' == f:
            f = int(dt[4:6], 16) + int(dt[6:8], 16)*256
            Str += dt[4:8] + ' : (%d) 数据块长度\r\n' % f
            Str += dt[8:10] + ' : 版本\r\n'
            Str += dt[10:22] + ' : 传输时间\r\n'
            Str += dt[22:26] + ' : 应答码\r\n'
            Str += dt[26:30] + ' : 公司\r\n'
            Str += dt[30:36] + ' : 线路\r\n'
            Str += dt[36:42] + ' : 车辆\r\n'
            Str += dt[42:44] + ' : 设备类型\r\n'
            L1 = int(dt[44:46], 16)
            Str += dt[44:46+(L1*2)] + ' : 设备标识\r\n'
            f = dt[46+(L1*2):46+(L1*2)+4]
            Str += f + ' : (%d) 透传数据长度\r\n' % int(f, 16)
            dt1 = dt[46+(L1*2)+4:]
            ThrCmd = dt1[0:2]
            Str += '    ' + ThrCmd + ' : 数据类型\r\n'
            Str += '    ' + dt1[2:10] + ' : IC卡机号\r\n'
            Str += '    ' + dt1[10:26] + ' : 消息流水号\r\n'
            Str += '    ' + dt1[26:30] + ' : 公司号\r\n'
            Str += '    ' + dt1[30:36] + ' : 线路号\r\n'
            Str += '    ' + dt1[36:42] + ' : 车辆号\r\n'
            Str += '    ' + dt1[42:44] + ' : 设备类型\r\n'
            L2 = int(dt1[44:46], 16)
            Str += '    ' + dt1[44:46+(L2*2)] + ' : SID标志\r\n'
            dt2 = dt1[46+(L2*2):]
            if 'C1' == ThrCmd:
                Str = '----------------注册--返回---------------\r\n' + Str
                Str += '        ' + dt2[0:14] + ' : 服务器时间\r\n'
            elif 'C2' == ThrCmd:
                Str = '----------------上传记录--返回---------------\r\n' + Str
                Str += '        ' + dt2[0:4] + ' : 末条记录地址\r\n'
            elif 'C3' == ThrCmd:
                FileType = dt2[0:2]
                Str = '----------------请求文件头--返回--%s-------------\r\n' % FileType + Str
                Str += '        ' + FileType + ' : (%s) 文件类型\r\n' % mapFileType[FileType]
                Str += '        ' + dt2[2:14] + ' : 文件当前版本\r\n'
                Str += '        ' + dt2[14:18] + ' : 文件CRC\r\n'
                f = dt2[18:26]
                Str += '        ' + f + ' : (%s) 所下发文件的长度\r\n' % int(f, 16)
                f = dt2[26:30]
                Str += '        ' + f + ' : (%s) 所下发文件的总包数\r\n' % int(f, 16)
            elif 'C4' == ThrCmd:
                FileType = dt2[2:4]
                Str = '----------------请求文件体--返回--%s-------------\r\n' % FileType + Str
                Str += '        ' + dt2[0:2] + ' : 响应代码\r\n'
                Str += '        ' + FileType + ' : (%s) 文件类型\r\n' % mapFileType[FileType]
                Str += '        ' + dt2[4:16] + ' : 所下发文件的版本\r\n'
                f = dt2[16:20]
                Str += '        ' + f + ' : (%s) 所下发文件的包号\r\n' % int(f, 16)
                f = dt2[20:24]
                Str += '        ' + f + ' : (%s) 所下发文件的总包数\r\n' % int(f, 16)
                Str += '        ' + dt2[24:-4] + ' : 所下发文件当前包的数据内容\r\n'
            elif 'C5' == ThrCmd:
                Str = '----------------请求补采集任务--返回---------------\r\n' + Str
                Str += '        ' + dt2[0:12] + ' : 补采集任务标识\r\n'
                f = dt2[12:14]
                Str += '        ' + f + ' : (%s) 补采集模式\r\n' % {'00':'', '01':'按地址', '02':'按时间'}[f]
                Str += '        ' + dt2[14:22] + ' : 补采集开始地址或时间\r\n'
                Str += '        ' + dt2[22:30] + ' : 补采集结束地址或时间\r\n'
                Str += '        ' + dt2[30:32] + ' : 是否断点续传\r\n'
                Str += '        ' + dt2[32:36] + ' : 断点续传地址\r\n'
            elif 'C6' == ThrCmd:
                Str = '----------------补采集记录上传--返回---------------\r\n' + Str
                Str += '        ' + dt2[0:12] + ' : 补采集任务标识\r\n'
                f = dt2[12:14]
                Str += '        ' + f + ' : (%s) 补采集模式\r\n' % {'00':'', '01':'按地址', '02':'按时间'}[f]
                Str += '        ' + dt2[14:18] + ' : 补采集开始地址\r\n'
                Str += '        ' + dt2[18:22] + ' : 补采集结束地址\r\n'
                Str += '        ' + dt2[22:26] + ' : 本包末条记录地址\r\n'
            else:
                pass
        else:
            pass
        Str += dt[-4:-2] + ' : 校验位\r\n'
        Str += dt[-2:] + ' : 结束符\r\n'
    else:
        Str = ''
    return Str
    


if __name__ == '__main__':
    s = '24 5 62 37 84 0a b5eff'
    b = Pack(s)
    print(b)
    c = Unpack(b)
    print(c)
    print('==================')
    s = '40EB71000110071C105E023501100100140088880208015E02456789ABCDEF0056D10088880A160728163553000C01100100140088880208015E02456789ABCDEF1607201200001607280431BE160728145249F4B50000000000000000000000000000000000000000000000004C16072814524900010001C223'
    print(UpPackAnalysis(Unpack(s)))