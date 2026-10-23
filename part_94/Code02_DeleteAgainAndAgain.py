# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 不停删除之后剩下的字符串
# 给定一个字符串s1，如果其中含有s2字符串，就删除最左出现的那个
# 删除之后s1剩下的字符重新拼接在一起，再删除最左出现的那个
# 如此周而复始，返回最终剩下的字符串
# 测试链接 : https://www.luogu.com.cn/problem/P4824
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_DeleteAgainAndAgain:
    __java_fields__ = {'s1': 's1', 's2': 's2', 'MAXN': 'MAXN', 'next': 'next', 'stack1': 'stack1', 'stack2': 'stack2', 'size': 'size'}
    s1 = None
    s2 = None
    MAXN = 0
    next = None
    stack1 = None
    stack2 = None
    size = 0
    @staticmethod
    def main(args):
        in_ = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_DeleteAgainAndAgain.s1 = jcall(jcall(in_, 'readLine'), 'toCharArray')
        Code02_DeleteAgainAndAgain.s2 = jcall(jcall(in_, 'readLine'), 'toCharArray')
        Code02_DeleteAgainAndAgain.compute()
        i = jcast('int', 0)
        while (i < Code02_DeleteAgainAndAgain.size):
            jcall(out, 'print', Code02_DeleteAgainAndAgain.s1[Code02_DeleteAgainAndAgain.stack1[i]])
            i = jcast('int', (i + 1))
        jcall(out, 'println')
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(in_, 'close')

    @staticmethod
    def compute():
        Code02_DeleteAgainAndAgain.size = jcast('int', 0)
        n = jcast('int', jget(Code02_DeleteAgainAndAgain.s1, 'length'))
        m = jcast('int', jget(Code02_DeleteAgainAndAgain.s2, 'length'))
        x = jcast('int', 0)
        y = jcast('int', 0)
        Code02_DeleteAgainAndAgain.nextArray(m)
        while (x < n):
            if (Code02_DeleteAgainAndAgain.s1[x] == Code02_DeleteAgainAndAgain.s2[y]):
                Code02_DeleteAgainAndAgain.stack1[Code02_DeleteAgainAndAgain.size] = jcast('int', x)
                Code02_DeleteAgainAndAgain.stack2[Code02_DeleteAgainAndAgain.size] = jcast('int', y)
                Code02_DeleteAgainAndAgain.size = jcast('int', (Code02_DeleteAgainAndAgain.size + 1))
                x = jcast('int', (x + 1))
                y = jcast('int', (y + 1))
            else:
                if (y == 0):
                    Code02_DeleteAgainAndAgain.stack1[Code02_DeleteAgainAndAgain.size] = jcast('int', x)
                    Code02_DeleteAgainAndAgain.stack2[Code02_DeleteAgainAndAgain.size] = jcast('int', jcast('int', (-1)))
                    Code02_DeleteAgainAndAgain.size = jcast('int', (Code02_DeleteAgainAndAgain.size + 1))
                    x = jcast('int', (x + 1))
                else:
                    y = jcast('int', Code02_DeleteAgainAndAgain.next[y])
            if (y == m):
                # 相当于栈直接弹出了m条记录
                Code02_DeleteAgainAndAgain.size = jcast('int', jcast('int', (Code02_DeleteAgainAndAgain.size - m)))
                y = jcast('int', (jcast('int', jadd(Code02_DeleteAgainAndAgain.stack2[jcast('int', (Code02_DeleteAgainAndAgain.size - 1))], 1)) if (Code02_DeleteAgainAndAgain.size > 0) else 0))

    @staticmethod
    def nextArray(m):
        m = jcast('int', m)
        Code02_DeleteAgainAndAgain.next[0] = jcast('int', jcast('int', (-1)))
        Code02_DeleteAgainAndAgain.next[1] = jcast('int', 0)
        i = jcast('int', 2)
        cn = jcast('int', 0)
        while (i < m):
            if (Code02_DeleteAgainAndAgain.s2[jcast('int', (i - 1))] == Code02_DeleteAgainAndAgain.s2[cn]):
                jset(Code02_DeleteAgainAndAgain.next, ((_java_old_1 := i), (i := jcast('int', (i + (1)))), _java_old_1)[2], (cn := jcast('int', (cn + (1)))))
            else:
                if (cn > 0):
                    cn = jcast('int', Code02_DeleteAgainAndAgain.next[cn])
                else:
                    jset(Code02_DeleteAgainAndAgain.next, ((_java_old_2 := i), (i := jcast('int', (i + (1)))), _java_old_2)[2], 0)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_DeleteAgainAndAgain.s1 = None
Code02_DeleteAgainAndAgain.s2 = None
Code02_DeleteAgainAndAgain.MAXN = jcast('int', 1000001)
Code02_DeleteAgainAndAgain.next = jarray('int', [Code02_DeleteAgainAndAgain.MAXN])
Code02_DeleteAgainAndAgain.stack1 = jarray('int', [Code02_DeleteAgainAndAgain.MAXN])
Code02_DeleteAgainAndAgain.stack2 = jarray('int', [Code02_DeleteAgainAndAgain.MAXN])
Code02_DeleteAgainAndAgain.size = jcast('int', 0)

if __name__ == '__main__':
    Code02_DeleteAgainAndAgain.main([])
