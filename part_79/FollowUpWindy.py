# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# windy数，加强版
# 课上没有讲这个文件，这是windy数的加强版测试
# 需要改成long类型，除此之外和课上讲的完全一样
# 测试链接 : https://www.luogu.com.cn/problem/P13085
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class FollowUpWindy:
    __java_fields__ = {'MAXLEN': 'MAXLEN', 'dp': 'dp'}
    MAXLEN = 0
    dp = None
    @staticmethod
    def build(len):
        len = jcast('int', len)
        i = jcast('int', 0)
        while (i <= len):
            j = jcast('int', 0)
            while (j <= 10):
                jset(FollowUpWindy.dp[i][j], 0, jcast('int', (-1)))
                jset(FollowUpWindy.dp[i][j], 1, jcast('int', (-1)))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            a = jcast('long', jcast('long', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            b = jcast('long', jcast('long', jget(in_, 'nval')))
            jcall(out, 'println', FollowUpWindy.compute(a, b))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute(a, b):
        a = jcast('long', a)
        b = jcast('long', b)
        return jcast('long', jcast('long', (FollowUpWindy.cnt(b) - FollowUpWindy.cnt(jcast('long', (a - 1))))))

    @staticmethod
    def cnt(num):
        num = jcast('long', num)
        if (num == 0):
            return jcast('long', 1)
        len = jcast('int', 1)
        offset = jcast('long', 1)
        tmp = jcast('long', jcast('long', jdiv(num, 10)))
        while (tmp > 0):
            len = jcast('int', (len + 1))
            offset = jcast('long', jcast('long', (offset * 10)))
            tmp = jcast('long', jcast('long', jdiv(tmp, 10)))
        FollowUpWindy.build(len)
        return jcast('long', FollowUpWindy.f(num, offset, len, 10, 0))

    @staticmethod
    def f(num, offset, len, pre, free):
        num = jcast('long', num)
        offset = jcast('long', offset)
        len = jcast('int', len)
        pre = jcast('int', pre)
        free = jcast('int', free)
        if (len == 0):
            return jcast('long', 1)
        if (FollowUpWindy.dp[len][pre][free] != jcast('int', (-1))):
            return jcast('long', FollowUpWindy.dp[len][pre][free])
        cur = jcast('int', jcast('int', jcast('long', jmod(jcast('long', jdiv(num, offset)), 10))))
        ans = jcast('long', 0)
        if (free == 0):
            if (pre == 10):
                ans = jcast('long', jcast('long', jadd(ans, FollowUpWindy.f(num, jcast('long', jdiv(offset, 10)), jcast('int', (len - 1)), 10, 1))))
                i = jcast('int', 1)
                while (i < cur):
                    ans = jcast('long', jcast('long', jadd(ans, FollowUpWindy.f(num, jcast('long', jdiv(offset, 10)), jcast('int', (len - 1)), i, 1))))
                    i = jcast('int', (i + 1))
                ans = jcast('long', jcast('long', jadd(ans, FollowUpWindy.f(num, jcast('long', jdiv(offset, 10)), jcast('int', (len - 1)), cur, 0))))
            else:
                i = jcast('int', 0)
                while (i <= 9):
                    if ((i <= jcast('int', (pre - 2))) or (i >= jcast('int', jadd(pre, 2)))):
                        if (i < cur):
                            ans = jcast('long', jcast('long', jadd(ans, FollowUpWindy.f(num, jcast('long', jdiv(offset, 10)), jcast('int', (len - 1)), i, 1))))
                        else:
                            if (i == cur):
                                ans = jcast('long', jcast('long', jadd(ans, FollowUpWindy.f(num, jcast('long', jdiv(offset, 10)), jcast('int', (len - 1)), cur, 0))))
                    i = jcast('int', (i + 1))
        else:
            if (pre == 10):
                ans = jcast('long', jcast('long', jadd(ans, FollowUpWindy.f(num, jcast('long', jdiv(offset, 10)), jcast('int', (len - 1)), 10, 1))))
                i = jcast('int', 1)
                while (i <= 9):
                    ans = jcast('long', jcast('long', jadd(ans, FollowUpWindy.f(num, jcast('long', jdiv(offset, 10)), jcast('int', (len - 1)), i, 1))))
                    i = jcast('int', (i + 1))
            else:
                i = jcast('int', 0)
                while (i <= 9):
                    if ((i <= jcast('int', (pre - 2))) or (i >= jcast('int', jadd(pre, 2)))):
                        ans = jcast('long', jcast('long', jadd(ans, FollowUpWindy.f(num, jcast('long', jdiv(offset, 10)), jcast('int', (len - 1)), i, 1))))
                    i = jcast('int', (i + 1))
        jset(FollowUpWindy.dp[len][pre], free, ans)
        return jcast('long', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


FollowUpWindy.MAXLEN = jcast('int', 21)
FollowUpWindy.dp = jarray('long', [FollowUpWindy.MAXLEN, 11, 2])

if __name__ == '__main__':
    FollowUpWindy.main([])
