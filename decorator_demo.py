# def deco(func):
#     def _deco(*args,**kwargs):
#         print 'before invoked'
#         result = func(*args,**kwargs)
#         print 'after invoked'
#         return result
#     return _deco
#
# @deco
# def f(a):
#     print 'f is invoked'
#     return a+1
#
# b = f(1)
# print b

# import datetime
# now = datetime.datetime.now() - datetime.timedelta(seconds = 3)
# print now

import socket
import fcntl
import struct
def get_ip(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915, # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

ip = get_ip('eth0')

print ip