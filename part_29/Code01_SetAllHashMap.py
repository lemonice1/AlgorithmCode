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

# setAll功能的哈希表
# 测试链接 : https://www.nowcoder.com/practice/7c4559f138e74ceb9ba57d76fd169967
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_SetAllHashMap:
    __java_fields__ = {'map': 'map', 'setAllValue': 'setAllValue', 'setAllTime': 'setAllTime', 'cnt': 'cnt', 'n': 'n', 'op': 'op', 'a': 'a', 'b': 'b'}
    map = None
    setAllValue = 0
    setAllTime = 0
    cnt = 0
    @staticmethod
    def put(k, v):
        k = jcast('int', k)
        v = jcast('int', v)
        if jcall(Code01_SetAllHashMap.map, 'containsKey', k):
            value = jcall(Code01_SetAllHashMap.map, 'get', k)
            value[0] = jcast('int', v)
            jset(value, 1, ((_java_obj_1 := Code01_SetAllHashMap), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])
        else:
            jcall(Code01_SetAllHashMap.map, 'put', k, jarray('int', [None], [v, ((_java_obj_4 := Code01_SetAllHashMap), (_java_key_5 := 'cnt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]]))

    @staticmethod
    def setAll(v):
        v = jcast('int', v)
        Code01_SetAllHashMap.setAllValue = jcast('int', v)
        Code01_SetAllHashMap.setAllTime = jcast('int', ((_java_obj_7 := Code01_SetAllHashMap), (_java_key_8 := 'cnt'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4])

    @staticmethod
    def get(k):
        k = jcast('int', k)
        if (not jcall(Code01_SetAllHashMap.map, 'containsKey', k)):
            return jcast('int', jcast('int', (-1)))
        value = jcall(Code01_SetAllHashMap.map, 'get', k)
        if (value[1] > Code01_SetAllHashMap.setAllTime):
            return jcast('int', value[0])
        else:
            return jcast('int', Code01_SetAllHashMap.setAllValue)

    n = 0
    op = 0
    a = 0
    b = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            jcall(Code01_SetAllHashMap.map, 'clear')
            Code01_SetAllHashMap.setAllValue = jcast('int', 0)
            Code01_SetAllHashMap.setAllTime = jcast('int', jcast('int', (-1)))
            Code01_SetAllHashMap.cnt = jcast('int', 0)
            Code01_SetAllHashMap.n = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 0)
            while (i < Code01_SetAllHashMap.n):
                jcall(in_, 'nextToken')
                Code01_SetAllHashMap.op = jcast('int', jcast('int', jget(in_, 'nval')))
                if (Code01_SetAllHashMap.op == 1):
                    jcall(in_, 'nextToken')
                    Code01_SetAllHashMap.a = jcast('int', jcast('int', jget(in_, 'nval')))
                    jcall(in_, 'nextToken')
                    Code01_SetAllHashMap.b = jcast('int', jcast('int', jget(in_, 'nval')))
                    Code01_SetAllHashMap.put(Code01_SetAllHashMap.a, Code01_SetAllHashMap.b)
                else:
                    if (Code01_SetAllHashMap.op == 2):
                        jcall(in_, 'nextToken')
                        Code01_SetAllHashMap.a = jcast('int', jcast('int', jget(in_, 'nval')))
                        jcall(out, 'println', Code01_SetAllHashMap.get(Code01_SetAllHashMap.a))
                    else:
                        jcall(in_, 'nextToken')
                        Code01_SetAllHashMap.a = jcast('int', jcast('int', jget(in_, 'nval')))
                        Code01_SetAllHashMap.setAll(Code01_SetAllHashMap.a)
                i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_SetAllHashMap.map = jnew('HashMap')
Code01_SetAllHashMap.setAllValue = jcast('int', 0)
Code01_SetAllHashMap.setAllTime = jcast('int', 0)
Code01_SetAllHashMap.cnt = jcast('int', 0)
Code01_SetAllHashMap.n = jcast('int', 0)
Code01_SetAllHashMap.op = jcast('int', 0)
Code01_SetAllHashMap.a = jcast('int', 0)
Code01_SetAllHashMap.b = jcast('int', 0)

if __name__ == '__main__':
    Code01_SetAllHashMap.main([])
