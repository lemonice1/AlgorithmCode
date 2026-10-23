# -*- coding: utf-8 -*-
# Python 3 算法实现；中文题意、算法说明与原课程顺序对应。
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 最大频率栈
class Code06_MaximumFrequencyStack:
    __java_fields__ = {}
    # 测试链接 : https://leetcode.cn/problems/maximum-frequency-stack/
    class FreqStack:
        __java_fields__ = {'topTimes': 'topTimes', 'cntValues': 'cntValues', 'valueTimes': 'valueTimes'}
        # 出现的最大次数
        # topTimes：实例字段，在构造函数中初始化。
        # 每层节点
        # cntValues：实例字段，在构造函数中初始化。
        # 每一个数出现了几次
        # valueTimes：实例字段，在构造函数中初始化。
        def push(self, val):
            val = jcast('int', val)
            jcall(self.valueTimes, 'put', val, jadd(jcall(self.valueTimes, 'getOrDefault', val, 0), 1))
            curTopTimes = jcast('int', jcall(self.valueTimes, 'get', val))
            if (not jcall(self.cntValues, 'containsKey', curTopTimes)):
                jcall(self.cntValues, 'put', curTopTimes, jnew('ArrayList'))
            curTimeValues = jcall(self.cntValues, 'get', curTopTimes)
            jcall(curTimeValues, 'add', val)
            self.topTimes = jcast('int', jstatic('Math', 'max', self.topTimes, curTopTimes))

        def pop(self):
            topTimeValues = jcall(self.cntValues, 'get', self.topTimes)
            ans = jcast('int', jcall(topTimeValues, 'remove', jcast('int', (jcall(topTimeValues, 'size') - 1))))
            if (jcall(topTimeValues, 'size') == 0):
                jcall(self.cntValues, 'remove', ((_java_obj_1 := self), (_java_key_2 := 'topTimes'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (-1)))), _java_old_3)[4])
            times = jcast('int', jcall(self.valueTimes, 'get', ans))
            if (times == 1):
                jcall(self.valueTimes, 'remove', ans)
            else:
                jcall(self.valueTimes, 'put', ans, jcast('int', (times - 1)))
            return jcast('int', ans)

        def __init__(self, *args, _java_ctor=None):
            self.topTimes = jcast('int', 0)
            self.cntValues = jnew('HashMap')
            self.valueTimes = jnew('HashMap')
            if args:
                raise TypeError('This class has a no-argument constructor')


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


