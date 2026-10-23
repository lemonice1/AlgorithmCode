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

# 过河踩过的最少石子数
# 在河上有一座独木桥，一只青蛙想沿着独木桥从河的一侧跳到另一侧
# 在桥上有一些石子，青蛙很讨厌踩在这些石子上
# 我们可以把独木桥上青蛙可能到达的点看成数轴上的一串整点0...n
# 其中n是桥的长度，坐标为0的点表示桥的起点，坐标为n的点表示桥的终点
# 青蛙从桥的起点开始，不停的向终点方向跳跃，一次跳跃的距离是[s,t]之间的任意正整数
# 当青蛙跳到或跳过坐标为n的点时，就算青蛙已经跳出了独木桥
# 题目给出独木桥的长度n，青蛙跳跃的距离范围s、t，题目还给定m个桥上石子的位置
# 你的任务是确定青蛙要想过河，最少需要踩到的石子数
# 1 <= n <= 10^7
# 1 <= s <= t <= 10
# 1 <= m <= 100
# 测试链接 : https://www.luogu.com.cn/problem/P1052
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_FrogCrossRiver:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXL': 'MAXL', 'arr': 'arr', 'where': 'where', 'dp': 'dp', 'stone': 'stone', 'n': 'n', 's': 's', 't': 't', 'm': 'm', 'safe': 'safe', 'MAXK': 'MAXK', 'reach': 'reach'}
    MAXN = 0
    MAXL = 0
    arr = None
    where = None
    dp = None
    stone = None
    n = 0
    s = 0
    t = 0
    m = 0
    safe = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code06_FrogCrossRiver.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code06_FrogCrossRiver.s = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code06_FrogCrossRiver.t = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code06_FrogCrossRiver.m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code06_FrogCrossRiver.m):
            jcall(in_, 'nextToken')
            Code06_FrogCrossRiver.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code06_FrogCrossRiver.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute():
        jstatic('Arrays', 'sort', Code06_FrogCrossRiver.arr, 1, jcast('int', jadd(Code06_FrogCrossRiver.m, 1)))
        if (Code06_FrogCrossRiver.s == Code06_FrogCrossRiver.t):
            ans = jcast('int', 0)
            i = jcast('int', 1)
            while (i <= Code06_FrogCrossRiver.m):
                if (jcast('int', jmod(Code06_FrogCrossRiver.arr[i], Code06_FrogCrossRiver.s)) == 0):
                    ans = jcast('int', (ans + 1))
                i = jcast('int', (i + 1))
            return jcast('int', ans)
            # s < t
        else:
            # 可以直接给一个足够安全的距离，不需要算
            # 因为s和t不大，都<= 10
            # safe = 201;
            Code06_FrogCrossRiver.safe = jcast('int', Code06_FrogCrossRiver.reduce(Code06_FrogCrossRiver.s, Code06_FrogCrossRiver.t))
            i = jcast('int', 1)
            while (i <= Code06_FrogCrossRiver.m):
                jset(Code06_FrogCrossRiver.where, i, jcast('int', jadd(Code06_FrogCrossRiver.where[jcast('int', (i - 1))], jstatic('Math', 'min', jcast('int', (Code06_FrogCrossRiver.arr[i] - Code06_FrogCrossRiver.arr[jcast('int', (i - 1))])), Code06_FrogCrossRiver.safe))))
                jset(Code06_FrogCrossRiver.stone, Code06_FrogCrossRiver.where[i], True)
                i = jcast('int', (i + 1))
            # where[m] + safe : 最后一颗石子 + 安全距离
            # 过了这个安全距离之后，dp值不会再有变化，也不会再遇到石子
            Code06_FrogCrossRiver.n = jcast('int', jcast('int', jadd(Code06_FrogCrossRiver.where[Code06_FrogCrossRiver.m], Code06_FrogCrossRiver.safe)))
            jstatic('Arrays', 'fill', Code06_FrogCrossRiver.dp, 1, jcast('int', jadd(Code06_FrogCrossRiver.n, 1)), Code06_FrogCrossRiver.MAXN)
            i = jcast('int', 1)
            while (i <= Code06_FrogCrossRiver.n):
                j = jcast('int', jstatic('Math', 'max', jcast('int', (i - Code06_FrogCrossRiver.t)), 0))
                while (j <= jcast('int', (i - Code06_FrogCrossRiver.s))):
                    jset(Code06_FrogCrossRiver.dp, i, jstatic('Math', 'min', Code06_FrogCrossRiver.dp[i], jcast('int', jadd(Code06_FrogCrossRiver.dp[j], (1 if Code06_FrogCrossRiver.stone[i] else 0)))))
                    j = jcast('int', (j + 1))
                i = jcast('int', (i + 1))
            ans = jcast('int', Code06_FrogCrossRiver.MAXN)
            i = jcast('int', jcast('int', jadd(Code06_FrogCrossRiver.where[Code06_FrogCrossRiver.m], 1)))
            while (i <= Code06_FrogCrossRiver.n):
                ans = jcast('int', jstatic('Math', 'min', ans, Code06_FrogCrossRiver.dp[i]))
                i = jcast('int', (i + 1))
            return jcast('int', ans)

    MAXK = 0
    reach = None
    # 一旦s和t定了，那么距离多远就可以缩减呢？
    # 做实验！
    @staticmethod
    def reduce(s, t):
        s = jcast('int', s)
        t = jcast('int', t)
        jstatic('Arrays', 'fill', Code06_FrogCrossRiver.reach, False)
        cnt = jcast('int', 0)
        ans = jcast('int', 0)
        i = jcast('int', 0)
        while (i < Code06_FrogCrossRiver.MAXK):
            try:
                j = jcast('int', jcast('int', jadd(i, s)))
                while (j < jstatic('Math', 'min', jcast('int', jadd(jcast('int', jadd(i, t)), 1)), Code06_FrogCrossRiver.MAXK)):
                    Code06_FrogCrossRiver.reach[j] = jcast('boolean', True)
                    j = jcast('int', (j + 1))
                if (not Code06_FrogCrossRiver.reach[i]):
                    cnt = jcast('int', 0)
                else:
                    cnt = jcast('int', (cnt + 1))
                if (cnt == t):
                    ans = jcast('int', i)
                    raise JBreak(None)
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_FrogCrossRiver.MAXN = jcast('int', 101)
Code06_FrogCrossRiver.MAXL = jcast('int', 100001)
Code06_FrogCrossRiver.arr = jarray('int', [Code06_FrogCrossRiver.MAXN])
Code06_FrogCrossRiver.where = jarray('int', [Code06_FrogCrossRiver.MAXN])
Code06_FrogCrossRiver.dp = jarray('int', [Code06_FrogCrossRiver.MAXL])
Code06_FrogCrossRiver.stone = jarray('boolean', [Code06_FrogCrossRiver.MAXL])
Code06_FrogCrossRiver.n = jcast('int', 0)
Code06_FrogCrossRiver.s = jcast('int', 0)
Code06_FrogCrossRiver.t = jcast('int', 0)
Code06_FrogCrossRiver.m = jcast('int', 0)
Code06_FrogCrossRiver.safe = jcast('int', 0)
Code06_FrogCrossRiver.MAXK = jcast('int', 201)
Code06_FrogCrossRiver.reach = jarray('boolean', [Code06_FrogCrossRiver.MAXK])

if __name__ == '__main__':
    Code06_FrogCrossRiver.main([])
