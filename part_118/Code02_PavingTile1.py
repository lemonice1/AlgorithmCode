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

# 贴瓷砖的方法数(轮廓线dp)
# 给定两个参数n和m，表示n行m列的空白区域
# 有无限多的1*2规格的瓷砖，目标是严丝合缝的铺满所有的空白区域
# 返回有多少种铺满的方法
# 1 <= n, m <= 11
# 测试链接 : http://poj.org/problem?id=2411
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_PavingTile1:
    __java_fields__ = {'MAXN': 'MAXN', 'dp': 'dp', 'n': 'n', 'm': 'm', 'maxs': 'maxs'}
    MAXN = 0
    dp = None
    n = 0
    m = 0
    maxs = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code02_PavingTile1.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code02_PavingTile1.m = jcast('int', jcast('int', jget(in_, 'nval')))
            Code02_PavingTile1.maxs = jcast('int', jcast('int', (1 << (Code02_PavingTile1.m & 31))))
            if ((Code02_PavingTile1.n != 0) or (Code02_PavingTile1.m != 0)):
                jcall(out, 'println', Code02_PavingTile1.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute():
        i = jcast('int', 0)
        while (i < Code02_PavingTile1.n):
            j = jcast('int', 0)
            while (j < Code02_PavingTile1.m):
                s = jcast('int', 0)
                while (s < Code02_PavingTile1.maxs):
                    jset(Code02_PavingTile1.dp[i][j], s, jcast('int', (-1)))
                    s = jcast('int', (s + 1))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('long', Code02_PavingTile1.f(0, 0, 0))

    # 当前来到i行j列
    # i-1行中，[j..m-1]列有没有作为竖砖的上点，状况用s[j..m-1]表示
    # i行中，[0..j-1]列有没有作为竖砖的上点，状况用s[0..j-1]表示
    # s表示轮廓线的状况
    # 返回后续有几种摆放的方法
    @staticmethod
    def f(i, j, s):
        i = jcast('int', i)
        j = jcast('int', j)
        s = jcast('int', s)
        if (i == Code02_PavingTile1.n):
            return jcast('long', 1)
        if (j == Code02_PavingTile1.m):
            return jcast('long', Code02_PavingTile1.f(jcast('int', jadd(i, 1)), 0, s))
        if (Code02_PavingTile1.dp[i][j][s] != jcast('int', (-1))):
            return jcast('long', Code02_PavingTile1.dp[i][j][s])
        ans = jcast('long', 0)
        if (Code02_PavingTile1.get(s, j) == 1):
            ans = jcast('long', Code02_PavingTile1.f(i, jcast('int', jadd(j, 1)), Code02_PavingTile1.set(s, j, 0)))
            # 上方没有竖着摆砖
        else:
            # 当前竖着摆砖
            if (jcast('int', jadd(i, 1)) < Code02_PavingTile1.n):
                ans = jcast('long', Code02_PavingTile1.f(i, jcast('int', jadd(j, 1)), Code02_PavingTile1.set(s, j, 1)))
            # 当前横着摆砖
            if ((jcast('int', jadd(j, 1)) < Code02_PavingTile1.m) and (Code02_PavingTile1.get(s, jcast('int', jadd(j, 1))) == 0)):
                ans = jcast('long', jcast('long', jadd(ans, Code02_PavingTile1.f(i, jcast('int', jadd(j, 2)), s))))
        jset(Code02_PavingTile1.dp[i][j], s, ans)
        return jcast('long', ans)

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


Code02_PavingTile1.MAXN = jcast('int', 11)
Code02_PavingTile1.dp = jarray('long', [Code02_PavingTile1.MAXN, Code02_PavingTile1.MAXN, jcast('int', (1 << (Code02_PavingTile1.MAXN & 31)))])
Code02_PavingTile1.n = jcast('int', 0)
Code02_PavingTile1.m = jcast('int', 0)
Code02_PavingTile1.maxs = jcast('int', 0)

if __name__ == '__main__':
    Code02_PavingTile1.main([])
