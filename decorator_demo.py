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

import datetime
unknow_time = datetime.timedelta(seconds = 3)
print unknow_time
now_time = datetime.datetime.now()
print now_time
now =now_time- unknow_time
print now

