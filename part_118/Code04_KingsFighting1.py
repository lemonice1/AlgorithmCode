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

# 摆放国王的方法数(轮廓线dp)
# 给定两个参数n和k，表示n*n的区域内要摆放k个国王
# 国王可以攻击临近的8个方向，所以摆放时不能让任何两个国王打架
# 返回摆放的方法数
# 1 <= n <= 9
# 1 <= k <= n*n
# 测试链接 : https://www.luogu.com.cn/problem/P1896
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 不过更推荐写出空间压缩的版本
class Code04_KingsFighting1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXK': 'MAXK', 'dp': 'dp', 'n': 'n', 'kings': 'kings', 'maxs': 'maxs'}
    MAXN = 0
    MAXK = 0
    dp = None
    n = 0
    kings = 0
    maxs = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code04_KingsFighting1.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code04_KingsFighting1.kings = jcast('int', jcast('int', jget(in_, 'nval')))
        Code04_KingsFighting1.maxs = jcast('int', jcast('int', (1 << (Code04_KingsFighting1.n & 31))))
        jcall(out, 'println', Code04_KingsFighting1.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute():
        i = jcast('int', 0)
        while (i < Code04_KingsFighting1.n):
            j = jcast('int', 0)
            while (j < Code04_KingsFighting1.n):
                s = jcast('int', 0)
                while (s < Code04_KingsFighting1.maxs):
                    leftup = jcast('int', 0)
                    while (leftup <= 1):
                        k = jcast('int', 0)
                        while (k <= Code04_KingsFighting1.kings):
                            jset(Code04_KingsFighting1.dp[i][j][s][leftup], k, jcast('int', (-1)))
                            k = jcast('int', (k + 1))
                        leftup = jcast('int', (leftup + 1))
                    s = jcast('int', (s + 1))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('long', Code04_KingsFighting1.f(0, 0, 0, 0, Code04_KingsFighting1.kings))

    # 当前来到i行j列
    # i-1行中，[j..m-1]列有没有摆放国王，用s[j..m-1]号格子表示
    # i行中，[0..j-1]列有没有摆放国王，用s[0..j-1]号格子表示
    # s表示轮廓线的状况
    # (i-1, j-1)位置，也就是左上角，有没有摆放国王，用leftup表示
    # 国王还剩下k个需要去摆放
    # 返回有多少种摆放方法
    @staticmethod
    def f(i, j, s, leftup, k):
        i = jcast('int', i)
        j = jcast('int', j)
        s = jcast('int', s)
        leftup = jcast('int', leftup)
        k = jcast('int', k)
        if (i == Code04_KingsFighting1.n):
            return jcast('long', (1 if (k == 0) else 0))
        if (j == Code04_KingsFighting1.n):
            return jcast('long', Code04_KingsFighting1.f(jcast('int', jadd(i, 1)), 0, s, 0, k))
        if (Code04_KingsFighting1.dp[i][j][s][leftup][k] != jcast('int', (-1))):
            return jcast('long', Code04_KingsFighting1.dp[i][j][s][leftup][k])
        left = jcast('int', (0 if (j == 0) else Code04_KingsFighting1.get(s, jcast('int', (j - 1)))))
        up = jcast('int', Code04_KingsFighting1.get(s, j))
        rightup = jcast('int', Code04_KingsFighting1.get(s, jcast('int', jadd(j, 1))))
        ans = jcast('long', Code04_KingsFighting1.f(i, jcast('int', jadd(j, 1)), Code04_KingsFighting1.set(s, j, 0), up, k))
        if (((((k > 0) and (left == 0)) and (leftup == 0)) and (up == 0)) and (rightup == 0)):
            ans = jcast('long', jcast('long', jadd(ans, Code04_KingsFighting1.f(i, jcast('int', jadd(j, 1)), Code04_KingsFighting1.set(s, j, 1), up, jcast('int', (k - 1))))))
        jset(Code04_KingsFighting1.dp[i][j][s][leftup], k, ans)
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


Code04_KingsFighting1.MAXN = jcast('int', 9)
Code04_KingsFighting1.MAXK = jcast('int', 82)
Code04_KingsFighting1.dp = jarray('long', [Code04_KingsFighting1.MAXN, Code04_KingsFighting1.MAXN, jcast('int', (1 << (Code04_KingsFighting1.MAXN & 31))), 2, Code04_KingsFighting1.MAXK])
Code04_KingsFighting1.n = jcast('int', 0)
Code04_KingsFighting1.kings = jcast('int', 0)
Code04_KingsFighting1.maxs = jcast('int', 0)

if __name__ == '__main__':
    Code04_KingsFighting1.main([])
