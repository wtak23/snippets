`[Parent Directory] <./>`_

.. contents:: **Table of Contents**
    :depth: 2

.. sectnum::    
    :start: 1    

#########
decorator
#########
- http://stackoverflow.com/questions/739654/how-can-i-make-a-chain-of-function-decorators-in-python?rq=1
- http://stackoverflow.com/questions/489720/what-are-some-common-uses-for-python-decorators
- http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/

.. code:: python

    def print_warning(fn):
        def wrapper():
            warn('module-name changed from "pnc_tob" to "tob_pnc" on 06/22/2016',ImportWarning)
            print('module-name changed from "pnc_tob" to "tob_pnc" on 06/22/2016')
        return wrapper
    
    @print_warning
    def get_matched_subjects_0614():
        """ Get list of *matched* pnc/tob subjects
        pass

Using with arguments (``*args, **kwargs``)

.. code:: python

    def logger(func):
        def inner(*args, **kwargs): #1
            print "Arguments were: %s, %s" % (args, kwargs)
            return func(*args, **kwargs) #2
        return inner

    >>> @logger
    ... def foo1(x, y=1):
    ...     return x * y
    >>> @logger
    ... def foo2():
    ...     return 2
    >>> foo1(5, 4)
    Arguments were: (5, 4), {}
    20
    >>> foo1(1)
    Arguments were: (1,), {}
    1
    >>> foo2()
    Arguments were: (), {}
    2
