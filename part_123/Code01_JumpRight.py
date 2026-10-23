# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 向右跳跃获得最大得分
# 给定长度为n+1的数组arr，下标编号0 ~ n，给定正数a、b
# 一开始在0位置，每次可以选择[a,b]之间的一个整数，作为向右跳跃的距离
# 每来到一个位置i，可以获得arr[i]作为得分，位置一旦大于n就停止
# 返回能获得的最大得分
# 1 <= n <= 2 * 10^5
# 1 <= a <= b <= n
# -1000 <= arr[i] <= +1000
# 测试链接 : https://www.luogu.com.cn/problem/P1725
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_JumpRight:
    __java_fields__ = {'MAXN': 'MAXN', 'NA': 'NA', 'arr': 'arr', 'dp': 'dp', 'queue': 'queue', 'l': 'l', 'r': 'r', 'n': 'n', 'a': 'a', 'b': 'b'}
    MAXN = 0
    NA = 0
    arr = None
    dp = None
    queue = None
    l = 0
    r = 0
    n = 0
    a = 0
    b = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code01_JumpRight.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code01_JumpRight.a = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code01_JumpRight.b = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 0)
        while (i <= Code01_JumpRight.n):
            jcall(in_, 'nextToken')
            Code01_JumpRight.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code01_JumpRight.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute():
        Code01_JumpRight.dp[0] = jcast('int', Code01_JumpRight.arr[0])
        Code01_JumpRight.l = jcast('int', jset(Code01_JumpRight, 'r', 0))
        i = jcast('int', 1)
        while (i <= Code01_JumpRight.n):
            Code01_JumpRight.add(jcast('int', (i - Code01_JumpRight.a)))
            Code01_JumpRight.overdue(jcast('int', (jcast('int', (i - Code01_JumpRight.b)) - 1)))
            Code01_JumpRight.dp[i] = jcast('int', (jcast('int', jadd(Code01_JumpRight.dp[Code01_JumpRight.queue[Code01_JumpRight.l]], Code01_JumpRight.arr[i])) if (Code01_JumpRight.l < Code01_JumpRight.r) else Code01_JumpRight.NA))
            i = jcast('int', (i + 1))
        ans = jcast('int', Code01_JumpRight.NA)
        i = jcast('int', jcast('int', (jcast('int', jadd(Code01_JumpRight.n, 1)) - Code01_JumpRight.b)))
        while (i <= Code01_JumpRight.n):
            ans = jcast('int', jstatic('Math', 'max', ans, Code01_JumpRight.dp[i]))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    @staticmethod
    def add(j):
        j = jcast('int', j)
        if ((j >= 0) and (Code01_JumpRight.dp[j] != Code01_JumpRight.NA)):
            while ((Code01_JumpRight.l < Code01_JumpRight.r) and (Code01_JumpRight.dp[Code01_JumpRight.queue[jcast('int', (Code01_JumpRight.r - 1))]] <= Code01_JumpRight.dp[j])):
                Code01_JumpRight.r = jcast('int', (Code01_JumpRight.r - 1))
            jset(Code01_JumpRight.queue, ((_java_obj_1 := Code01_JumpRight), (_java_key_2 := 'r'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], j)

    @staticmethod
    def overdue(t):
        t = jcast('int', t)
        if ((Code01_JumpRight.l < Code01_JumpRight.r) and (Code01_JumpRight.queue[Code01_JumpRight.l] == t)):
            Code01_JumpRight.l = jcast('int', (Code01_JumpRight.l + 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_JumpRight.MAXN = jcast('int', 200001)
Code01_JumpRight.NA = jcast('int', jget(Integer, 'MIN_VALUE'))
Code01_JumpRight.arr = jarray('int', [Code01_JumpRight.MAXN])
Code01_JumpRight.dp = jarray('int', [Code01_JumpRight.MAXN])
Code01_JumpRight.queue = jarray('int', [Code01_JumpRight.MAXN])
Code01_JumpRight.l = jcast('int', 0)
Code01_JumpRight.r = jcast('int', 0)
Code01_JumpRight.n = jcast('int', 0)
Code01_JumpRight.a = jcast('int', 0)
Code01_JumpRight.b = jcast('int', 0)

if __name__ == '__main__':
    Code01_JumpRight.main([])
