# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 一群人落水后求每个位置的水位高度
# 问题描述比较复杂，见测试链接
# 测试链接 : https://www.luogu.com.cn/problem/P5026
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_WaterHeight:
    __java_fields__ = {'MAXN': 'MAXN', 'OFFSET': 'OFFSET', 'arr': 'arr', 'n': 'n', 'm': 'm'}
    # 题目说了m <= 10^6，代表湖泊宽度
    # 这就是MAXN的含义，湖泊最大宽度的极限
    MAXN = 0
    # 数值保护，因为题目中v最大是10000
    # 所以左侧影响最远的位置到达了x - 3 * v + 1
    # 所以右侧影响最远的位置到达了x + 3 * v - 1
    # x如果是正式的位置(1~m)，那么左、右侧可能超过正式位置差不多30000的规模
    # 这就是OFFSET的含义
    OFFSET = 0
    # 湖泊宽度是MAXN，是正式位置的范围
    # 左、右侧可能超过正式位置差不多OFFSET的规模
    # 所以准备一个长度为OFFSET + MAXN + OFFSET的数组
    # 这样一来，左侧影响最远的位置...右侧影响最远的位置，
    # 都可以被arr中的下标表示出来，就省去了很多越界讨论
    # 详细解释看set方法的注释
    arr = None
    n = 0
    m = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            # n有多少个人落水，每个人落水意味着四个等差数列操作
            Code03_WaterHeight.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            # 一共有多少位置，1~m个位置，最终要打印每个位置的水位
            Code03_WaterHeight.m = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 0)
            v = 0
            x = 0
            while (i < Code03_WaterHeight.n):
                jcall(in_, 'nextToken')
                v = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                x = jcast('int', jcast('int', jget(in_, 'nval')))
                # v体积的朋友，在x处落水，修改差分数组
                Code03_WaterHeight.fall(v, x)
                i = jcast('int', (i + 1))
            # 生成最终的水位数组
            Code03_WaterHeight.build()
            # 开始收集答案
            # 0...OFFSET这些位置是辅助位置，为了防止越界设计的
            # 从OFFSET+1开始往下数m个，才是正式的位置1...m
            # 打印这些位置，就是返回正式位置1...m的水位
            start = jcast('int', jcast('int', jadd(Code03_WaterHeight.OFFSET, 1)))
            jcall(out, 'print', Code03_WaterHeight.arr[((_java_old_1 := start), (start := jcast('int', (start + (1)))), _java_old_1)[2]])
            i = jcast('int', 2)
            while (i <= Code03_WaterHeight.m):
                jcall(out, 'print', jadd(' ', Code03_WaterHeight.arr[((_java_old_2 := start), (start := jcast('int', (start + (1)))), _java_old_2)[2]]))
                i = jcast('int', (i + 1))
            jcall(out, 'println')
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def fall(v, x):
        v = jcast('int', v)
        x = jcast('int', x)
        Code03_WaterHeight.set(jcast('int', jadd(jcast('int', (x - jcast('int', (3 * v)))), 1)), jcast('int', (x - jcast('int', (2 * v)))), 1, v, 1)
        Code03_WaterHeight.set(jcast('int', jadd(jcast('int', (x - jcast('int', (2 * v)))), 1)), x, jcast('int', (v - 1)), jcast('int', (-v)), jcast('int', (-1)))
        Code03_WaterHeight.set(jcast('int', jadd(x, 1)), jcast('int', jadd(x, jcast('int', (2 * v)))), jcast('int', jadd(jcast('int', (-v)), 1)), v, 1)
        Code03_WaterHeight.set(jcast('int', jadd(jcast('int', jadd(x, jcast('int', (2 * v)))), 1)), jcast('int', (jcast('int', jadd(x, jcast('int', (3 * v)))) - 1)), jcast('int', (v - 1)), 1, jcast('int', (-1)))

    @staticmethod
    def set(l, r, s, e, d):
        l = jcast('int', l)
        r = jcast('int', r)
        s = jcast('int', s)
        e = jcast('int', e)
        d = jcast('int', d)
        # 为了防止x - 3 * v + 1出现负数下标，进而有很多很烦的边界讨论
        # 所以任何位置，都加上一个较大的数字(OFFSET)
        # 这样一来，所有下标就都在0以上了，省去了大量边界讨论
        # 这就是为什么arr在初始化的时候要准备OFFSET + MAXN + OFFSET这么多的空间
        Code03_WaterHeight.arr[jcast('int', jadd(l, Code03_WaterHeight.OFFSET))] = jcast('int', jcast('int', jadd(Code03_WaterHeight.arr[jcast('int', jadd(l, Code03_WaterHeight.OFFSET))], s)))
        Code03_WaterHeight.arr[jcast('int', jadd(jcast('int', jadd(l, 1)), Code03_WaterHeight.OFFSET))] = jcast('int', jcast('int', jadd(Code03_WaterHeight.arr[jcast('int', jadd(jcast('int', jadd(l, 1)), Code03_WaterHeight.OFFSET))], jcast('int', (d - s)))))
        Code03_WaterHeight.arr[jcast('int', jadd(jcast('int', jadd(r, 1)), Code03_WaterHeight.OFFSET))] = jcast('int', jcast('int', (Code03_WaterHeight.arr[jcast('int', jadd(jcast('int', jadd(r, 1)), Code03_WaterHeight.OFFSET))] - jcast('int', jadd(d, e)))))
        Code03_WaterHeight.arr[jcast('int', jadd(jcast('int', jadd(r, 2)), Code03_WaterHeight.OFFSET))] = jcast('int', jcast('int', jadd(Code03_WaterHeight.arr[jcast('int', jadd(jcast('int', jadd(r, 2)), Code03_WaterHeight.OFFSET))], e)))

    @staticmethod
    def build():
        i = jcast('int', 1)
        while (i <= jcast('int', jadd(Code03_WaterHeight.m, Code03_WaterHeight.OFFSET))):
            Code03_WaterHeight.arr[i] = jcast('int', jcast('int', jadd(Code03_WaterHeight.arr[i], Code03_WaterHeight.arr[jcast('int', (i - 1))])))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= jcast('int', jadd(Code03_WaterHeight.m, Code03_WaterHeight.OFFSET))):
            Code03_WaterHeight.arr[i] = jcast('int', jcast('int', jadd(Code03_WaterHeight.arr[i], Code03_WaterHeight.arr[jcast('int', (i - 1))])))
            i = jcast('int', (i + 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_WaterHeight.MAXN = jcast('int', 1000001)
Code03_WaterHeight.OFFSET = jcast('int', 30001)
Code03_WaterHeight.arr = jarray('int', [jcast('int', jadd(jcast('int', jadd(Code03_WaterHeight.OFFSET, Code03_WaterHeight.MAXN)), Code03_WaterHeight.OFFSET))])
Code03_WaterHeight.n = jcast('int', 0)
Code03_WaterHeight.m = jcast('int', 0)

if __name__ == '__main__':
    Code03_WaterHeight.main([])
