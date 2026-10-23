# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 接取落水的最小花盆
# 老板需要你帮忙浇花。给出 N 滴水的坐标，y 表示水滴的高度，x 表示它下落到 x 轴的位置
# 每滴水以每秒1个单位长度的速度下落。你需要把花盆放在 x 轴上的某个位置
# 使得从被花盆接着的第 1 滴水开始，到被花盆接着的最后 1 滴水结束，之间的时间差至少为 D
# 我们认为，只要水滴落到 x 轴上，与花盆的边沿对齐，就认为被接住
# 给出 N 滴水的坐标和 D 的大小，请算出最小的花盆的宽度 W
# 测试链接 : https://www.luogu.com.cn/problem/P2698
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_FallingWaterSmallestFlowerPot:
    __java_fields__ = {'MAXN': 'MAXN', 'arr': 'arr', 'n': 'n', 'd': 'd', 'maxDeque': 'maxDeque', 'minDeque': 'minDeque', 'maxh': 'maxh', 'maxt': 'maxt', 'minh': 'minh', 'mint': 'mint'}
    MAXN = 0
    arr = None
    n = 0
    d = 0
    maxDeque = None
    minDeque = None
    maxh = 0
    maxt = 0
    minh = 0
    mint = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code03_FallingWaterSmallestFlowerPot.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code03_FallingWaterSmallestFlowerPot.d = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 0)
            while (i < Code03_FallingWaterSmallestFlowerPot.n):
                jcall(in_, 'nextToken')
                jset(Code03_FallingWaterSmallestFlowerPot.arr[i], 0, jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                jset(Code03_FallingWaterSmallestFlowerPot.arr[i], 1, jcast('int', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            ans = jcast('int', Code03_FallingWaterSmallestFlowerPot.compute())
            jcall(out, 'println', (jcast('int', (-1)) if (ans == jget(Integer, 'MAX_VALUE')) else ans))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute():
        # arr[0...n-1][2]: x(0), 高度(1)
        # 所有水滴根据x排序，谁小谁在前
        jstatic('Arrays', 'sort', Code03_FallingWaterSmallestFlowerPot.arr, 0, Code03_FallingWaterSmallestFlowerPot.n, (lambda a, b: (a[0] - b[0])))
        Code03_FallingWaterSmallestFlowerPot.maxh = jcast('int', jset(Code03_FallingWaterSmallestFlowerPot, 'maxt', jset(Code03_FallingWaterSmallestFlowerPot, 'minh', jset(Code03_FallingWaterSmallestFlowerPot, 'mint', 0))))
        ans = jcast('int', jget(Integer, 'MAX_VALUE'))
        l = jcast('int', 0)
        r = jcast('int', 0)
        while (l < Code03_FallingWaterSmallestFlowerPot.n):
            # [l,r) : 水滴的编号
            # l : 当前花盘的左边界，arr[l][0]
            while ((not Code03_FallingWaterSmallestFlowerPot.ok()) and (r < Code03_FallingWaterSmallestFlowerPot.n)):
                Code03_FallingWaterSmallestFlowerPot.push(((_java_old_1 := r), (r := jcast('int', (r + (1)))), _java_old_1)[2])
            if Code03_FallingWaterSmallestFlowerPot.ok():
                ans = jcast('int', jstatic('Math', 'min', ans, jcast('int', (Code03_FallingWaterSmallestFlowerPot.arr[jcast('int', (r - 1))][0] - Code03_FallingWaterSmallestFlowerPot.arr[l][0]))))
            Code03_FallingWaterSmallestFlowerPot.pop(l)
            l = jcast('int', (l + 1))
        return jcast('int', ans)

    # 当前窗口 最大值 - 最小值 是不是>=d
    @staticmethod
    def ok():
        max = jcast('int', (Code03_FallingWaterSmallestFlowerPot.arr[Code03_FallingWaterSmallestFlowerPot.maxDeque[Code03_FallingWaterSmallestFlowerPot.maxh]][1] if (Code03_FallingWaterSmallestFlowerPot.maxh < Code03_FallingWaterSmallestFlowerPot.maxt) else 0))
        min = jcast('int', (Code03_FallingWaterSmallestFlowerPot.arr[Code03_FallingWaterSmallestFlowerPot.minDeque[Code03_FallingWaterSmallestFlowerPot.minh]][1] if (Code03_FallingWaterSmallestFlowerPot.minh < Code03_FallingWaterSmallestFlowerPot.mint) else 0))
        return jcast('boolean', (jcast('int', (max - min)) >= Code03_FallingWaterSmallestFlowerPot.d))

    @staticmethod
    def push(r):
        r = jcast('int', r)
        while ((Code03_FallingWaterSmallestFlowerPot.maxh < Code03_FallingWaterSmallestFlowerPot.maxt) and (Code03_FallingWaterSmallestFlowerPot.arr[Code03_FallingWaterSmallestFlowerPot.maxDeque[jcast('int', (Code03_FallingWaterSmallestFlowerPot.maxt - 1))]][1] <= Code03_FallingWaterSmallestFlowerPot.arr[r][1])):
            Code03_FallingWaterSmallestFlowerPot.maxt = jcast('int', (Code03_FallingWaterSmallestFlowerPot.maxt - 1))
        jset(Code03_FallingWaterSmallestFlowerPot.maxDeque, ((_java_obj_2 := Code03_FallingWaterSmallestFlowerPot), (_java_key_3 := 'maxt'), (_java_old_4 := jget(_java_obj_2, _java_key_3)), jset(_java_obj_2, _java_key_3, jcast('int', (_java_old_4 + (1)))), _java_old_4)[4], r)
        while ((Code03_FallingWaterSmallestFlowerPot.minh < Code03_FallingWaterSmallestFlowerPot.mint) and (Code03_FallingWaterSmallestFlowerPot.arr[Code03_FallingWaterSmallestFlowerPot.minDeque[jcast('int', (Code03_FallingWaterSmallestFlowerPot.mint - 1))]][1] >= Code03_FallingWaterSmallestFlowerPot.arr[r][1])):
            Code03_FallingWaterSmallestFlowerPot.mint = jcast('int', (Code03_FallingWaterSmallestFlowerPot.mint - 1))
        jset(Code03_FallingWaterSmallestFlowerPot.minDeque, ((_java_obj_5 := Code03_FallingWaterSmallestFlowerPot), (_java_key_6 := 'mint'), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (1)))), _java_old_7)[4], r)

    @staticmethod
    def pop(l):
        l = jcast('int', l)
        if ((Code03_FallingWaterSmallestFlowerPot.maxh < Code03_FallingWaterSmallestFlowerPot.maxt) and (Code03_FallingWaterSmallestFlowerPot.maxDeque[Code03_FallingWaterSmallestFlowerPot.maxh] == l)):
            Code03_FallingWaterSmallestFlowerPot.maxh = jcast('int', (Code03_FallingWaterSmallestFlowerPot.maxh + 1))
        if ((Code03_FallingWaterSmallestFlowerPot.minh < Code03_FallingWaterSmallestFlowerPot.mint) and (Code03_FallingWaterSmallestFlowerPot.minDeque[Code03_FallingWaterSmallestFlowerPot.minh] == l)):
            Code03_FallingWaterSmallestFlowerPot.minh = jcast('int', (Code03_FallingWaterSmallestFlowerPot.minh + 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_FallingWaterSmallestFlowerPot.MAXN = jcast('int', 100005)
Code03_FallingWaterSmallestFlowerPot.arr = jarray('int', [Code03_FallingWaterSmallestFlowerPot.MAXN, 2])
Code03_FallingWaterSmallestFlowerPot.n = jcast('int', 0)
Code03_FallingWaterSmallestFlowerPot.d = jcast('int', 0)
Code03_FallingWaterSmallestFlowerPot.maxDeque = jarray('int', [Code03_FallingWaterSmallestFlowerPot.MAXN])
Code03_FallingWaterSmallestFlowerPot.minDeque = jarray('int', [Code03_FallingWaterSmallestFlowerPot.MAXN])
Code03_FallingWaterSmallestFlowerPot.maxh = jcast('int', 0)
Code03_FallingWaterSmallestFlowerPot.maxt = jcast('int', 0)
Code03_FallingWaterSmallestFlowerPot.minh = jcast('int', 0)
Code03_FallingWaterSmallestFlowerPot.mint = jcast('int', 0)

if __name__ == '__main__':
    Code03_FallingWaterSmallestFlowerPot.main([])
