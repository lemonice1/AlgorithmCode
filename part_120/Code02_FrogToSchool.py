# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 上学需要的最少跳跃能力
# 青蛙住在一条河边，家在0位置, 每天到河对岸的上学，学校在n位置
# 河里的石头排成了一条直线，青蛙每次跳跃必须落在一块石头或者岸上
# 给定一个长度为n-1的数组arr，表示1~n-1位置每块石头的高度数值
# 每次青蛙从一块石头起跳，这块石头的高度就会下降1
# 当石头的高度下降到0时，青蛙不能再跳到这块石头上，跳跃后使石头高度下降到0是允许的
# 青蛙一共需要去学校上x天课, 所以它需要往返x次，青蛙具有跳跃能力y, 它可以跳跃不超过y的距离
# 请问青蛙的跳跃能力至少是多少，才能用这些石头往返x次
# 1 <= n <= 10^5
# 1 <= arr[i] <= 10^4
# 1 <= x <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P8775
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_FrogToSchool:
    __java_fields__ = {'MAXN': 'MAXN', 'arr': 'arr', 'n': 'n', 'x': 'x'}
    MAXN = 0
    arr = None
    n = 0
    x = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code02_FrogToSchool.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code02_FrogToSchool.x = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i < Code02_FrogToSchool.n):
            jcall(in_, 'nextToken')
            Code02_FrogToSchool.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        # 认为学校所在的位置n，有足够的高度
        Code02_FrogToSchool.arr[Code02_FrogToSchool.n] = jcast('int', jcast('int', (2 * Code02_FrogToSchool.x)))
        jcall(out, 'println', Code02_FrogToSchool.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute():
        ans = jcast('int', 0)
        # 窗口[l,r)，左闭右开！左闭右开！左闭右开！
        # 窗口内的累加和是sum
        # 当r来到n+1位置，那么窗口一定无法继续右扩了，因为n位置有足够的高度
        sum = jcast('long', Code02_FrogToSchool.arr[1])
        l = jcast('int', 1)
        r = jcast('int', 2)
        while (l <= Code02_FrogToSchool.n):
            while (sum < jcast('int', (Code02_FrogToSchool.x * 2))):
                sum = jcast('long', jcast('long', jadd(sum, Code02_FrogToSchool.arr[((_java_old_1 := r), (r := jcast('int', (r + (1)))), _java_old_1)[2]])))
            ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', (r - l))))
            sum = jcast('long', jcast('long', (sum - Code02_FrogToSchool.arr[l])))
            l = jcast('int', (l + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_FrogToSchool.MAXN = jcast('int', 100001)
Code02_FrogToSchool.arr = jarray('int', [Code02_FrogToSchool.MAXN])
Code02_FrogToSchool.n = jcast('int', 0)
Code02_FrogToSchool.x = jcast('int', 0)

if __name__ == '__main__':
    Code02_FrogToSchool.main([])
