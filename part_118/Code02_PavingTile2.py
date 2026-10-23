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

# 贴瓷砖的方法数(轮廓线dp+空间压缩)
# 给定两个参数n和m，表示n行m列的空白区域
# 有无限多的1*2规格的瓷砖，目标是严丝合缝的铺满所有的空白区域
# 返回有多少种铺满的方法
# 1 <= n, m <= 11
# 测试链接 : http://poj.org/problem?id=2411
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_PavingTile2:
    __java_fields__ = {'MAXN': 'MAXN', 'dp': 'dp', 'prepare': 'prepare', 'n': 'n', 'm': 'm', 'maxs': 'maxs'}
    MAXN = 0
    dp = None
    prepare = None
    n = 0
    m = 0
    maxs = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code02_PavingTile2.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code02_PavingTile2.m = jcast('int', jcast('int', jget(in_, 'nval')))
            Code02_PavingTile2.maxs = jcast('int', jcast('int', (1 << (Code02_PavingTile2.m & 31))))
            if ((Code02_PavingTile2.n != 0) or (Code02_PavingTile2.m != 0)):
                jcall(out, 'println', Code02_PavingTile2.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute():
        jstatic('Arrays', 'fill', Code02_PavingTile2.prepare, 0, Code02_PavingTile2.maxs, 1)
        i = jcast('int', jcast('int', (Code02_PavingTile2.n - 1)))
        while (i >= 0):
            # j == m
            s = jcast('int', 0)
            while (s < Code02_PavingTile2.maxs):
                jset(Code02_PavingTile2.dp[Code02_PavingTile2.m], s, Code02_PavingTile2.prepare[s])
                s = jcast('int', (s + 1))
            # 普通位置
            j = jcast('int', jcast('int', (Code02_PavingTile2.m - 1)))
            while (j >= 0):
                s = jcast('int', 0)
                while (s < Code02_PavingTile2.maxs):
                    ans = jcast('long', 0)
                    if (Code02_PavingTile2.get(s, j) == 1):
                        ans = jcast('long', Code02_PavingTile2.dp[jcast('int', jadd(j, 1))][Code02_PavingTile2.set(s, j, 0)])
                    else:
                        if (jcast('int', jadd(i, 1)) < Code02_PavingTile2.n):
                            ans = jcast('long', Code02_PavingTile2.dp[jcast('int', jadd(j, 1))][Code02_PavingTile2.set(s, j, 1)])
                        if ((jcast('int', jadd(j, 1)) < Code02_PavingTile2.m) and (Code02_PavingTile2.get(s, jcast('int', jadd(j, 1))) == 0)):
                            ans = jcast('long', jcast('long', jadd(ans, Code02_PavingTile2.dp[jcast('int', jadd(j, 2))][s])))
                    jset(Code02_PavingTile2.dp[j], s, ans)
                    s = jcast('int', (s + 1))
                j = jcast('int', (j - 1))
            # 设置prepare
            s = jcast('int', 0)
            while (s < Code02_PavingTile2.maxs):
                Code02_PavingTile2.prepare[s] = jcast('long', Code02_PavingTile2.dp[0][s])
                s = jcast('int', (s + 1))
            i = jcast('int', (i - 1))
        return jcast('long', Code02_PavingTile2.dp[0][0])

    @staticmethod
    def get(s, j):
        s = jcast('int', s)
        j = jcast('int', j)
        return jcast('int', jcast('int', (jcast('int', (s >> (j & 31))) & 1)))

    @staticmethod
    def set(s, j, v):
        s = jcast('int', s)
        j = jcast('int', j)
        v = jcast('int', v)
        return jcast('int', (jcast('int', (s & jcast('int', (~jcast('int', (1 << (j & 31))))))) if (v == 0) else jcast('int', (s | jcast('int', (1 << (j & 31)))))))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_PavingTile2.MAXN = jcast('int', 11)
Code02_PavingTile2.dp = jarray('long', [jcast('int', jadd(Code02_PavingTile2.MAXN, 1)), jcast('int', (1 << (Code02_PavingTile2.MAXN & 31)))])
Code02_PavingTile2.prepare = jarray('long', [jcast('int', (1 << (Code02_PavingTile2.MAXN & 31)))])
Code02_PavingTile2.n = jcast('int', 0)
Code02_PavingTile2.m = jcast('int', 0)
Code02_PavingTile2.maxs = jcast('int', 0)

if __name__ == '__main__':
    Code02_PavingTile2.main([])
