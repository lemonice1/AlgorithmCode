# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 最多线段重合问题
# 测试链接 : https://www.nowcoder.com/practice/1ae8d0b6bb4e4bcdbf64ec491f63fc37
# 测试链接 : https://leetcode.cn/problems/meeting-rooms-ii/
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_MaxCover:
    __java_fields__ = {'MAXN': 'MAXN', 'line': 'line', 'n': 'n', 'heap': 'heap', 'size': 'size'}
    MAXN = 0
    line = None
    n = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code02_MaxCover.n = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 0)
            while (i < Code02_MaxCover.n):
                jcall(in_, 'nextToken')
                jset(Code02_MaxCover.line[i], 0, jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                jset(Code02_MaxCover.line[i], 1, jcast('int', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code02_MaxCover.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute():
        # 堆的清空
        Code02_MaxCover.size = jcast('int', 0)
        # 线段一共有n条，line[0...n-1][2] : line[i][0] line[i][1], 左闭右闭
        # 所有线段，根据开始位置排序，结束位置无所谓
        # 比较器的用法
        # line [0...n) 排序 : 所有小数组，开始位置谁小谁在前
        jstatic('Arrays', 'sort', Code02_MaxCover.line, 0, Code02_MaxCover.n, (lambda a, b: (a[0] - b[0])))
        ans = jcast('int', 0)
        i = jcast('int', 0)
        while (i < Code02_MaxCover.n):
            # i : line[i][0] line[i][1]
            while ((Code02_MaxCover.size > 0) and (Code02_MaxCover.heap[0] <= Code02_MaxCover.line[i][0])):
                Code02_MaxCover.pop()
            Code02_MaxCover.add(Code02_MaxCover.line[i][1])
            ans = jcast('int', jstatic('Math', 'max', ans, Code02_MaxCover.size))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    # 小根堆，堆顶0位置
    heap = None
    # 堆的大小
    size = 0
    @staticmethod
    def add(x):
        x = jcast('int', x)
        Code02_MaxCover.heap[Code02_MaxCover.size] = jcast('int', x)
        i = jcast('int', ((_java_obj_1 := Code02_MaxCover), (_java_key_2 := 'size'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])
        while (Code02_MaxCover.heap[i] < Code02_MaxCover.heap[jcast('int', jdiv(jcast('int', (i - 1)), 2))]):
            Code02_MaxCover.swap(i, jcast('int', jdiv(jcast('int', (i - 1)), 2)))
            i = jcast('int', jcast('int', jdiv(jcast('int', (i - 1)), 2)))

    @staticmethod
    def pop():
        Code02_MaxCover.swap(0, ((_java_obj_4 := Code02_MaxCover), (_java_key_5 := 'size'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (-1)))))[3])
        i = jcast('int', 0)
        l = jcast('int', 1)
        while (l < Code02_MaxCover.size):
            try:
                best = jcast('int', (jcast('int', jadd(l, 1)) if ((jcast('int', jadd(l, 1)) < Code02_MaxCover.size) and (Code02_MaxCover.heap[jcast('int', jadd(l, 1))] < Code02_MaxCover.heap[l])) else l))
                best = jcast('int', (best if (Code02_MaxCover.heap[best] < Code02_MaxCover.heap[i]) else i))
                if (best == i):
                    raise JBreak(None)
                Code02_MaxCover.swap(i, best)
                i = jcast('int', best)
                l = jcast('int', jcast('int', jadd(jcast('int', (i * 2)), 1)))
            except JContinue as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
            except JBreak as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
                break

    @staticmethod
    def swap(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = jcast('int', Code02_MaxCover.heap[i])
        Code02_MaxCover.heap[i] = jcast('int', Code02_MaxCover.heap[j])
        Code02_MaxCover.heap[j] = jcast('int', tmp)

    # 也找到了leetcode测试链接
    # 测试链接 : https://leetcode.cn/problems/meeting-rooms-ii/
    # Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
    @staticmethod
    def minMeetingRooms(meeting):
        n = jcast('int', jget(meeting, 'length'))
        jstatic('Arrays', 'sort', meeting, (lambda a, b: (a[0] - b[0])))
        heap = jnew('PriorityQueue')
        ans = jcast('int', 0)
        i = jcast('int', 0)
        while (i < n):
            while ((not jcall(heap, 'isEmpty')) and (jcall(heap, 'peek') <= meeting[i][0])):
                jcall(heap, 'poll')
            jcall(heap, 'add', meeting[i][1])
            ans = jcast('int', jstatic('Math', 'max', ans, jcall(heap, 'size')))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    # 上面的leetcode题目是会员题，需要付费
    # 如果不想开通leetcode会员，还有一个类似的题，但是注意题意，和课上讲的有细微差别
    # 课上讲的题目，认为[1,4]、[4、5]可以严丝合缝接在一起，不算有重合
    # 但是如下链接的题目，认为[1,4]、[4、5]有重合部分，也就是4
    # 除此之外再无差别
    # 测试链接 : https://leetcode.cn/problems/divide-intervals-into-minimum-number-of-groups/
    # Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
    @staticmethod
    def minGroups(meeting):
        n = jcast('int', jget(meeting, 'length'))
        jstatic('Arrays', 'sort', meeting, (lambda a, b: (a[0] - b[0])))
        heap = jnew('PriorityQueue')
        ans = jcast('int', 0)
        i = jcast('int', 0)
        while (i < n):
            # 注意这里的判断
            while ((not jcall(heap, 'isEmpty')) and (jcall(heap, 'peek') < meeting[i][0])):
                jcall(heap, 'poll')
            jcall(heap, 'add', meeting[i][1])
            ans = jcast('int', jstatic('Math', 'max', ans, jcall(heap, 'size')))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_MaxCover.MAXN = jcast('int', 10001)
Code02_MaxCover.line = jarray('int', [Code02_MaxCover.MAXN, 2])
Code02_MaxCover.n = jcast('int', 0)
Code02_MaxCover.heap = jarray('int', [Code02_MaxCover.MAXN])
Code02_MaxCover.size = jcast('int', 0)

if __name__ == '__main__':
    Code02_MaxCover.main([])
