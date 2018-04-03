""" copy from https://segmentfault.com/a/1190000004238416"""

"""
demo 1
"""
def deco(func):
    def _deco():
        print 'before invoked'
        func()
        print 'after invoked'
    return _deco

@deco
def f():
    print 'f is invoked'

"""
demo 2
"""
def deco(func):
    def _deco(*args, **kwargs):
        print 'before invoked'
        ret = func(*args, **kwargs)
        print 'after invoded'
        return ret
    return _deco

@deco
def f(a):
    print 'f is invoked'
    return a + 1

"""
demo 3
"""

def deco(*args):
    def _deco(func):
        def __deco(*args, **kwargs):
            print 'decorator args is', args
            print 'before invoked'
            ret = func(*args, **kwargs)
            print 'after invoded'
            return ret
        return __deco
    return _deco

@deco('test')
def f(a):
    print 'f is invoked'
    return a + 1