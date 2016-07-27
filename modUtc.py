#-*- coding: utf-8 -*-

import time
import datetime

def dt2utc(dt):
    print('---in dt2utc-----')
    print('in datetime str = %s' % dt)
    struct_tm = time.strptime(dt, '%Y-%m-%d %H:%M:%S')
    print('struct_tm = %s' % struct_tm)
    return '%08X' % int(time.mktime(struct_tm)-time.timezone)

def utc2dt(utc):
    print('---int utc2dt----')
    print('in utc str = %s' % utc)
    struct_tm = time.gmtime(int(utc, 16))
    print('struct_tm = %s' % struct_tm)
    return time.strftime('%Y-%m-%d %H:%M:%S', struct_tm)
    
##def utc2local(utc_st):
##    """UTC时间转本地时间（+8:00）"""
##    now_stamp = time.time()
##    local_time = datetime.datetime.fromtimestamp(now_stamp)
##    utc_time = datetime.datetime.utcfromtimestamp(now_stamp)
##    offset = local_time - utc_time
##    local_st = utc_st + offset
##    return local_st
##
##def local2utc(local_st):
##    """本地时间转UTC时间（-8:00）"""
##    time_struct = time.mktime(local_st.timetuple())
##    utc_st = datetime.datetime.utcfromtimestamp(time_struct)
##    return utc_st

if __name__ == '__main__':
##    utc_time = datetime.datetime(2014, 9, 18, 10, 42, 16, 126000)
##
##    # utc转本地
##    print 'utc_time=%s' % utc_time
##    local_time = utc2local(utc_time)
##    print 'local_time=%s' % local_time
##    print local_time.strftime("%Y-%m-%d %H:%M:%S")
##    # output：2014-09-18 18:42:16
##
##
##    # 本地转utc
##    utc_tran = local2utc(local_time)
##    print utc_tran.strftime("%Y-%m-%d %H:%M:%S")
##    # output：2014-09-18 10:42:16
    strDT = '2016-7-26 15:41:36'
    strUTC = dt2utc(strDT)
    print strUTC
    print utc2dt(strUTC)
