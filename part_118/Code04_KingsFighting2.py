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

# 摆放国王的方法数(轮廓线dp+空间压缩)
# 给定两个参数n和k，表示n*n的区域内要摆放k个国王
# 国王可以攻击临近的8个方向，所以摆放时不能让任何两个国王打架
# 返回摆放的方法数
# 1 <= n <= 9
# 1 <= k <= n*n
# 测试链接 : https://www.luogu.com.cn/problem/P1896
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 空间压缩的版本一定稳定通过
class Code04_KingsFighting2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXK': 'MAXK', 'dp': 'dp', 'prepare': 'prepare', 'n': 'n', 'kings': 'kings', 'maxs': 'maxs'}
    MAXN = 0
    MAXK = 0
    dp = None
    prepare = None
    n = 0
    kings = 0
    maxs = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code04_KingsFighting2.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code04_KingsFighting2.kings = jcast('int', jcast('int', jget(in_, 'nval')))
        Code04_KingsFighting2.maxs = jcast('int', jcast('int', (1 << (Code04_KingsFighting2.n & 31))))
        jcall(out, 'println', Code04_KingsFighting2.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute():
        s = jcast('int', 0)
        while (s < Code04_KingsFighting2.maxs):
            k = jcast('int', 0)
            while (k <= Code04_KingsFighting2.kings):
                jset(Code04_KingsFighting2.prepare[s], k, (1 if (k == 0) else 0))
                k = jcast('int', (k + 1))
            s = jcast('int', (s + 1))
        i = jcast('int', jcast('int', (Code04_KingsFighting2.n - 1)))
        while (i >= 0):
            # j == n
            s = jcast('int', 0)
            while (s < Code04_KingsFighting2.maxs):
                k = jcast('int', 0)
                while (k <= Code04_KingsFighting2.kings):
                    jset(Code04_KingsFighting2.dp[Code04_KingsFighting2.n][s][0], k, Code04_KingsFighting2.prepare[s][k])
                    jset(Code04_KingsFighting2.dp[Code04_KingsFighting2.n][s][1], k, Code04_KingsFighting2.prepare[s][k])
                    k = jcast('int', (k + 1))
                s = jcast('int', (s + 1))
            # 普通位置
            j = jcast('int', jcast('int', (Code04_KingsFighting2.n - 1)))
            while (j >= 0):
                s = jcast('int', 0)
                while (s < Code04_KingsFighting2.maxs):
                    leftup = jcast('int', 0)
                    while (leftup <= 1):
                        k = jcast('int', 0)
                        while (k <= Code04_KingsFighting2.kings):
                            left = jcast('int', (0 if (j == 0) else Code04_KingsFighting2.get(s, jcast('int', (j - 1)))))
                            up = jcast('int', Code04_KingsFighting2.get(s, j))
                            rightup = jcast('int', Code04_KingsFighting2.get(s, jcast('int', jadd(j, 1))))
                            ans = jcast('long', Code04_KingsFighting2.dp[jcast('int', jadd(j, 1))][Code04_KingsFighting2.set(s, j, 0)][up][k])
                            if (((((k > 0) and (left == 0)) and (leftup == 0)) and (up == 0)) and (rightup == 0)):
                                ans = jcast('long', jcast('long', jadd(ans, Code04_KingsFighting2.dp[jcast('int', jadd(j, 1))][Code04_KingsFighting2.set(s, j, 1)][up][jcast('int', (k - 1))])))
                            jset(Code04_KingsFighting2.dp[j][s][leftup], k, ans)
                            k = jcast('int', (k + 1))
                        leftup = jcast('int', (leftup + 1))
                    s = jcast('int', (s + 1))
                j = jcast('int', (j - 1))
            # 设置prepare
            s = jcast('int', 0)
            while (s < Code04_KingsFighting2.maxs):
                k = jcast('int', 0)
                while (k <= Code04_KingsFighting2.kings):
                    jset(Code04_KingsFighting2.prepare[s], k, Code04_KingsFighting2.dp[0][s][0][k])
                    k = jcast('int', (k + 1))
                s = jcast('int', (s + 1))
            i = jcast('int', (i - 1))
        return jcast('long', Code04_KingsFighting2.dp[0][0][0][Code04_KingsFighting2.kings])

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


Code04_KingsFighting2.MAXN = jcast('int', 9)
Code04_KingsFighting2.MAXK = jcast('int', 82)
Code04_KingsFighting2.dp = jarray('long', [jcast('int', jadd(Code04_KingsFighting2.MAXN, 1)), jcast('int', (1 << (Code04_KingsFighting2.MAXN & 31))), 2, Code04_KingsFighting2.MAXK])
Code04_KingsFighting2.prepare = jarray('long', [jcast('int', (1 << (Code04_KingsFighting2.MAXN & 31))), Code04_KingsFighting2.MAXK])
Code04_KingsFighting2.n = jcast('int', 0)
Code04_KingsFighting2.kings = jcast('int', 0)
Code04_KingsFighting2.maxs = jcast('int', 0)

if __name__ == '__main__':
    Code04_KingsFighting2.main([])
