# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 区间内没有出现的最小自然数，Python版
# 给定一个长度为n的数组arr，下标1~n，一共有m条查询
# 每条查询 l r : 打印arr[l..r]内没有出现过的最小自然数，注意0是自然数
# 请用在线算法解决该问题，因为可以设计强制在线的要求，让离线算法失效
# 1 <= n、m <= 2 * 10^5
# 0 <= arr[i] <= 2 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P4137
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_MissingSmallest2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'n': 'n', 'm': 'm', 'arr': 'arr', 'root': 'root', 'left': 'left', 'right': 'right', 'lateLeft': 'lateLeft', 'cnt': 'cnt'}
    MAXN = 0
    MAXT = 0
    n = 0
    m = 0
    arr = None
    root = None
    left = None
    right = None
    # 数字范围中，每个数字出现的最晚位置中，最左的位置在哪
    lateLeft = None
    cnt = 0
    @staticmethod
    def build(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        rt = jcast('int', ((_java_obj_1 := Code02_MissingSmallest2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3])
        Code02_MissingSmallest2.lateLeft[rt] = jcast('int', 0)
        if (l < r):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            jset(Code02_MissingSmallest2.left, rt, Code02_MissingSmallest2.build(l, mid))
            jset(Code02_MissingSmallest2.right, rt, Code02_MissingSmallest2.build(jcast('int', jadd(mid, 1)), r))
        return jcast('int', rt)

    # 数字范围l~r，信息在i号节点
    # 数字范围上，jobi这个数字，最晚出现的位置更新为jobv
    # 返回新的头节点编号
    @staticmethod
    def update(jobi, jobv, l, r, i):
        jobi = jcast('int', jobi)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        rt = jcast('int', ((_java_obj_4 := Code02_MissingSmallest2), (_java_key_5 := 'cnt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        Code02_MissingSmallest2.left[rt] = jcast('int', Code02_MissingSmallest2.left[i])
        Code02_MissingSmallest2.right[rt] = jcast('int', Code02_MissingSmallest2.right[i])
        Code02_MissingSmallest2.lateLeft[rt] = jcast('int', Code02_MissingSmallest2.lateLeft[i])
        if (l == r):
            Code02_MissingSmallest2.lateLeft[rt] = jcast('int', jobv)
        else:
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (jobi <= mid):
                jset(Code02_MissingSmallest2.left, rt, Code02_MissingSmallest2.update(jobi, jobv, l, mid, Code02_MissingSmallest2.left[rt]))
            else:
                jset(Code02_MissingSmallest2.right, rt, Code02_MissingSmallest2.update(jobi, jobv, jcast('int', jadd(mid, 1)), r, Code02_MissingSmallest2.right[rt]))
            jset(Code02_MissingSmallest2.lateLeft, rt, jstatic('Math', 'min', Code02_MissingSmallest2.lateLeft[Code02_MissingSmallest2.left[rt]], Code02_MissingSmallest2.lateLeft[Code02_MissingSmallest2.right[rt]]))
        return jcast('int', rt)

    # 数字在l~r范围上，没有出现的最小自然数，课上重点图解
    @staticmethod
    def query(pos, l, r, i):
        pos = jcast('int', pos)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            return jcast('int', l)
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        if (Code02_MissingSmallest2.lateLeft[Code02_MissingSmallest2.left[i]] < pos):
            # l...mid范围上，每个数字最晚出现的位置中
            # 最左的位置如果在pos以左，说明l...mid范围上，一定有缺失的数字
            return jcast('int', Code02_MissingSmallest2.query(pos, l, mid, Code02_MissingSmallest2.left[i]))
        else:
            # 缺失的数字一定在mid+1....r范围
            # 因为l...r一定有缺失的数字才会来到这个范围的
            # 如果左侧不缺失，那缺失的数字一定在右侧范围上
            return jcast('int', Code02_MissingSmallest2.query(pos, jcast('int', jadd(mid, 1)), r, Code02_MissingSmallest2.right[i]))

    @staticmethod
    def prepare():
        Code02_MissingSmallest2.cnt = jcast('int', 0)
        jset(Code02_MissingSmallest2.root, 0, Code02_MissingSmallest2.build(0, Code02_MissingSmallest2.n))
        i = jcast('int', 1)
        while (i <= Code02_MissingSmallest2.n):
            if ((Code02_MissingSmallest2.arr[i] > Code02_MissingSmallest2.n) or (Code02_MissingSmallest2.arr[i] < 0)):
                Code02_MissingSmallest2.root[i] = jcast('int', Code02_MissingSmallest2.root[jcast('int', (i - 1))])
            else:
                jset(Code02_MissingSmallest2.root, i, Code02_MissingSmallest2.update(Code02_MissingSmallest2.arr[i], i, 0, Code02_MissingSmallest2.n, Code02_MissingSmallest2.root[jcast('int', (i - 1))]))
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code02_MissingSmallest2.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code02_MissingSmallest2.m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code02_MissingSmallest2.n):
            jcall(in_, 'nextToken')
            Code02_MissingSmallest2.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        Code02_MissingSmallest2.prepare()
        i = jcast('int', 1)
        l = 0
        r = 0
        while (i <= Code02_MissingSmallest2.m):
            jcall(in_, 'nextToken')
            l = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            r = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(out, 'println', Code02_MissingSmallest2.query(l, 0, Code02_MissingSmallest2.n, Code02_MissingSmallest2.root[r]))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_MissingSmallest2.MAXN = jcast('int', 200001)
Code02_MissingSmallest2.MAXT = jcast('int', jcast('int', (Code02_MissingSmallest2.MAXN * 22)))
Code02_MissingSmallest2.n = jcast('int', 0)
Code02_MissingSmallest2.m = jcast('int', 0)
Code02_MissingSmallest2.arr = jarray('int', [Code02_MissingSmallest2.MAXN])
Code02_MissingSmallest2.root = jarray('int', [Code02_MissingSmallest2.MAXN])
Code02_MissingSmallest2.left = jarray('int', [Code02_MissingSmallest2.MAXT])
Code02_MissingSmallest2.right = jarray('int', [Code02_MissingSmallest2.MAXT])
Code02_MissingSmallest2.lateLeft = jarray('int', [Code02_MissingSmallest2.MAXT])
Code02_MissingSmallest2.cnt = jcast('int', 0)

if __name__ == '__main__':
    Code02_MissingSmallest2.main([])
